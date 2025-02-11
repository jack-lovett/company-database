from crud.base_crud import CRUDBase
from models.address_model import Address


class CRUDAddress(CRUDBase):
    def __init__(self):
        super().__init__(Address)
