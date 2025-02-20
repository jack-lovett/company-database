from datetime import datetime
from enum import Enum
from typing import Optional

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship


class NoteType(str, Enum):
    comment = "comment"
    reminder = "reminder"
    follow_up = "follow_up"


class NoteBase(SQLModel):
    type: NoteType
    content: str = Field()
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    client_id: Optional[int] = Field(default=None, foreign_key="client.id")
    creation_datetime: datetime = Field(default_factory=datetime.utcnow)


class Note(NoteBase, table=True):
    __tablename__ = "note"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    client: Optional["Client"] = Relationship(back_populates="notes")
    project: Optional["Project"] = Relationship(back_populates="notes")


class NoteCreate(SQLModel):
    type: NoteType
    content: str
    project_id: int
    client_id: int


class NoteUpdate(SQLModel):
    type: Optional[NoteType] = None
    content: Optional[str] = None


class NoteDisplay(NoteBase):
    id: int
