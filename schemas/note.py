from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NoteBase(BaseModel):
    note_type: str
    note_content: str

class NoteCreate(NoteBase):
    pass  # No additional fields for creation

class NoteUpdate(NoteBase):
    note_type: Optional[str] = None
    note_content: Optional[str] = None

class Note(NoteBase):
    note_id: int
    project_id: int
    client_id: int
    note_creation_datetime: datetime

    class Config:
        from_attributes = True
