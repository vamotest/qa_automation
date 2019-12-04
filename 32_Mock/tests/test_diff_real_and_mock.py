import requests
import requests_mock


def real(url):
    return requests.get(url).status_code


def mock(url, mock_code):
    with requests_mock.Mocker() as m:
        m.register_uri('GET', url, status_code=mock_code)
        response_mock = requests.get(url).status_code
        return response_mock


def test_diff_real_and_mock():
    url = 'http://test.com/'
    mock_code = '500'

    response_real = real(url)
    response_mock = mock(url, mock_code)

    assert response_real != response_mock



