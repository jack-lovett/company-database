from app.crud.site_crud import CRUDSite
from app.models import LocalAuthority, WindClass, SoilClass
from app.services.address_service import AddressService
from app.services.base_service import BaseService


class SiteService(BaseService):
    def __init__(self):
        super().__init__(CRUDSite())

    def enrich_site(self, database, site):
        """Convert foreign keys into meaningful values for display."""
        site_dict = site.__dict__.copy()

        # Enrich address details
        address_service = AddressService()
        address = address_service.get_by_id(database, site.address_id)
        if address:
            site_dict['address'] = {
                'full_address': f"{address.street}, {address.suburb}, {address.city}, {address.state} {address.postal_code}"
            }

        # Get related models
        local_authority = database.query(LocalAuthority).get(site.local_authority_id)
        wind_class = database.query(WindClass).get(site.wind_class_id)
        soil_class = database.query(SoilClass).get(site.soil_class_id)

        # Add related data
        site_dict['local_authority'] = {'name': local_authority.name} if local_authority else None
        site_dict['wind_class'] = {'class_': wind_class.class_} if wind_class else None
        site_dict['soil_class'] = {'class_': soil_class.class_} if soil_class else None

        # Format overlays as a list of names
        site_dict['overlays'] = [overlay.name for overlay in site.overlays] if site.overlays else []

        return site_dict
