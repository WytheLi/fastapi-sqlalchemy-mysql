#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from sqlalchemy import event
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import create_session, sessionmaker

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


async def get_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        except Exception as ex:
            await session.rollback()
            raise ex
        else:
            await session.commit()
        finally:
            await session.close()


# # 创建监听器，将SQL输出到控制台，便于调试。（event事件监听器，暂时不支持异步引擎连接数据库对象）
# @event.listens_for(async_engine, "before_cursor_execute", retval=True)
# def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
#     conn.info.setdefault('query_start_time', []).append(time.time())
#     print("Start Query: %s", statement)

# @event.listens_for(async_engine, "after_cursor_execute", retval=True)
# def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
#     total = time.time() - conn.info['query_start_time'].pop(-1)
#     print("Query Complete: %s, Time: %f", statement, total)
