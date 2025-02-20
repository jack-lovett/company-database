import datetime
from enum import Enum
from typing import Optional

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship


class CallLogType(str, Enum):
    lead = "lead"
    information_request = "information_request"


class CallLogStatus(str, Enum):
    follow_up = "follow_up"
    resolved = "resolved"
    in_progress = "in_progress"


class CallLogBase(SQLModel):
    client_id: int = Field(foreign_key="client.id")
    staff_id: int = Field(foreign_key="staff.id")
    project_id: Optional[int] = Field(default=None, foreign_key="project.id")
    type: CallLogType = Field(sa_column_kwargs={"name": "type"})
    status: CallLogStatus
    datetime_: datetime.datetime = Field(default_factory=lambda: datetime.datetime.now(datetime.UTC))
    description: Optional[str] = Field(default=None, max_length=255)


class CallLog(CallLogBase, table=True):
    __tablename__ = "call_log"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    client: "Client" = Relationship(back_populates="call_logs")
    staff: "Staff" = Relationship(back_populates="call_logs")
    project: Optional["Project"] = Relationship(back_populates="call_logs")


class CallLogCreate(CallLogBase):
    pass


class CallLogUpdate(SQLModel):
    client_id: Optional[int] = None
    staff_id: Optional[int] = None
    type: Optional[CallLogType] = None
    status: Optional[CallLogStatus] = None
    description: Optional[str] = None

class CallLogDisplay(CallLogBase):
    id: int