from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


# Enum for Call Log Type and Status
class CallLogTypeEnum(str, Enum):
    lead = "lead"
    information_request = "information_request"


class CallLogStatusEnum(str, Enum):
    follow_up = "follow_up"
    resolved = "resolved"
    in_progress = "in_progress"


class CallLogBase(BaseModel):
    client_id: int
    staff_id: int
    project_id: Optional[int] = None
    type: CallLogTypeEnum
    status: CallLogStatusEnum
    datetime: Optional[datetime] = None
    description: Optional[str] = None


class CallLogCreate(CallLogBase):
    pass


class CallLogUpdate(CallLogBase):
    client_id: Optional[int] = None
    staff_id: Optional[int] = None
    type: Optional[CallLogTypeEnum] = None
    status: Optional[CallLogStatusEnum] = None


class CallLog(CallLogBase):
    id: int

    class Config:
        from_attributes = True
