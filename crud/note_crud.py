from crud.base_crud import CRUDBase
from models.note_model import Note


class CRUDNote(CRUDBase):
    def __init__(self):
        super().__init__(Note)
