from sqlalchemy import create_engine, text

from app.core.config import DATABASE_URL


def clear_all_tables():
    engine = create_engine(DATABASE_URL)

    with engine.connect() as connection:
        # Disable foreign key checks temporarily
        connection.execute(text("SET FOREIGN_KEY_CHECKS = 0"))

        # Get all tables
        result = connection.execute(text("SHOW TABLES"))
        tables = [row[0] for row in result]

        # Truncate each table
        for table in tables:
            connection.execute(text(f"TRUNCATE TABLE {table}"))

        # Re-enable foreign key checks
        connection.execute(text("SET FOREIGN_KEY_CHECKS = 1"))

        print(f"Successfully cleared {len(tables)} tables:")
        for table in tables:
            print(f"- {table}")


if __name__ == "__main__":
    clear_all_tables()
