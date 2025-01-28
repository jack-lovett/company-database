from crud.base import CRUDBase
from models.contractor import Contractor

class CRUDContractor(CRUDBase):
    def __init__(self):
        super().__init__(Contractor)