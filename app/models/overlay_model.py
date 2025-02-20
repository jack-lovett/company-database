from typing import Optional, List

from sqlalchemy.orm import Mapped
from sqlmodel import SQLModel, Field, Relationship
from app.models.site_overlay_model import SiteOverlay


class OverlayBase(SQLModel):
    name: Optional[str] = Field(default=None, max_length=45)


class Overlay(OverlayBase, table=True):
    __tablename__ = "overlay"

    id: Optional[int] = Field(default=None, primary_key=True)

    # Relationship
    sites: List["Site"] = Relationship(
        back_populates="overlays",
        link_model=SiteOverlay
    )

    def __str__(self) -> str:
        return self.name


class OverlayCreate(OverlayBase):
    pass


class OverlayUpdate(OverlayBase):
    pass
