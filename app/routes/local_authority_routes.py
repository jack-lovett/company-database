from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.local_authority_schema import LocalAuthority, LocalAuthorityCreate
from app.services.local_authority_service import LocalAuthorityService

router = APIRouter(prefix="/local-authorities", tags=["local-authorities"])


@router.post("/", response_model=LocalAuthority)
def create_local_authority(local_authority: LocalAuthorityCreate, database: Session = Depends(get_database)):
    service = LocalAuthorityService()
    return service.create(database, local_authority.dict())


@router.get("/", response_model=list[LocalAuthority])
def get_local_authorities(database: Session = Depends(get_database)):
    service = LocalAuthorityService()
    return service.get_all(database)
