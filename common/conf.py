#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import lru_cache
import os
from pathlib import Path
from typing import ClassVar
from dotenv import load_dotenv

from pydantic_settings import BaseSettings


load_dotenv(verbose=True)


# 获取项目根目录
workspaceFolder = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    # Fastapi
    TITLE: str = 'FastAPI'
    VERSION: str = 'v0.1'
    DESCRIPTION: str = "Fastapi Web Service."
    DOCS_URL: str = '/v1/docs'
    REDOCS_URL: str = '/v1/redocs'
    OPENAPI_URL: str = '/v1/openapi'

    # Uvicorn
    UVICORN_HOST: str = os.getenv('UVICORN_HOST', '127.0.0.1')
    UVICORN_PORT: int = os.getenv('UVICORN_PORT', 8000)
    UVICORN_RELOAD: bool = os.getenv('UVICORN_RELOAD', True)

    # Static Server
    STATIC_FILES: bool = os.getenv('STATIC_FILES', False)

    # Log
    log_file: ClassVar[str] = os.path.join(workspaceFolder, 'logs', 'fastapi-{time:YYYY-MM-DD}.log')
    log_formatter: ClassVar[str] = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>'
    LOG_LEVEL: str = os.getenv('LOG_LEVEL', "INFO")
    LOG_PATH: str = os.getenv('LOG_PATH', log_file)
    LOG_FORMATTER: str = os.getenv('LOG_FORMATTER', log_formatter)

    # DB
    DB_ECHO: bool = os.getenv('DB_ECHO', True)
    DB_HOST: str = os.getenv('DB_HOST', '127.0.0.1')
    DB_PORT: int = os.getenv('DB_PORT', 3306)
    DB_USER: str = os.getenv('DB_USER', 'root')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD', 'vivi1911')
    DB_DATABASE: str = os.getenv('DB_DATABASE', 'demo')
    DB_CHARSET: str = os.getenv('DB_CHARSET', 'utf8mb4')

    # Redis
    REDIS_OPEN: bool = os.getenv('REDIS_OPEN', False)
    REDIS_HOST: str = os.getenv('REDIS_HOST', '127.0.0.1')
    REDIS_PORT: int = os.getenv('REDIS_PORT', 6379)
    REDIS_PASSWORD: str = os.getenv('REDIS_PASSWORD', '')
    REDIS_DATABASE: int = os.getenv('REDIS_DATABASE', 0)
    REDIS_TIMEOUT: int = os.getenv('REDIS_TIMEOUT', 5)

    # Token
    TOKEN_ALGORITHM: str = os.getenv('TOKEN_ALGORITHM', 'HS256')  # 算法
    TOKEN_SECRET_KEY: str = os.getenv('TOKEN_SECRET_KEY', '1VkVF75nsNABBjK_7-qz7GtzNy3AMvktc9TCPwKczCk')  # 密钥 secrets.token_urlsafe(32))
    TOKEN_EXPIRES: int = os.getenv('TOKEN_EXPIRES', 60 * 24 * 1)  # token 时效 60 * 24 * 1 = 1 天

    # MIDDLEWARE
    MIDDLEWARE_CORS: bool = os.getenv('MIDDLEWARE_CORS', True)
    MIDDLEWARE_GZIP: bool = os.getenv('MIDDLEWARE_GZIP', True)

    # Administrator
    SUPERUSER_USERNAME: str = os.getenv('SUPERUSER_USERNAME', 'admin')
    SUPERUSER_PASSWORD: str = os.getenv('SUPERUSER_PASSWORD', 'qwe123456')


@lru_cache  # 缓存执行函数的结果
def get_settings():
    """
        读取配置并缓存
        lru_cache装饰器会缓存执行函数的结果
    :return:
    """
    return Settings()


settings = get_settings()
