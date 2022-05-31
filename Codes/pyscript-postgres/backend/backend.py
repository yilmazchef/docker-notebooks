from gevent import monkey

monkey.patch_all()

import os
import select

from bottle import route, run, request, response, default_app, static_file
import gevent
import psycopg

from models import CreateNoteRequest


@route("/<:re:.*>", method="OPTIONS")
def cors():
    pass


@route("/")
@route("")
def index():
    return static_file("index.html", ".")


@route("/models.py")
def index():
    return static_file("models.py", ".")


def get_connection():
    connection = psycopg.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=int(os.getenv("POSTGRES_PORT")),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        autocommit=True,
    )
    return connection


@route("/listen_notes")
def listen_notes():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("LISTEN channel_note;")

    select.select([connection], [], [])
    gen = connection.notifies()
    while notify := next(gen):
        yield notify.payload


@route("/notes", method="POST")
def add_note():
    connection = get_connection()
    note = CreateNoteRequest.from_string(request.body.read())
    with connection.cursor() as cursor:
        cursor.execute(
            "INSERT INTO note(username, body) VALUES(%s, %s);",
            (note.username, note.body),
        )


def apply_cors():
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, DELETE, PUT, OPTIONS"
    response.headers[
        "Access-Control-Allow-Headers"
    ] = "Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token, Authorization"


if __name__ == "__main__":
    app = default_app()
    app.add_hook("after_request", apply_cors)
    run(
        app,
        host="0.0.0.0",
        port=os.getenv("PORT", 8080),
        server="gevent",
        reloader=True,
    )
