from .html_collector import HtmlCollector
from .mocks.http_requester_mock import mock_http_requester

def test_collect_essencial_information():
    mock_request = mock_http_requester()
    html_collector = HtmlCollector()

    essencial_information = html_collector.collect_essencial_information(mock_request['html_content'])
    print(essencial_information) # --- IGNORE ---

    assert isinstance(essencial_information, list)
    assert isinstance(essencial_information[0], dict)
    assert 'name' in essencial_information[0]
    assert 'link' in essencial_information[0]
