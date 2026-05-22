from typing import List, Dict

class HtmlCollectorSpy:

    def __init__(self) -> None:
        self.collect_essencial_information_atributtes = {}


    def collect_essencial_information(self, html:str) -> List[Dict[str, str]]:
        self.collect_essencial_information_atributtes['html'] = html

        return [{
        'name': 'SomeName',
        'link': 'https://some-link.com'
    }]
