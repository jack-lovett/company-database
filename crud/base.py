from sqlalchemy.orm import Session


class CRUDBase:
    def __init__(self, model_class):
        self.model_class = model_class
        self.id_field_name = f"{model_class.__name__.lower()}_id"

    def get(self, database: Session, object_id: int):
        return database.query(self.model_class).filter(
            getattr(self.model_class, self.id_field_name) == object_id).first()

    def get_all(self, database: Session, skip: int = 0, limit: int = 10):
        return database.query(self.model_class).offset(skip).limit(limit).all()

    def create(self, database: Session, object_data):
        database_object = self.model_class(**object_data)
        database.add(database_object)
        database.commit()
        database.refresh(database_object)
        return database_object

    def update(self, database: Session, object_id: int, object_data: dict):
        database_object = self.get(database, object_id)
        if database_object:
            for key, value in object_data.items():
                setattr(database_object, key, value)
            database.commit()
            database.refresh(database_object)
        return database_object

    def delete(self, database: Session, object_id: int):
        database_object = self.get(database, object_id)
        if database_object:
            database.delete(database_object)
            database.commit()
        return database_object
