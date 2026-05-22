# Pylint: disable=multiple-statements

from typing import List, Dict

from src.stages.contracts.extract_contract import ExtractContract
from src.stages.contracts.transform_contract import TranformContract
from src.errors.transform_error import TransformError

class TransformRawData:
    def transform (self, extract_contract:ExtractContract) -> TranformContract:
        try:
            tranformed_information = self.__filter_and_transform_data(extract_contract)
            transformed_data_content = TranformContract(
                load_content=tranformed_information
            )

            return transformed_data_content
        except Exception as exception:
            raise TransformError(
                f"exception {str(exception)}"
            ) from exception

    def __filter_and_transform_data(self, extract_contract:ExtractContract) -> List[Dict]:
        extraction_date = extract_contract.extraction_date
        data_content = extract_contract.raw_information_content

        tranformed_information = []

        for data in data_content:
            transformed_data = None
            link = data['link']

            if 'artistid=' not in link:
                continue

            names = None

            if ',' in data['name']:
                names = data['name'].split(', ')

            elif ' ' in data['name']:
                names = data['name'].split(' ')

            else: names = [data['name']]

            transformed_data = self.__transform_data(names, link)
            transformed_data['extraction_date'] = extraction_date

            tranformed_information.append(transformed_data)

        return tranformed_information

    @classmethod
    def __transform_data(cls, names:List, link:str) -> Dict:
        link_artist_id = link.split('artistid=')

        if len(names) == 2:
            return {
                'first_name': names[1],
                'last_name': names[0],
                'surname': None,
                'artist_id': link_artist_id[1],
                'link': link
            }

        if len(names) == 3:
            return {
                'first_name': names[2],
                'last_name': names[0],
                'surname': names[1],
                'artist_id': link_artist_id[1],
                'link': link
            }
        return {
            'first_name': names[0],
            'last_name':None,
            'surname': None,
            'artist_id': link_artist_id[1],
            'link': link
        }
