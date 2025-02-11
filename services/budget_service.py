from crud.budget_crud import CRUDBudget
from services.base_service import BaseService


class BudgetService(BaseService):
    def __init__(self):
        super().__init__(CRUDBudget())
