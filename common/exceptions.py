#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 14:57
# @SoftWare: PyCharm
from typing import Any

from fastapi import HTTPException, status


class BaseExceptionMixin(Exception):
    code: int

    def __init__(self, *, msg: str = None, data: Any = None):
        self.msg = msg
        self.data = data


class HTTPError(HTTPException):
    pass


class RequestError(BaseExceptionMixin):
    code = status.HTTP_400_BAD_REQUEST

    def __init__(self, *, msg: str = 'Bad Request', data: Any = None):
        super().__init__(msg=msg, data=data)


class ForbiddenError(BaseExceptionMixin):
    code = status.HTTP_403_FORBIDDEN

    def __init__(self, *, msg: str = 'Forbidden', data: Any = None):
        super().__init__(msg=msg, data=data)


class NotFoundError(BaseExceptionMixin):
    code = status.HTTP_404_NOT_FOUND

    def __init__(self, *, msg: str = 'Not Found', data: Any = None):
        super().__init__(msg=msg, data=data)


class ServerError(BaseExceptionMixin):
    code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, *, msg: str = 'Internal Server Error', data: Any = None):
        super().__init__(msg=msg, data=data)


class GatewayError(BaseExceptionMixin):
    code = status.HTTP_502_BAD_GATEWAY

    def __init__(self, *, msg: str = 'Bad Gateway', data: Any = None):
        super().__init__(msg=msg, data=data)


class AuthorizationError(BaseExceptionMixin):
    code = status.HTTP_401_UNAUTHORIZED

    def __init__(self, *, msg: str = 'Permission denied', data: Any = None):
        super().__init__(msg=msg, data=data)


class TokenError(BaseExceptionMixin):
    code = status.HTTP_401_UNAUTHORIZED

    def __init__(self, *, msg: str = 'Token is invalid', data: Any = None):
        super().__init__(msg=msg, data=data)
