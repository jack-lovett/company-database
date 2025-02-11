from crud.base_crud import CRUDBase
from models.contractor_type_model import ContractorType


class CRUDContractor_type(CRUDBase):
    def __init__(self):
        super().__init__(ContractorType)
