from sqlmodel import SQLModel, Field


class SiteOverlay(SQLModel, table=True):
    __tablename__ = 'site_overlay'

    overlay_id: int = Field(
        foreign_key="overlay.id",
        primary_key=True
    )
    site_id: int = Field(
        foreign_key="site.id",
        primary_key=True
    )


class SiteOverlayDisplay(SiteOverlay):
    pass
