from crud.base import CRUDBase
from models.budget import Budget

class CRUDBudget(CRUDBase):
    def __init__(self):
        super().__init__(Budget)