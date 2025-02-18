from fastapi import APIRouter

from app.schemas import (
    Address, Client, Contact, Project, Site,
    LocalAuthority, WindClass, SoilClass, Overlay
)
from app.ui.templates.modals.modal_generator import ModalGenerator

router = APIRouter()


@router.get("/modal-configs")
def get_modal_configs():
    schemas = [
        Address, Client, Contact, Project, Site,
        LocalAuthority, WindClass, SoilClass, Overlay
    ]
    return [ModalGenerator.generate_modal_config(schema) for schema in schemas]
