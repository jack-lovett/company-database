from app.crud.note_crud import CRUDNote
from app.services.base_service import BaseService


class NoteService(BaseService):
    def __init__(self):
        super().__init__(CRUDNote())
