from dataclasses import asdict, dataclass
import dataclasses
from datetime import datetime
import json


def timestamp_from_iso(raw_datetime: str) -> int:
    # Bad ISO example: '2022-05-03T20:11:07.93299+00:00'
    return int(datetime.strptime(raw_datetime, "%Y-%m-%dT%H:%M:%S.%f%z").timestamp())


@dataclass
class Note:
    rowid: int
    created_timestamp: int
    updated_timestamp: int
    username: str
    body: str

    def __post_init__(self):
        if isinstance(self.created_timestamp, str):
            self.created_timestamp = timestamp_from_iso(self.created_timestamp)
        if isinstance(self.updated_timestamp, str):
            self.updated_timestamp = timestamp_from_iso(self.updated_timestamp)


@dataclass
class CreateNoteRequest:
    username: str
    body: str

    def __post_init__(self):
        if len(self.username) > 140:
            raise Exception(f"Username: {self.username!r} too long. Max 140 char")
        if len(self.body) > 140:
            raise Exception(f"Body: {self.body!r} too long. Max 140 char")

    def as_string(self):
        return json.dumps(asdict(self))

    @classmethod
    def from_string(cls, json_string: str):
        return cls(**json.loads(json_string))
