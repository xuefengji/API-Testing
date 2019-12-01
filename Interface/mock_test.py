from unittest import mock

class mockTest:
    def test_mock(self,mock_method,url,mock_data,method,response_data):
        mock_method = mock.Mock(return_value=response_data)
        return mock_method(url,mock_data,method)