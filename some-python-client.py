import openapi_client
from openapi_client.paths.ping import post  # noqa: E501
from openapi_client import configuration, schemas, api_client
from openapi_client.model.ping_request import PingRequest

_configuration = configuration.Configuration(host="http://localhost:8000")
cli = api_client.ApiClient(configuration=_configuration)
api = post.ApiForpost(api_client=cli)  # noqa: E501
response = api.post(PingRequest(ping="ping", pong="pong"))
print(response.body)