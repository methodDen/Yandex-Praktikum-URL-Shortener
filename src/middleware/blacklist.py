from typing import Callable

from starlette import status
from starlette.requests import Request
from starlette.responses import Response


class BlacklistMiddleware:

    def __init__(self, blacklist: list[str]):
        self.blacklist = blacklist

    async def __call__(self, request: Request, call_next: Callable) -> Response:
        client_host = request.client.host
        if client_host in self.blacklist:
            return Response("Blocked", status_code=status.HTTP_403_FORBIDDEN)
        return await call_next(request)