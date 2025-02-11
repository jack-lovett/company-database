from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.contact import Contact, ContactCreate, ContactDisplay
from services.contact import ContactService

router = APIRouter(prefix="/contacts", tags=["contacts"])


@router.post("/", response_model=Contact)
def create_contact(contact: ContactCreate, database: Session = Depends(get_database)):
    contact_service = ContactService()
    return contact_service.create(database, contact.dict())


@router.get("/", response_model=list[ContactDisplay])
def get_contacts(database: Session = Depends(get_database)):
    contact_service = ContactService()
    return contact_service.get_enriched_contacts(database)
