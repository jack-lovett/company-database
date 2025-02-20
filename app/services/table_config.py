from typing import Dict, List

from app.models import AddressDisplay, ClientDisplay, ContactDisplay, ProjectDisplay, SiteDisplay


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
            for field_name in AddressDisplay.model_fields.keys()
        ],
        'clients': [
            create_column_config(field_name)
            for field_name in ClientDisplay.model_fields.keys()
        ],
        'contacts': [
            create_column_config(field_name)
            for field_name in ContactDisplay.model_fields.keys()
        ],
        'projects': [
            create_column_config(field_name)
            for field_name in ProjectDisplay.model_fields.keys()
        ],
        'sites': [
            create_column_config(field_name)
            for field_name in SiteDisplay.model_fields.keys()
        ]
    }
