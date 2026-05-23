from src.infra.interfaces.database_repository import InterfaceDatabaseRepository
from src.stages.contracts.transform_contract import TranformContract
from src.errors.load_error import LoadError

class Load:
    def __init__(self, repository:InterfaceDatabaseRepository) -> None:
        self.__repository = repository

    def load(self, transform_data_content: TranformContract) -> None:

        try:
            load_content = transform_data_content.load_content
            for data in load_content:
                self.__repository.insert_artist(data)

        except Exception as exception:
            raise LoadError(
                f"exception {str(exception)}"
            ) from exception
