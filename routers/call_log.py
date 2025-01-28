
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from schemas.call_log import CallLog, CallLogCreate, CallLogUpdate
from services.call_log import CallLogService
from database import get_database

call_log_router = APIRouter()

call_log_service = CallLogService()

@call_log_router.post("/", response_model=CallLog)
def create_call_log(obj: CallLogCreate, database: Session = Depends(get_database)):
    return call_log_service.create(database, obj)

@call_log_router.get("/call_log_id", response_model=CallLog)
def get_call_log(call_log_id: int, database: Session = Depends(get_database)):
    return call_log_service.get_by_id(database, call_log_id)

@call_log_router.put("/call_log_id", response_model=CallLog)
def update_call_log(call_log_id: int, obj: CallLogUpdate, database: Session = Depends(get_database)):
    return call_log_service.update(database, call_log_id, obj)

@call_log_router.delete("/call_log_id", response_model=CallLog)
def delete_call_log(call_log_id: int, database: Session = Depends(get_database)):
    return call_log_service.delete(database, call_log_id)

@call_log_router.get("/", response_model=List[CallLog])
def get_call_logs(database: Session = Depends(get_database)):
    return call_log_service.get_all(database)
