from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class NoteTypeEnum(str, Enum):
    comment = "comment"
    reminder = "reminder"
    follow_up = "follow_up"


class NoteBase(BaseModel):
    note_type: NoteTypeEnum
    note_content: str


class NoteCreate(NoteBase):
    project_id: int
    client_id: int


class NoteUpdate(NoteBase):
    note_type: Optional[NoteTypeEnum] = None
    note_content: Optional[str] = None


class Note(NoteBase):
    note_id: int
    project_id: int
    client_id: int
    note_creation_datetime: datetime

    class Config:
        from_attributes = True
