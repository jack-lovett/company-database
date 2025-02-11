import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import (
    building_class_routes
)

app = FastAPI()

# Include all routers
app.include_router(project.router)
app.include_router(client.router)
app.include_router(contact.router)
app.include_router(address.router)
app.include_router(budget.router)
app.include_router(building_class_routes.router)
app.include_router(call_log.router)
app.include_router(contractor.router)
app.include_router(contractor_type.router)
app.include_router(note.router)
app.include_router(project_has_contractor.router)
app.include_router(project_is_building_class.router)
app.include_router(staff.router)
app.include_router(staff_project.router)
app.include_router(staff_time.router)

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


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
