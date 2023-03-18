import time
import openapi_client
from pprint import pprint
from openapi_client.apis.tags import default_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.ping_request import PingRequest
from openapi_client.model.ping_response import PingResponse
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost:8000"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    ping_request = PingRequest(
        ping="ping_example",
        pong="pong_example",
    ) # PingRequest | 

    try:
        # Deleteping
        api_response = api_instance.delete_ping_ping_delete(ping_request)
        pprint(api_response.body)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_ping_ping_delete: %s\n" % e)