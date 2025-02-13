from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class NoteTypeEnum(str, Enum):
    comment = "comment"
    reminder = "reminder"
    follow_up = "follow_up"


class NoteBase(BaseModel):
    type: NoteTypeEnum
    content: str


class NoteCreate(NoteBase):
    project_id: int
    client_id: int


class NoteUpdate(NoteBase):
    type: Optional[NoteTypeEnum] = None
    content: Optional[str] = None


class Note(NoteBase):
    id: int
    project_id: int
    client_id: int
    creation_datetime: datetime

    class Config:
        from_attributes = True
