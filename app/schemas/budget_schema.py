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
    type: BudgetTypeEnum
    status: BudgetStatusEnum
    description: Optional[str] = None
    estimate: Optional[Decimal] = None
    actual: Optional[Decimal] = None


class BudgetCreate(BudgetBase):
    project_id: int  # Adding required field for creation


class BudgetUpdate(BudgetBase):
    type: Optional[BudgetTypeEnum] = None
    status: Optional[BudgetStatusEnum] = None
    estimate: Optional[str] = None
    actual: Optional[str] = None


class Budget(BudgetBase):
    id: int
    project_id: int

    class Config:
        from_attributes = True
