from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.site_schema import Site, SiteCreate, SiteDisplay
from app.services.site_service import SiteService

router = APIRouter(prefix="/sites", tags=["sites"])


@router.post("/", response_model=Site)
def create_site(site: SiteCreate, database: Session = Depends(get_database)):
    service = SiteService()
    return service.create(database, site.dict())


@router.get("/", response_model=list[SiteDisplay])
def get_sites(database: Session = Depends(get_database)):
    service = SiteService()
    return service.get_enriched_sites(database)
