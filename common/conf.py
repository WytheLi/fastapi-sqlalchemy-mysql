#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import lru_cache     # 缓存执行函数的结果

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Fastapi
    TITLE: str = 'FastAPI'
    VERSION: str = 'v0.1'
    DESCRIPTION: str = "Fastapi Web Service."
    DOCS_URL: str = '/v1/docs'
    REDOCS_URL: str = '/v1/redocs'
    OPENAPI_URL: str = '/v1/openapi'

    # Uvicorn
    UVICORN_HOST: str = '127.0.0.1'
    UVICORN_PORT: int = 8000
    UVICORN_RELOAD: bool = True

    # Static Server
    STATIC_FILES: bool = True

    # DB
    DB_ECHO: bool = False
    DB_HOST: str = '127.0.0.1'
    DB_PORT: int = 3306
    DB_USER: str = 'root'
    DB_PASSWORD: str = 'vivi1911'
    DB_DATABASE: str = 'fastapi_demo'
    DB_CHARSET: str = 'utf8mb4'

    # Redis
    REDIS_OPEN: bool = False
    REDIS_HOST: str = '127.0.0.1'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = ''
    REDIS_DATABASE: int = 0
    REDIS_TIMEOUT: int = 5

    # Token
    TOKEN_ALGORITHM: str = 'HS256'  # 算法
    TOKEN_SECRET_KEY: str = '1VkVF75nsNABBjK_7-qz7GtzNy3AMvktc9TCPwKczCk'  # 密钥 secrets.token_urlsafe(32))
    TOKEN_EXPIRES: int = 60 * 24 * 1  # token 时效 60 * 24 * 1 = 1 天


@lru_cache
def get_settings():
    """
        读取配置并缓存
        lru_cache装饰器会缓存执行函数的结果
    :return:
    """
    return Settings()


settings = get_settings()
