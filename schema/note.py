from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class Note(BaseModel):
    note_id: int
    project_id: int
    client_id: int
    note_type: str
    note_content: str
    note_creation_datetime: datetime

    class Config:
        orm_mode = True
