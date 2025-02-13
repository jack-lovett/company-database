from sqlalchemy.orm import class_mapper

from app.models import Client, Address


class GenericTableService:
    def __init__(self, database):
        self.db = database

    def get_table_columns(self, model):
        """Retrieve column names dynamically from the model."""
        return [column.name for column in class_mapper(model).columns]

    def get_foreign_keys(self, model):
        """Identify foreign keys for enrichment."""
        mapper = class_mapper(model)
        return {
            column.name: column.foreign_keys.pop().column.table.name
            for column in mapper.columns if column.foreign_keys
        }

    def enrich_record(self, model, record):
        """Enrich a single record by resolving foreign key values."""
        record_dict = record.__dict__.copy()
        foreign_keys = self.get_foreign_keys(model)

        for column, ref_table in foreign_keys.items():
            ref_model = self.get_model_by_table_name(ref_table)
            if ref_model:
                related_record = self.db.query(ref_model).get(getattr(record, column))
                if related_record:
                    # Check if the related record is a Client
                    if isinstance(related_record, Client):
                        record_dict[
                            column] = f"{related_record.primary_contact.first_name} {related_record.primary_contact.last_name}"
                    # Check if the related record is an Address
                    elif isinstance(related_record, Address):
                        record_dict[
                            column] = f"{related_record.street}, {related_record.city}, {related_record.state}"
                    else:
                        record_dict[column] = str(related_record)  # Default handling for other related models
                else:
                    record_dict[column] = "Unknown"

        return record_dict

    def get_enriched_data(self, model):
        """Retrieve all records with enriched values."""
        records = self.db.query(model).all()
        return [self.enrich_record(model, record) for record in records]

    def get_model_by_table_name(self, table_name):
        """Dynamically retrieve the model class by table name."""
        from app.models.base_model import Base
        for cls in Base.__subclasses__():
            if cls.__tablename__ == table_name:
                return cls
        return None

    def get_readable_value(self, record):
        """Return a user-friendly display name for a foreign key record."""
        if hasattr(record, "name"):
            return record.name  # Example: If the table has a `name` column
        elif hasattr(record, "first_name") and hasattr(record, "last_name"):
            return f"{record.first_name} {record.last_name}"
        return str(record)
