from crud.note_crud import CRUDNote
from services.base_service import BaseService


class NoteService(BaseService):
    def __init__(self):
        super().__init__(CRUDNote())
