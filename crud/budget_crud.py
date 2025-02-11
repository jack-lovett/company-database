from crud.base_crud import CRUDBase
from models.budget_model import Budget


class CRUDBudget(CRUDBase):
    def __init__(self):
        super().__init__(Budget)
