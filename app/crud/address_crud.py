from app.crud.base_crud import CRUDBase
from app.models.address_model import Address


class CRUDAddress(CRUDBase):
    def __init__(self):
        super().__init__(Address)
