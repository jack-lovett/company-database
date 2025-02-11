from crud.base_crud import CRUDBase
from models.contact_model import Contact


class CRUDContact(CRUDBase):
    def __init__(self):
        super().__init__(Contact)
