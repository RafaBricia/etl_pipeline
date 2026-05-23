from src.stages.contracts.mocks.transform_contract import TRANSFORM_CONTRACT_MOCKS

from src.infra.database_repository import DatabaseRepository
from src.infra.database_conector import DatabaseConnector

# @pytest.mark.skip(reason="No need to insert data in database") # type: ignore
def test_insert_artist():
    DatabaseConnector.connect()
    database_repo = DatabaseRepository()
    data = TRANSFORM_CONTRACT_MOCKS.load_content[0]

    database_repo.insert_artist(data)
