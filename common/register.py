#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 16:56
# @SoftWare: PyCharm
# 注册模块
from contextlib import asynccontextmanager
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.gzip import GZipMiddleware

from common.conf import settings
from db.async_engine import create_table, async_session
from db.engine import session
from models.users import Users
from routers import router


def create_app():
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        docs_url=settings.DOCS_URL,
        redoc_url=settings.REDOCS_URL,
        openapi_url=settings.OPENAPI_URL,
        lifespan=init_app
    )

    if settings.STATIC_FILES:
        # 注册静态文件服务
        register_static_file(app)

    # 中间件
    add_middleware(app)

    # 路由
    register_router(app)

    # 全局异常处理
    # register_exception(app)

    return app


async def init_app(app: FastAPI):
    """
        初始化
    Args:
        app (FastAPI): _description_
    """
    # 创建数据库表
    await create_table()

    # 创建管理员用户
    await create_superuser()

    # # limiter请求限频率
    # from fastapi_limiter import FastAPILimiter
    # await FastAPILimiter.init(redis_client, prefix=settings.LIMITER_REDIS_PREFIX, http_callback=http_limit_callback)
    yield


def register_router(app: FastAPI):
    """
        注册路由

    :param app: FastAPI
    :return:
    """
    app.include_router(router)


def register_static_file(app: FastAPI):
    """
        静态文件交互开发模式, 生产使用 nginx 静态资源服务

    :param app:
    :return:
    """
    import os
    from fastapi.staticfiles import StaticFiles
    if not os.path.exists("./static"):
        os.mkdir("./static")
    app.mount("/static", StaticFiles(directory="static"), name="static")


def on_event(app: FastAPI):
    """
        fastapi事件监听器
        用于web service服务启动前后的一些操作，如：服务启动前根据模型创建数据库表

    :param app: FastAPI
    :return:
    """
    @app.on_event("startup")
    async def startup_event():
        if settings.REDIS_OPEN:
            # 连接redis
            await redis_client.init_redis_connect()

    @app.on_event("shutdown")
    async def shutdown_event():
        if settings.REDIS_OPEN:
            # 关闭redis连接
            await redis_client.close()


def add_middleware(app) -> None:
    # gzip
    if settings.MIDDLEWARE_GZIP:
        app.add_middleware(GZipMiddleware)

    # 跨域
    if settings.MIDDLEWARE_CORS:
        app.add_middleware(
            CORSMiddleware,
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )


async def create_superuser():
    async with async_session() as session:
        user = Users()
        user.username = settings.SUPERUSER_USERNAME
        user.mobile = settings.SUPERUSER_USERNAME
        user.password = settings.SUPERUSER_PASSWORD
        user.is_admin = True

        session.add(user)
        await session.commit()
