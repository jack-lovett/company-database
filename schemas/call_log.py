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
    call_log_type: CallLogTypeEnum
    call_log_status: CallLogStatusEnum
    call_log_datetime: Optional[datetime] = None
    call_log_description: Optional[str] = None


class CallLogCreate(CallLogBase):
    pass


class CallLogUpdate(CallLogBase):
    client_id: Optional[int] = None
    staff_id: Optional[int] = None
    call_log_type: Optional[CallLogTypeEnum] = None
    call_log_status: Optional[CallLogStatusEnum] = None


class CallLog(CallLogBase):
    call_log_id: int

    class Config:
        from_attributes = True
