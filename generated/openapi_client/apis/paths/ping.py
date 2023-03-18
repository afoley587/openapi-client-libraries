from openapi_client.paths.ping.get import ApiForget
from openapi_client.paths.ping.post import ApiForpost
from openapi_client.paths.ping.delete import ApiFordelete


class Ping(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
