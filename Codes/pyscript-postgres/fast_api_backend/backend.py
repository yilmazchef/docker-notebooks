import asyncio
import logging
import os
import select

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

import psycopg


logger = os.getenv("LOGGER", "uvicorn")
log = logging.getLogger(logger)
log.setLevel(logging.DEBUG)


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


def create_application() -> FastAPI:
    application = FastAPI()
    application.add_middleware(CORSMiddleware, allow_origins="*")
    return application


app = create_application()


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")


async def note_stream():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("LISTEN channel_note;")

    select.select([connection], [], [])
    gen = connection.notifies()
    while notify := next(gen):
        yield notify.payload


@app.route("/")
async def listen_notes(request):
    log.info("Listening")
    return StreamingResponse(note_stream())


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
