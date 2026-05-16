from src.drivers.html_collector import HtmlCollector
from src.drivers.http_requester import HttpRequester
from .extract_html import ExtractHtml

def test_extract_html():

    html_collector = HtmlCollector()
    http_requester = HttpRequester()

    extract_html = ExtractHtml(html_collector, http_requester)
    response = extract_html.extract()
    print(response)

    # assert
