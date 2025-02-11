from app.crud.base_crud import CRUDBase
from app.models.note_model import Note


class CRUDNote(CRUDBase):
    def __init__(self):
        super().__init__(Note)
