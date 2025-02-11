from app.crud.base_crud import CRUDBase
from app.models.contractor_type_model import ContractorType


class CRUDContractor_type(CRUDBase):
    def __init__(self):
        super().__init__(ContractorType)
