from typing import Dict
from .database_conector import DatabaseConnector
from .interfaces.database_repository import InterfaceDatabaseRepository

class DatabaseRepository(InterfaceDatabaseRepository):

    def insert_artist(self, data: Dict) -> None:

        query = '''
            INSERT INTO artists (
                first_name,
                second_name,
                surname,
                artist_id,
                link,
                extraction_date
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        '''

        cursor = DatabaseConnector.connection.cursor()
        cursor.execute(query, tuple(data.values()))

        DatabaseConnector.connection.commit()
