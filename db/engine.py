#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from sqlalchemy import event
from sqlalchemy.orm import create_session, sessionmaker, Session

from common.conf import settings

SQLALCHEMY_DATABASE_URL = f'mysql+mysql://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:' \
                          f'{settings.DB_PORT}/{settings.DB_DATABASE}?charset={settings.DB_CHARSET}'

# 创建引擎（数据库连接的工厂，它还保留连接池内的连接以便快速重用）
engine = create_session(SQLALCHEMY_DATABASE_URL, future=True)

session = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)


async def get_session() -> Session:
    async with session() as session:
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
