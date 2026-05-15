from .http_requester import HttpRequester


def test_request_from_page(requests_mock):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ1.htm'

    status_code = 200
    context_text = 'o teste passou!'

    requests_mock.get(
        url,
        status_code=status_code,
        text=context_text
    )

    http_requester = HttpRequester()
    request_response = http_requester.request_from_page()

    assert request_response['status_code'] == status_code
    assert request_response['html_content'] == context_text
