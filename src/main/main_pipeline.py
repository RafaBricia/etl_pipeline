from src.stages.extract.extract_html import ExtractHtml
from src.stages.transform.transform_raw_data import TransformRawData
from src.stages.load.load import Load

from src.drivers.html_collector import HtmlCollector
from src.drivers.http_requester import HttpRequester

from src.infra.database_conector import DatabaseConnector
from src.infra.database_repository import DatabaseRepository

class MainPipeline:

    def __init__(self) -> None:
        html_collector = HtmlCollector()
        http_requester = HttpRequester()

        repository = DatabaseRepository()

        self.__extract = ExtractHtml(html_collector, http_requester)
        self.__transform = TransformRawData()
        self.__load = Load(repository)

    def run_pipeline(self) -> None:
        DatabaseConnector().connect()

        extract_contract = self.__extract.extract()
        transform_contract = self.__transform.transform(extract_contract)
        self.__load.load(transform_contract)
