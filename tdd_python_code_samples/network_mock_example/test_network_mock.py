from unittest.mock import MagicMock
from network_mock import getURL

def test_callsGetAndReturnsGoodResult(monkeypatch):
    mock_result = MagicMock()
    mock_result.text = "Hello World"
    mock_get = MagicMock(return_value=mock_result)
    monkeypatch.setattr("requests.get", mock_get)
    result = getURL("http://www.cnn.com")
    mock_get.assert_called_once_with("http://www.cnn.com")
    assert result.text == "Hello World"

