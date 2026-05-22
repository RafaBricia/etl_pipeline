from typing import Dict, Any


class HttpRequesterSpy():
    def __init__(self) -> None:
        self.request_from_page_count = 0

    def request_from_page(self) -> Dict[str, Any]:
        self.request_from_page_count += 1
        return {
            "status_code": 200,
            "html_content": "<h1>Olá mundo!</h1>"
        }
