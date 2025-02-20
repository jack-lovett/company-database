from datetime import date
from enum import Enum
from typing import Optional, List

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship

from app.models.staff_project_model import StaffProject


class StaffRole(str, Enum):
    secretary = "secretary"
    director = "director"
    building_designer = "building_designer"
    draftsperson = "draftsperson"
    junior_draftsperson = "junior_draftsperson"


class EmploymentStatus(str, Enum):
    full_time = "full_time"
    part_time = "part_time"
    casual = "casual"
    not_employed = "not_employed"


class StaffBase(SQLModel):
    contact_id: int = Field(foreign_key="contact.id")
    role: StaffRole
    employment_status: EmploymentStatus
    hire_date: date
    notes: Optional[str] = Field(default=None)


class Staff(StaffBase, table=True):
    __tablename__ = "staff"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    contact: "Contact" = Relationship(back_populates="staff")
    projects: List["Project"] = Relationship(
        back_populates="staff",
        link_model=StaffProject
    )
    staff_times: List["StaffTime"] = Relationship(back_populates="staff")
    call_logs: List["CallLog"] = Relationship(back_populates="staff")


class StaffCreate(StaffBase):
    pass


class StaffUpdate(StaffBase):
    role: Optional[StaffRole] = None
    employment_status: Optional[EmploymentStatus] = None
    hire_date: Optional[date] = None


class StaffDisplay(StaffBase):
    id: int
