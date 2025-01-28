from enum import Enum

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteTypeEnum(str, Enum):
    follow_up = "follow_up"
    resolved = "resolved"
    in_progress = "in_progress"

class NoteBase(BaseModel):
    note_type: NoteTypeEnum
    note_content: str

class NoteCreate(NoteBase):
    pass  # No additional fields for creation

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
