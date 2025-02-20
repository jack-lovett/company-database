from typing import Optional

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship


class StaffTimeBase(SQLModel):
    staff_id: int = Field(foreign_key="staff.id")
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    description: Optional[str] = Field(default=None, max_length=255)
    hours: int


class StaffTime(StaffTimeBase, table=True):
    __tablename__ = "staff_time"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    staff: "Staff" = Relationship(back_populates="staff_times")
    project: Optional["Project"] = Relationship(back_populates="staff_times")


class StaffTimeCreate(StaffTimeBase):
    pass


class StaffTimeUpdate(SQLModel):
    description: Optional[str] = None
    hours: Optional[int] = None
