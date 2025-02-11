from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.note_schema import Note, NoteCreate
from app.services.note_service import NoteService

router = APIRouter(prefix="/notes", tags=["notes"])


@router.post("/", response_model=Note)
def create_note(note: NoteCreate, database: Session = Depends(get_database)):
    note_service = NoteService()
    return note_service.create(database, note.dict())


@router.get("/", response_model=list[Note])
def get_notes(database: Session = Depends(get_database)):
    note_service = NoteService()
    return note_service.get_all(database)
