from typing import Optional

from pydantic import BaseModel


class SiteBase(BaseModel):
    address_id: int
    local_authority_id: int
    wind_class_id: int
    soil_class_id: int
    lot_number: Optional[int] = None
    plan_number: Optional[str] = None
    heritage_status: Optional[bool] = None
    zone: Optional[str] = None
    precinct: Optional[str] = None
    area: Optional[str] = None


class SiteCreate(SiteBase):
    pass


class SiteUpdate(SiteBase):
    pass


class Site(SiteBase):
    id: int

    class Config:
        from_attributes = True
