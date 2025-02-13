from typing import Optional

from pydantic import BaseModel


class OverlayBase(BaseModel):
    name: Optional[str] = None


class OverlayCreate(OverlayBase):
    pass


class OverlayUpdate(OverlayBase):
    pass


class Overlay(OverlayBase):
    id: int

    class Config:
        from_attributes = True
