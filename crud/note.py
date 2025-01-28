from crud.base import CRUDBase
from models.note import Note

class CRUDNote(CRUDBase):
    def __init__(self):
        super().__init__(Note)