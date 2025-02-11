from crud.base_crud import CRUDBase
from models.contractor_model import Contractor


class CRUDContractor(CRUDBase):
    def __init__(self):
        super().__init__(Contractor)
