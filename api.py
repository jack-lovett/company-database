from fastapi import FastAPI

from routers.address import address_router
from routers.budget import budget_router
from routers.building_class import building_class_router
from routers.call_log import call_log_router
from routers.client import client_router
from routers.contact import contact_router
from routers.contractor import contractor_router
from routers.contractor_type import contractor_type_router
from routers.note import note_router
from routers.project import project_router
from routers.project_has_contractor import project_has_contractor_router
from routers.project_is_building_class import project_is_building_class_router
from routers.staff import staff_router
from routers.staff_project import staff_project_router
from routers.staff_time import staff_time_router

app = FastAPI()

# Include the routers
app.include_router(address_router, prefix="/addresses", tags=["addresses"])
app.include_router(budget_router, prefix="/budgets", tags=["budgets"])
app.include_router(building_class_router, prefix="/building_classes", tags=["building_classes"])
app.include_router(call_log_router, prefix="/call_logs", tags=["call_logs"])
app.include_router(client_router, prefix="/clients", tags=["clients"])
app.include_router(contact_router, prefix="/contacts", tags=["contacts"])
app.include_router(contractor_router, prefix="/contractors", tags=["contractors"])
app.include_router(contractor_type_router, prefix="/contractor_types", tags=["contractor_types"])
app.include_router(note_router, prefix="/notes", tags=["notes"])
app.include_router(project_router, prefix="/projects", tags=["projects"])
app.include_router(project_has_contractor_router, prefix="/projects_has_contractors", tags=["projects_has_contractors"])
app.include_router(project_is_building_class_router, prefix="/projects_is_building_classes",
                   tags=["projects_is_building_classes"])
app.include_router(staff_router, prefix="/staff", tags=["staff"])
app.include_router(staff_project_router, prefix="/staff_projects", tags=["staff_projects"])
app.include_router(staff_time_router, prefix="/staff_times", tags=["staff_times"])


@app.get("/")
def read_root():
    return "Welcome to the Drawing Works backend database API"


@app.get("/test")
def read_test():
    return "This is a test endpoint!"