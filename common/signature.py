#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 16:06
# @SoftWare: PyCharm
from datetime import timedelta, datetime
from typing import Union, Any

from jose import jwt
from passlib.context import CryptContext

from common.conf import settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')  # 密码加密


async def verity_password(plain_password: str, hashed_password: str) -> bool:
    """
    密码校验

    :param plain_password: 要验证的密码
    :param hashed_password: 要比较的hash密码
    :return: 比较密码之后的结果
    """
    return pwd_context.verify(plain_password, hashed_password)


async def create_access_token(data: Union[int, Any], expires_delta: Union[timedelta, None] = None) -> str:
    """
    生成加密 token

    :param data: 传进来的值
    :param expires_delta: 增加的到期时间
    :return: 加密token
    """
    if expires_delta:
        expires = datetime.utcnow() + expires_delta
    else:
        expires = datetime.utcnow() + timedelta(settings.TOKEN_EXPIRES)
    to_encode = {"exp": expires, "sub": str(data)}
    encoded_jwt = jwt.encode(to_encode, settings.TOKEN_SECRET_KEY, settings.TOKEN_ALGORITHM)
    return encoded_jwt
