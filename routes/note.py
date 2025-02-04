from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.note import Note, NoteCreate
from services.note import NoteService

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("/", response_model=Note)
def create_note(note: NoteCreate, database: Session = Depends(get_database)):
    note_service = NoteService()
    return note_service.create(database, note.dict())


@router.get("/", response_model=list[Note])
def get_notes(database: Session = Depends(get_database)):
    note_service = NoteService()
    return note_service.get_all(database)
