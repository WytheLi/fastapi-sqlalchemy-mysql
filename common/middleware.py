import datetime
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware


class HttpMiddleware(BaseHTTPMiddleware):
    """
        请求中间件
        用于在http/https请求前后添加业务逻辑
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        start_time = datetime.now()
        response = await call_next(request)
        end_time = datetime.now()
        print(f'{response.status_code} {request.client.host} {request.method} {request.url} {end_time - start_time}')
        return response
