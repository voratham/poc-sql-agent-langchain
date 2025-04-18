from sqlalchemy import create_engine, MetaData
from langchain_community.utilities import SQLDatabase


class DatabaseConnector:
    def __init__(self, connection_string=None):
        print("Initializing DatabaseConnector...")
        self.connection_string = connection_string
        if not self.connection_string:
            raise ValueError("Database connection string not provided")

        self.engine = create_engine(self.connection_string)
        self.metadata = MetaData()
        self.metadata.reflect(bind=self.engine)
        self.db = SQLDatabase(self.engine)

    def get_table_names(self):
        return self.engine.table_names()

    def get_table_info(self):
        """Get schema information for all tables."""
        return self.db.get_table_info()
