from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_database
from schemas.call_log import CallLog, CallLogCreate
from services.call_log import CallLogService

router = APIRouter(prefix="/call_logs", tags=["call_logs"])


@router.post("/", response_model=CallLog)
def create_call_log(call_log: CallLogCreate, database: Session = Depends(get_database)):
    call_log_service = CallLogService()
    return call_log_service.create(database, call_log.dict())


@router.get("/", response_model=list[CallLog])
def get_call_logs(database: Session = Depends(get_database)):
    call_log_service = CallLogService()
    return call_log_service.get_all(database)
