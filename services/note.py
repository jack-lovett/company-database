from crud.note import CRUDNote
from services.base import BaseService


class NoteService(BaseService):
    def __init__(self):
        super().__init__(CRUDNote())
