from typing import Optional

from pydantic import BaseModel


class LocalAuthorityBase(BaseModel):
    name: str
    website: Optional[str] = None


class LocalAuthorityCreate(LocalAuthorityBase):
    pass


class LocalAuthorityUpdate(LocalAuthorityBase):
    pass


class LocalAuthorityDisplay(BaseModel):
    id: int
    name: str
    website: Optional[str] = None


class LocalAuthority(LocalAuthorityBase):
    id: int

    class Config:
        from_attributes = True
