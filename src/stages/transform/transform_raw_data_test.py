from src.stages.contracts.mocks.extract_contract import EXTRACT_CONTRACT_MOCKS
from src.stages.contracts.transform_contract import TranformContract
from src.errors.transform_error import TransformError
from .transform_raw_data import TransformRawData

def test_transform ():
    transform_raw_date = TransformRawData()
    transformed_data_content = transform_raw_date.transform(EXTRACT_CONTRACT_MOCKS)

    assert isinstance(transformed_data_content, TranformContract)
    assert 'first_name' in transformed_data_content.load_content[0]
    assert 'last_name' in transformed_data_content.load_content[0]
    assert 'surname' in transformed_data_content.load_content[0]
    assert 'artist_id' in transformed_data_content.load_content[0]
    assert 'link' in transformed_data_content.load_content[0]
    assert 'extraction_date' in transformed_data_content.load_content[0]


def test_transform_error ():
    transform_raw_date = TransformRawData()

    try:
        _transformed_data_content = transform_raw_date.transform('Entrada com erro')
    except Exception as exception: #pylint: disable=broad-except
        assert isinstance(exception,TransformError)
