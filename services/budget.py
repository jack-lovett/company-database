from crud.budget import CRUDBudget
from services.base import BaseService

class BudgetService(BaseService):
    def __init__(self):
        super().__init__(CRUDBudget())