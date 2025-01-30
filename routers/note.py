from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.note import Note, NoteCreate, NoteUpdate
from services.note import NoteService

note_router = APIRouter()

note_service = NoteService()


@note_router.post("/", response_model=Note)
def create_note(obj: NoteCreate, database: Session = Depends(get_database)):
    return note_service.create(database, obj)


@note_router.get("/note_id", response_model=Note)
def get_note(note_id: int, database: Session = Depends(get_database)):
    return note_service.get_by_id(database, note_id)


@note_router.put("/note_id", response_model=Note)
def update_note(note_id: int, obj: NoteUpdate, database: Session = Depends(get_database)):
    return note_service.update(database, note_id, obj)


@note_router.delete("/note_id", response_model=Note)
def delete_note(note_id: int, database: Session = Depends(get_database)):
    return note_service.delete(database, note_id)


@note_router.get("/", response_model=List[Note])
def get_notes(database: Session = Depends(get_database)):
    return note_service.get_all(database)
