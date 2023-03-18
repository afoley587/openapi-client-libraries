import typing_extensions

from openapi_client.paths import PathValues
from openapi_client.apis.paths.ping import Ping

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PING: Ping,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PING: Ping,
    }
)
