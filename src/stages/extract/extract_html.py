from datetime import datetime
from src.stages.contracts.extract_contract import ExtraxtContract
from src.errors.extract_error import ExtractError
from src.drivers.interfaces.http_requester_interface import HttpRequesterInterface
from src.drivers.interfaces.html_collector_interface import HtmlCollectorInterface

class ExtractHtml:
    def __init__ (self, html_collector:HtmlCollectorInterface, http_requester:HttpRequesterInterface) -> None:
        self.__html_collector = html_collector
        self.__http_requester = http_requester

    def extract(self):
        try:
            html_information = self.__http_requester.request_from_page()
            essencial_information = self.__html_collector.collect_essencial_information(html_information['html_content'])

            return ExtraxtContract(
                raw_information_content = essencial_information,
                extraction_date = datetime.now()
            )
        except Exception as exception:
            raise ExtractError(str(exception)) from exception
