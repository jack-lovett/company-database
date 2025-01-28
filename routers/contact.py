
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.contact import Contact, ContactCreate, ContactUpdate
from services.contact import ContactService
from database import get_database

contact_router = APIRouter()

contact_service = ContactService()

@contact_router.post("/", response_model=Contact)
def create_contact(obj: ContactCreate, database: Session = Depends(get_database)):
    return contact_service.create(database, obj)

@contact_router.get("/contact_id", response_model=Contact)
def get_contact(contact_id: int, database: Session = Depends(get_database)):
    return contact_service.get_by_id(database, contact_id)

@contact_router.put("/contact_id", response_model=Contact)
def update_contact(contact_id: int, obj: ContactUpdate, database: Session = Depends(get_database)):
    return contact_service.update(database, contact_id, obj)

@contact_router.delete("/contact_id", response_model=Contact)
def delete_contact(contact_id: int, database: Session = Depends(get_database)):
    return contact_service.delete(database, contact_id)

@contact_router.get("/", response_model=List[Contact])
def get_contacts(database: Session = Depends(get_database)):
    return contact_service.get_all(database)
