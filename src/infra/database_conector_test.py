from .database_conector import DatabaseConnector

def test_database_connection():
    assert DatabaseConnector.connection is None
    DatabaseConnector.connect()
    assert DatabaseConnector.connection is not None
