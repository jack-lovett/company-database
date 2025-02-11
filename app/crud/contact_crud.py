from app.crud.base_crud import CRUDBase
from app.models.contact_model import Contact


class CRUDContact(CRUDBase):
    def __init__(self):
        super().__init__(Contact)
