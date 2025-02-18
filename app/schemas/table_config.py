from typing import Dict, List

from .address_schema import AddressDisplay
from .client_schema import ClientDisplay
from .contact_schema import ContactDisplay
from .project_schema import ProjectDisplay
from .site_schema import SiteDisplay


def get_table_configs() -> Dict[str, List[Dict]]:
    def create_column_config(field_name: str) -> Dict:
        return {
            'data': field_name,
            'render': lambda data, type, row: (
                str(data) if isinstance(data, (str, int, float, bool))
                else data.__repr__() if hasattr(data, '__repr__')
                else str(data)
            )
        }

    return {
        'addresses': [
            create_column_config(field_name)
            for field_name in AddressDisplay.__fields__.keys()
        ],
        'clients': [
            create_column_config(field_name)
            for field_name in ClientDisplay.__fields__.keys()
        ],
        'contacts': [
            create_column_config(field_name)
            for field_name in ContactDisplay.__fields__.keys()
        ],
        'projects': [
            create_column_config(field_name)
            for field_name in ProjectDisplay.__fields__.keys()
        ],
        'sites': [
            create_column_config(field_name)
            for field_name in SiteDisplay.__fields__.keys()
        ]
    }
