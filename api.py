import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from app.core.database import get_database
from app.models import Address, Budget, BuildingClass, CallLog, Client, Contact, Contractor, ContractorType, \
    LocalAuthority, Overlay, Note, ProjectHasContractor, ProjectIsBuildingClass, SiteOverlay, SoilClass, Staff, \
    StaffProject, StaffTime, WindClass, Site, Project, AddressDisplay
# from app.schemas.table_config import get_table_configs

from app.routers.generic_router import CRUDRouter
from app.services.address_service import AddressService
from app.services.project_service import ProjectService
from app.services.table_config import get_table_configs
from app.ui.templates.modals.modal_generator import ModalGenerator

app = FastAPI()


for model in [
    Address,
    Budget,
    BuildingClass,
    CallLog,
    Client,
    Contact,
    Contractor,
    ContractorType,
    LocalAuthority,
    Note,
    Overlay,
    ProjectHasContractor,
    ProjectIsBuildingClass,
    Project,
    Site,
    SiteOverlay,
    SoilClass,
    Staff,
    StaffProject,
    StaffTime,
    WindClass
]:
    router = CRUDRouter(model).get_router()
    app.include_router(router)

origins = [
    "http://localhost:5000",
    "http://192.168.15.15:5000",
    "http://localhost:8080",
    "http://192.168.15.15:8080",
    "https://localhost:5000",
    "https://192.168.15.15:5000",
    "https://localhost:8080",
    "https://192.168.15.15:8080"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def main():
    return {"message": "Welcome to Drawing Works API"}


@app.get("/table-config")
async def get_table_configuration():
    return get_table_configs()


@app.post("/import", response_model=list[Address])
def import_addresses(addresses: list[str], database: Session = Depends(get_database)):
    address_service = AddressService()
    return address_service.batch_import_addresses(database, addresses)


@app.get("/modal-configs")
def get_modal_configs():
    schemas = [
        Address, Client, Contact, Project, Site,
        LocalAuthority, WindClass, SoilClass, Overlay
    ]
    return [ModalGenerator.generate_modal_config(schema) for schema in schemas]


@app.get("/next-number")
def get_next_project_number(database: Session = Depends(get_database)):
    service = ProjectService()
    next_number = service.generate_project_number(database)
    return {"project_number": next_number}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
