from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.schemas.call_log_schema import CallLog, CallLogCreate
from app.services.call_log_service import CallLogService

router = APIRouter(prefix="/call_logs", tags=["call_logs"])


@router.post("/", response_model=CallLog)
def create_call_log(call_log: CallLogCreate, database: Session = Depends(get_database)):
    call_log_service = CallLogService()
    return call_log_service.create(database, call_log.dict())


@router.get("/", response_model=list[CallLog])
def get_call_logs(database: Session = Depends(get_database)):
    call_log_service = CallLogService()
    return call_log_service.get_all(database)
