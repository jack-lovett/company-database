from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.budget import Budget, BudgetCreate, BudgetUpdate
from services.budget import BudgetService

budget_router = APIRouter()

budget_service = BudgetService()


@budget_router.post("/", response_model=Budget)
def create_budget(obj: BudgetCreate, database: Session = Depends(get_database)):
    return budget_service.create(database, obj)


@budget_router.get("/budget_id", response_model=Budget)
def get_budget(budget_id: int, database: Session = Depends(get_database)):
    return budget_service.get_by_id(database, budget_id)


@budget_router.put("/budget_id", response_model=Budget)
def update_budget(budget_id: int, obj: BudgetUpdate, database: Session = Depends(get_database)):
    return budget_service.update(database, budget_id, obj)


@budget_router.delete("/budget_id", response_model=Budget)
def delete_budget(budget_id: int, database: Session = Depends(get_database)):
    return budget_service.delete(database, budget_id)


@budget_router.get("/", response_model=List[Budget])
def get_budgets(database: Session = Depends(get_database)):
    return budget_service.get_all(database)
