from googlemaps import Client

from app.core.config import GOOGLE_MAPS_API_KEY
from app.crud.address_crud import CRUDAddress
from app.services.base_service import BaseService


class AddressService(BaseService):
    def __init__(self):
        super().__init__(CRUDAddress())
        self.gmaps = Client(key=GOOGLE_MAPS_API_KEY)

    def enrich_record(self, database, address):
        """Convert foreign keys into meaningful values for display."""
        address_dict = address.__dict__.copy()

        from app.services.contact_service import ContactService
        contact_service = ContactService()

        billing_contacts = [contact_service.get_by_id(database, contact.id) for contact in
                            address.contacts_as_billing]
        postal_contacts = [contact_service.get_by_id(database, contact.id) for contact in
                           address.contacts_as_postal]

        address_dict['billing_contacts'] = [f"{contact.first_name} {contact.last_name}" for contact in
                                            billing_contacts if contact]
        address_dict['postal_contacts'] = [f"{contact.first_name} {contact.last_name}" for contact in
                                           postal_contacts if contact]

        return address_dict

    def get_enriched_addresses(self, database):
        """Retrieve all addresses with enriched values."""
        addresses = self.get_all(database)
        return [self.enrich_address(database, address) for address in addresses]

    def process_import_address(self, address_text: str) -> dict:
        """Process a single address through Google Maps API."""
        geocode_result = self.gmaps.geocode(address_text, components={'country': 'AU'})

        if not geocode_result:
            return None

        result = geocode_result[0]
        components = result['address_components']

        address_data = {
            'address_street': '',
            'address_suburb': '',
            'address_city': '',
            'address_state': '',
            'address_postal_code': '',
            'address_country': 'Australia'
        }

        for component in components:
            if 'street_number' in component['types']:
                address_data['address_street'] = component['long_name']
            elif 'route' in component['types']:
                address_data['address_street'] += f" {component['long_name']}"
            elif 'locality' in component['types']:
                address_data['address_suburb'] = component['long_name']
                address_data['address_city'] = component['long_name']
            elif 'administrative_area_level_1' in component['types']:
                address_data['address_state'] = component['short_name']
            elif 'postal_code' in component['types']:
                address_data['address_postal_code'] = component['long_name']

        return address_data

    def batch_import_addresses(self, database, addresses: list[str]) -> list[dict]:
        """Process and import multiple addresses."""
        results = []
        for address_text in addresses:
            processed_data = self.process_import_address(address_text)
            if processed_data:
                created_address = self.create(database, processed_data)
                results.append(created_address)
            else:
                results.append(None)
        return results
