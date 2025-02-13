from sqlalchemy.orm import Session


class CRUDBase:
    def __init__(self, model_class):
        self.model_class = model_class

    def get(self, database: Session, object_id: int):
        return database.query(self.model_class).filter(
            getattr(self.model_class, "id") == object_id).first()

    def get_all(self, database: Session):
        return database.query(self.model_class).all()

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

    def filter_by(self, database: Session, **filters):
        query = database.query(self.model_class)
        for field, value in filters.items():
            column = getattr(self.model_class, field)
            query = query.filter(column.ilike(f"%{value}%") if isinstance(value, str) else column == value)
        return query.all()
