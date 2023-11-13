#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import async_sessionmaker

from common.conf import settings

SQLALCHEMY_DATABASE_URL = f'mysql+aiomysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:' \
                          f'{settings.DB_PORT}/{settings.DB_DATABASE}?charset={settings.DB_CHARSET}'

# 创建引擎（数据库连接的工厂，它还保留连接池内的连接以便快速重用）
async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=settings.DB_ECHO, future=True)

async_session = async_sessionmaker(bind=async_engine, autoflush=False, expire_on_commit=False)


async def create_table():
    """
    创建数据库表
    """
    from models.base import Base
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
