from pydantic import BaseModel
from enum import Enum
from typing import Optional


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
    staff_role: StaffRoleEnum
    staff_employment_status: EmploymentStatusEnum
    staff_hire_date: str
    staff_notes: Optional[str] = None


class StaffCreate(StaffBase):
    pass


class StaffUpdate(StaffBase):
    staff_role: Optional[StaffRoleEnum] = None
    staff_employment_status: Optional[EmploymentStatusEnum] = None
    staff_hire_date: Optional[str] = None
    staff_notes: Optional[str] = None


class Staff(StaffBase):
    staff_id: int

    class Config:
        from_attributes = True
