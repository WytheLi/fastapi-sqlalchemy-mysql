#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 14:47
# @SoftWare: PyCharm
# Repository 数据访问层
from typing import Optional

# from sqlalchemy import select
from sqlalchemy.future import select
from sqlalchemy import update, func
from sqlalchemy.ext.asyncio import AsyncSession

from models.users import Users


async def get_user_by_username(session: AsyncSession, username: str) -> Optional[Users]:
    user = await session.execute(select(Users).where(Users.username == username))
    return user.scalars().first()


async def update_user_login_time(db: AsyncSession, username: str) -> int:
    user = await db.execute(
        update(Users)
        .where(Users.username == username)
        .values(last_login=func.now())
    )
    return user.rowcount
