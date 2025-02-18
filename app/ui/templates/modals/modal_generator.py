import inspect
from datetime import date
from typing import Type, Dict, Any, Optional, get_origin, get_args

from pydantic import BaseModel


class ModalFieldConfig:
    def __init__(self, field_type: str, required: bool, label: str,
                 related_model: Optional[str] = None,
                 create_button: bool = False):
        self.field_type = field_type
        self.required = required
        self.label = label
        self.related_model = related_model
        self.create_button = create_button


class ModalGenerator:
    @staticmethod
    def get_field_config(field_name: str, field_type: Any, is_required: bool) -> ModalFieldConfig:
        # Handle foreign key fields
        if field_name.endswith('_id') and field_name != 'id':
            related_model = field_name.replace('_id', '').title()
            return ModalFieldConfig(
                field_type="select",
                required=is_required,
                label=related_model.replace('_', ' ').title(),
                related_model=related_model,
                create_button=True
            )

        # Handle basic types
        if field_type == int:
            return ModalFieldConfig("number", is_required,
                                    field_name.replace('_', ' ').title())
        elif field_type == str:
            if field_name in ['email', 'accounts_email']:
                return ModalFieldConfig("email", is_required,
                                        field_name.replace('_', ' ').title())
            elif field_name in ['website']:
                return ModalFieldConfig("url", is_required,
                                        field_name.replace('_', ' ').title())
            elif field_name in ['description']:
                return ModalFieldConfig("textarea", is_required,
                                        field_name.replace('_', ' ').title())
            return ModalFieldConfig("text", is_required,
                                    field_name.replace('_', ' ').title())
        elif field_type == bool:
            return ModalFieldConfig("checkbox", is_required,
                                    field_name.replace('_', ' ').title())
        elif field_type == date:
            return ModalFieldConfig("date", is_required,
                                    field_name.replace('_', ' ').title())

        # Handle Optional types
        origin = get_origin(field_type)
        if origin is Optional:
            args = get_args(field_type)
            return ModalGenerator.get_field_config(field_name, args[0], False)

        return ModalFieldConfig("text", is_required,
                                field_name.replace('_', ' ').title())

    @staticmethod
    def generate_modal_config(schema: Type[BaseModel]) -> Dict[str, Any]:
        # Get the Create schema if it exists
        create_schema = None
        for name, obj in inspect.getmembers(inspect.getmodule(schema)):
            if name == f"{schema.__name__}Create":
                create_schema = obj
                break

        if not create_schema:
            create_schema = schema

        fields = {}
        for name, field in create_schema.__annotations__.items():
            if name != 'id' and not name.endswith('_datetime'):
                is_required = True
                if hasattr(create_schema, '__fields__'):
                    if name in create_schema.__fields__:
                        is_required = not create_schema.__fields__[name].allow_none

                field_config = ModalGenerator.get_field_config(name, field, is_required)
                fields[name] = {
                    "type": field_config.field_type,
                    "required": field_config.required,
                    "label": field_config.label,
                    "related_model": field_config.related_model,
                    "create_button": field_config.create_button
                }

        return {
            "name": schema.__name__,
            "title": f"Create New {schema.__name__}",
            "fields": fields
        }
