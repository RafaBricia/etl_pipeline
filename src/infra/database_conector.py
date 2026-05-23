import os
import dotenv
import mysql.connector as mysql


dotenv.load_dotenv()


class DatabaseConnector:

    connection = None

    @classmethod
    def connect(cls):
        db_connection = mysql.connect(
            host='localhost',
            user='root',
            port=3306,
            password=os.getenv('passwd'),
            database='pipeline_db'
        )

        cls.connection = db_connection
