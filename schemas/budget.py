from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel


# Enum for Budget Type and Status
class BudgetTypeEnum(str, Enum):
    asset = "asset"
    liability = "liability"


class BudgetStatusEnum(str, Enum):
    not_invoiced = "not_invoiced"
    invoiced = "invoiced"
    paid = "paid"
    partially_invoiced = "partially_invoiced"


class BudgetBase(BaseModel):
    budget_type: BudgetTypeEnum
    budget_status: BudgetStatusEnum
    budget_description: Optional[str] = None
    budget_estimate: Optional[Decimal] = None
    budget_actual: Optional[Decimal] = None


class BudgetCreate(BudgetBase):
    project_id: int  # Adding required field for creation


class BudgetUpdate(BudgetBase):
    budget_type: Optional[BudgetTypeEnum] = None
    budget_status: Optional[BudgetStatusEnum] = None
    budget_description: Optional[str] = None
    budget_estimate: Optional[str] = None
    budget_actual: Optional[str] = None


class Budget(BudgetBase):
    budget_id: int
    project_id: int

    class Config:
        from_attributes = True
