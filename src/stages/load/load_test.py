from src.stages.contracts.mocks.transform_contract import TRANSFORM_CONTRACT_MOCKS
from src.stages.load.load import Load
from src.errors.load_error import LoadError

class RepositorySpy:
    def __init__(self) -> None:
        self.insert_artist_atribute = []

    def insert_artist(self, data):
        self.insert_artist_atribute.append(data)



def test_load():
    try:
        repo = RepositorySpy()
        load = Load(repo)
        load.load(TRANSFORM_CONTRACT_MOCKS)

        assert repo.insert_artist_atribute == TRANSFORM_CONTRACT_MOCKS.load_content

    except Exception as exception: #pylint: disable=broad-except
        assert isinstance(exception,LoadError)

def test_load_error():

    repo = RepositorySpy()
    load = Load(repo)

    try:
        load.load('entrada com erro')
        assert False

    except Exception as exception: #pylint: disable=broad-except
        assert isinstance(exception,LoadError)
