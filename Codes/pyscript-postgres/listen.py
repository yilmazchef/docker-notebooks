import select
from pathlib import Path

import psycopg

env_lines = Path(".env.dev").read_text().split("\n")
env = dict((line.split("=") for line in env_lines if line != ""))

connection = psycopg.connect(
    host="localhost",
    port=int(env.get("POSTGRES_PORT")),
    dbname=env.get("POSTGRES_DB"),
    user=env.get("POSTGRES_USER"),
    password=env.get("POSTGRES_PASSWORD"),
    autocommit=True,
)

cursor = connection.cursor()
cursor.execute("LISTEN channel_note;")
print("Listening. Insert a note to get notifications.")

select.select([connection], [], [])
gen = connection.notifies()
while notify := next(gen):
    print("Got NOTIFY:", notify.pid, notify.channel, notify.payload)
