from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel


class ProjectStatusEnum(str, Enum):
    lead = "lead"
    job = "job"
    completed = "completed"
    no_sale = "no_sale"


class ReferralSourceEnum(str, Enum):
    google = "google"
    referral = "referral"
    repeat_client = "repeat_client"
    jkc = "jkc"
    smce = "smce"
    word_of_mouth = "word_of_mouth"
    website = "website"


class PaymentBasisEnum(str, Enum):
    lump_sum = "lump_sum"
    hourly_rate = "hourly_rate"


class ProjectBase(BaseModel):
    client_id: int
    address_id: int
    status: ProjectStatusEnum
    description: Optional[str] = None
    initial_inquiry_date: date
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    storeys: Optional[int] = None
    referral_source: Optional[ReferralSourceEnum] = None
    payment_basis: Optional[PaymentBasisEnum] = None


class ProjectCreate(ProjectBase):
    number: int


class ProjectUpdate(ProjectBase):
    client_id: Optional[int] = None
    address_id: Optional[int] = None
    status: Optional[ProjectStatusEnum] = None
    initial_inquiry_date: Optional[date] = None


class Project(ProjectBase):
    id: int
    creation_datetime: datetime

    class Config:
        from_attributes = True


class ProjectDisplay(BaseModel):
    number: int
    full_address: str
    client_name: str
    status: ProjectStatusEnum
    description: Optional[str] = None
    initial_inquiry_date: date
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    storeys: Optional[int] = None
    referral_source: Optional[ReferralSourceEnum] = None
    payment_basis: Optional[PaymentBasisEnum] = None
    creation_datetime: datetime
