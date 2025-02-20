from decimal import Decimal
from enum import Enum
from typing import Optional

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship
from app.models.project_model import Project


class BudgetType(str, Enum):
    asset = "asset"
    liability = "liability"


class BudgetStatus(str, Enum):
    not_invoiced = "not_invoiced"
    invoiced = "invoiced"
    paid = "paid"
    partially_invoiced = "partially_invoiced"


class BudgetBase(SQLModel):
    type: BudgetType
    status: BudgetStatus = Field(default=BudgetStatus.not_invoiced)
    description: Optional[str] = Field(default=None, max_length=255)
    estimate: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=2)
    actual: Optional[Decimal] = Field(default=None, max_digits=10, decimal_places=2)


class Budget(BudgetBase, table=True):
    __tablename__ = "budget"

    id: Optional[int] = Field(default=None, primary_key=True)
    project_id: int = Field(foreign_key="project.id")

    # Relationship
    project: "Project" = Relationship(back_populates="budgets")


class BudgetCreate(BudgetBase):
    project_id: int


class BudgetUpdate(SQLModel):
    type: Optional[BudgetType] = None
    status: Optional[BudgetStatus] = None
    description: Optional[str] = None
    estimate: Optional[Decimal] = None
    actual: Optional[Decimal] = None
