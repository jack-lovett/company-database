from pydantic import BaseModel
from enum import Enum
from datetime import date, datetime
from typing import Optional

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

class Project(BaseModel):
    project_id: int
    client_id: int
    address_id: int
    project_status: ProjectStatusEnum
    project_description: Optional[str] = None
    project_initial_inquiry_date: Optional[date] = None
    project_start_date: Optional[date] = None
    project_end_date: Optional[date] = None
    project_storeys: Optional[int] = None
    project_referral_source: Optional[ReferralSourceEnum] = None
    project_payment_basis: Optional[PaymentBasisEnum] = None
    project_creation_datetime: datetime

    class Config:
        orm_mode = True
