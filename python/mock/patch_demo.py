from api import Api
import mock

_api = Api()

# mock api call
with mock.patch('requests.get', autospec=True) as mock_requests:
    mock_requests.return_value.text = "google is mocked"
    print _api.google()

# mock time
@mock.patch('time.time', autospec=True)
def my_time(mock_time):
    mock_time.return_value = '0000000.0000'
    print _api.time()

my_time()
