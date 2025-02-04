from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.budget import Budget, BudgetCreate
from services.budget import BudgetService

router = APIRouter(prefix="/budgets", tags=["budgets"])


@router.post("/", response_model=Budget)
def create_client(client: BudgetCreate, database: Session = Depends(get_database)):
    budget_service = BudgetService()
    return budget_service.create(database, client.dict())


@router.get("/", response_model=list[Budget])
def get_clients(database: Session = Depends(get_database)):
    budget_service = BudgetService()
    return budget_service.get_all(database)
