from typing import Optional

from pydantic import BaseModel


class StaffTimeBase(BaseModel):
    staff_id: int
    project_id: Optional[int]
    description: Optional[str] = None
    hours: int


class StaffTimeCreate(StaffTimeBase):
    pass


class StaffTimeUpdate(StaffTimeBase):
    description: Optional[str] = None
    hours: Optional[int] = None


class StaffTime(StaffTimeBase):
    id: int

    class Config:
        from_attributes = True
