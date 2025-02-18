import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import (
    project_routes,
    client_routes,
    contact_routes,
    address_routes,
    budget_routes,
    building_class_routes,
    call_log_routes,
    contractor_routes,
    contractor_type_routes,
    note_routes,
    project_has_contractor_routes,
    project_is_building_class_routes,
    staff_routes,
    staff_project_routes,
    staff_time_routes,
    site_routes,
    wind_class_routes,
    soil_class_routes,
    local_authority_routes,
    overlay_routes
)
from app.schemas.table_config import get_table_configs

app = FastAPI()

# Add to routers list
routers = [
    project_routes,
    client_routes,
    contact_routes,
    address_routes,
    site_routes,
    wind_class_routes,
    soil_class_routes,
    local_authority_routes,
    budget_routes,
    building_class_routes,
    call_log_routes,
    contractor_routes,
    contractor_type_routes,
    note_routes,
    project_has_contractor_routes,
    project_is_building_class_routes,
    staff_routes,
    staff_project_routes,
    staff_time_routes,
    overlay_routes
]

for router in routers:
    app.include_router(router.router)

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


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
