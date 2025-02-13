from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class AddressDisplay(BaseModel):
    full_address: str


class LocalAuthorityDisplay(BaseModel):
    name: str


class WindClassDisplay(BaseModel):
    class_: str


class SoilClassDisplay(BaseModel):
    class_: str


class SiteDisplay(BaseModel):
    address: AddressDisplay
    local_authority: LocalAuthorityDisplay
    wind_class: WindClassDisplay
    soil_class: SoilClassDisplay


class ProjectBase(BaseModel):
    client_id: int
    site_id: int
    status: str
    description: Optional[str] = None
    initial_inquiry_date: date
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    storeys: Optional[int] = None
    referral_source: Optional[str] = None
    payment_basis: Optional[str] = None


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    number: int
    creation_datetime: datetime

    class Config:
        from_attributes = True


class ProjectDisplay(BaseModel):
    id: int
    number: int
    client_name: str
    site: SiteDisplay
    status: str
    description: Optional[str]
    initial_inquiry_date: date
    start_date: Optional[date]
    end_date: Optional[date]
    storeys: Optional[int]
    referral_source: Optional[str]
    payment_basis: Optional[str]
    creation_datetime: datetime

    class Config:
        from_attributes = True
