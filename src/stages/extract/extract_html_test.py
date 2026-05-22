from src.stages.contracts.extract_contract import ExtractContract
from src.errors.extract_error import ExtractError

from src.drivers.tests.html_collector import HtmlCollectorSpy
from src.drivers.tests.http_requester import HttpRequesterSpy
from .extract_html import ExtractHtml

def test_extract_html():

    html_collector = HtmlCollectorSpy()
    http_requester = HttpRequesterSpy()

    extract_html = ExtractHtml(html_collector, http_requester)
    response = extract_html.extract()

    assert isinstance(response,ExtractContract)
    assert http_requester.request_from_page_count == 1
    assert 'html' in html_collector.collect_essencial_information_atributtes

def test_extract_html_error():
    http_requester = 'Teste de error na extração'
    html_collector = HtmlCollectorSpy()

    extract_html = ExtractHtml(html_collector, http_requester)

    try:
        extract_html.extract()
    except Exception as exception: #pylint: disable=broad-except
        assert isinstance(exception,ExtractError)
