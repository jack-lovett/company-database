import inspect
import logging
from datetime import date
from enum import Enum
from typing import Any, Optional, Union, get_args

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ModalFieldConfig:
    def __init__(self, field_type: str, required: bool, label: str,
                 related_model: Optional[str] = None,
                 create_button: bool = False,
                 enum_values: Optional[list] = None,
                 min_value: Optional[int] = None,
                 max_value: Optional[int] = None,
                 placeholder: Optional[str] = None):
        self.field_type = field_type
        self.required = required
        self.label = label
        self.related_model = related_model
        self.create_button = create_button
        self.enum_values = enum_values
        self.min_value = min_value
        self.max_value = max_value
        self.placeholder = placeholder


class ModalGenerator:
    @staticmethod
    def get_field_config(field_name: str, field_type: Any, is_required: bool) -> ModalFieldConfig:
        # Handle enum types
        if hasattr(field_type, '__origin__') and field_type.__origin__ is Union:
            field_type = get_args(field_type)[0]

        if isinstance(field_type, type) and issubclass(field_type, Enum):
            return ModalFieldConfig(
                field_type="select",
                required=is_required,
                label=field_name.replace('_', ' ').title(),
                enum_values=[e.value for e in field_type]
            )

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

        # Handle date fields
        if field_type == date or str(field_type).endswith('date'):
            return ModalFieldConfig("date", is_required,
                                    field_name.replace('_', ' ').title())

        # Handle other basic types
        if field_type == str:
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
        elif field_type == int:
            return ModalFieldConfig("number", is_required,
                                    field_name.replace('_', ' ').title())
        elif field_type == bool:
            return ModalFieldConfig("checkbox", is_required,
                                    field_name.replace('_', ' ').title())

        return ModalFieldConfig("text", is_required,
                                field_name.replace('_', ' ').title())

    import logging
    from typing import Type, Dict, Any
    from pydantic import BaseModel

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    @staticmethod
    def generate_modal_config(schema: Type[BaseModel]) -> Dict[str, Any]:
        logger.info(f"Generating modal config for schema: {schema.__name__}")

        # Get base model and create schema
        base_model = None
        create_schema = None
        for name, obj in inspect.getmembers(inspect.getmodule(schema)):
            if name == f"{schema.__name__}Base":
                base_model = obj
            elif name == f"{schema.__name__}Create":
                create_schema = obj

        if not create_schema:
            create_schema = schema

        fields = {}
        base_fields = base_model.model_fields if hasattr(base_model, 'model_fields') else base_model.__fields__
        model_fields = create_schema.model_fields if hasattr(create_schema,
                                                             'model_fields') else create_schema.__fields__

        for name, field in model_fields.items():
            if name != 'id' and not name.endswith('_datetime'):
                field_type = field.annotation if hasattr(field, 'annotation') else field.type_

                # Use the required property from the base field if available
                base_field = base_fields.get(name)
                is_required = base_field.is_required if base_field is not None else True

                logger.debug(f"Processing field: {name}, type: {field_type}, required: {is_required}")

                field_config = ModalGenerator.get_field_config(name, field_type, is_required)
                fields[name] = {
                    "type": field_config.field_type,
                    "required": bool(is_required),
                    "label": field_config.label,
                    "related_model": field_config.related_model,
                    "create_button": field_config.create_button,
                    "enum_values": field_config.enum_values
                }

        return {
            "name": schema.__name__,
            "title": f"Create New {schema.__name__}",
            "fields": fields
        }
