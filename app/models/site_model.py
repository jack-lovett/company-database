from typing import Optional, List

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship

from app.models.site_overlay_model import SiteOverlay


class SiteBase(SQLModel):
    address_id: int = Field(foreign_key="address.id")
    local_authority_id: int = Field(foreign_key="local_authority.id")
    wind_class_id: int = Field(foreign_key="wind_class.id")
    soil_class_id: int = Field(foreign_key="soil_class.id")
    lot_number: Optional[int] = None
    plan_number: Optional[str] = Field(default=None, max_length=15)
    heritage_status: Optional[bool] = None
    zone: Optional[str] = Field(default=None, max_length=45)
    precinct: Optional[str] = Field(default=None, max_length=45)
    area: Optional[str] = Field(default=None, max_length=45)


class Site(SiteBase, table=True):
    __tablename__ = "site"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationships
    address: "Address" = Relationship(back_populates="sites")
    local_authority: "LocalAuthority" = Relationship(back_populates="sites")
    wind_class: "WindClass" = Relationship(back_populates="sites")
    soil_class: "SoilClass" = Relationship(back_populates="sites")
    overlays: List["Overlay"] = Relationship(
        back_populates="sites",
        link_model=SiteOverlay
    )
    projects: List["Project"] = Relationship(back_populates="site")

    def __repr__(self) -> str:
        return f"Site {self.id}: {self.address.street}, {self.address.suburb}, {self.address.city}, {self.address.state} {self.address.postal_code}"


class SiteCreate(SiteBase):
    pass


class SiteUpdate(SiteBase):
    pass


class SiteDisplay(SQLModel):
    id: int
    address: str
    local_authority: str
    wind_class: str
    soil_class: str
    lot_number: Optional[int] = None
    plan_number: Optional[str] = None
    heritage_status: Optional[bool] = None
    zone: Optional[str] = None
    precinct: Optional[str] = None
    area: Optional[str] = None
    overlays: Optional[List[str]] = None
