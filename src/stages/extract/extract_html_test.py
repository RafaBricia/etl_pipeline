from src.stages.contracts.extract_contract import ExtraxtContract
from src.errors.extract_error import ExtractError

from src.drivers.html_collector import HtmlCollector
from src.drivers.http_requester import HttpRequester
from .extract_html import ExtractHtml

def test_extract_html():

    html_collector = HtmlCollector()
    http_requester = HttpRequester()

    extract_html = ExtractHtml(html_collector, http_requester)
    response = extract_html.extract()
    print(response)

    assert isinstance(response,ExtraxtContract)

def test_extract_html_error():

    html_collector = 'Teste de error na extração'
    http_requester = HttpRequester()

    extract_html = ExtractHtml(html_collector, http_requester)

    try:
        extract_html.extract()
    except Exception as exception: #pylint: disable=broad-except
        assert isinstance(exception,ExtractError)
