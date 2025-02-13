from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class StaffRoleEnum(str, Enum):
    secretary = "secretary"
    director = "director"
    building_designer = "building_designer"
    draftsperson = "draftsperson"
    junior_draftsperson = "junior_draftsperson"


class EmploymentStatusEnum(str, Enum):
    full_time = "full_time"
    part_time = "part_time"
    casual = "casual"
    not_employed = "not_employed"


class StaffBase(BaseModel):
    contact_id: int
    role: StaffRoleEnum
    employment_status: EmploymentStatusEnum
    hire_date: date
    notes: Optional[str] = None


class StaffCreate(StaffBase):
    pass


class StaffUpdate(StaffBase):
    role: Optional[StaffRoleEnum] = None
    employment_status: Optional[EmploymentStatusEnum] = None
    hire_date: Optional[date] = None


class Staff(StaffBase):
    id: int

    class Config:
        from_attributes = True
