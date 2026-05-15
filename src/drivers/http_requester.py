from typing import Dict, Any
import requests
from requests.exceptions import RequestException


class HttpRequester:
    def __init__(self) -> None:
        self.__url = (
            "https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm"
        )
    def request_from_page(self) -> Dict[str, Any]:
        try:
            response = requests.get(self.__url, timeout=5)

            return {
                "status_code": response.status_code,
                "html_content": response.text
            }

        except RequestException as error:
            return {
                "error": str(error)
            }
