from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.client_schema import Client, ClientCreate, ClientDisplay
from app.services.client_service import ClientService

router = APIRouter(prefix="/clients", tags=["clients"])


@router.post("/", response_model=Client)
def create_client(client: ClientCreate, db: Session = Depends(get_database)):
    client_service = ClientService()
    return client_service.create(db, client.dict())


@router.get("/", response_model=list[ClientDisplay])
def get_clients(database: Session = Depends(get_database)):
    client_service = ClientService()
    return client_service.get_enriched_clients(database)
