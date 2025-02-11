from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.contact_schema import Contact, ContactCreate, ContactDisplay
from app.services.contact_service import ContactService

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.post("/", response_model=Contact)
def create_contact(contact: ContactCreate, database: Session = Depends(get_database)):
    contact_service = ContactService()
    return contact_service.create(database, contact.dict())


@router.get("/", response_model=list[ContactDisplay])
def get_contacts(database: Session = Depends(get_database)):
    contact_service = ContactService()
    return contact_service.get_enriched_contacts(database)
