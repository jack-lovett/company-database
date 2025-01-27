from crud.base import CRUDBase
from models.address import Address

class CRUDAddress(CRUDBase):
    def __init__(self):
        super().__init__(Address)