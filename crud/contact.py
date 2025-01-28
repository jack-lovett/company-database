from crud.base import CRUDBase
from models.contact import Contact

class CRUDContact(CRUDBase):
    def __init__(self):
        super().__init__(Contact)