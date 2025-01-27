from typing import Optional

from pydantic import BaseModel


class StaffTimeBase(BaseModel):
    staff_id: int
    project_id: Optional[int]
    staff_time_description: Optional[str] = None
    staff_time_hours: int


class StaffTimeCreate(StaffTimeBase):
    pass


class StaffTimeUpdate(StaffTimeBase):
    staff_time_description: Optional[str] = None
    staff_time_hours: Optional[int] = None


class StaffTime(StaffTimeBase):
    staff_time_id: int

    class Config:
        orm_mode = True
