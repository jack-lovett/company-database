
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.client import Client, ClientCreate, ClientUpdate
from services.client import ClientService
from database import get_database

client_router = APIRouter()

client_service = ClientService()

@client_router.post("/", response_model=Client)
def create_client(obj: ClientCreate, database: Session = Depends(get_database)):
    return client_service.create(database, obj)

@client_router.get("/client_id", response_model=Client)
def get_client(client_id: int, database: Session = Depends(get_database)):
    return client_service.get_by_id(database, client_id)

@client_router.put("/client_id", response_model=Client)
def update_client(client_id: int, obj: ClientUpdate, database: Session = Depends(get_database)):
    return client_service.update(database, client_id, obj)

@client_router.delete("/client_id", response_model=Client)
def delete_client(client_id: int, database: Session = Depends(get_database)):
    return client_service.delete(database, client_id)

@client_router.get("/", response_model=List[Client])
def get_clients(database: Session = Depends(get_database)):
    return client_service.get_all(database)
