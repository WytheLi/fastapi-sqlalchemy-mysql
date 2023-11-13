#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 14:47
# @SoftWare: PyCharm
# Repository 数据访问层
from typing import Optional
from pydantic import BaseModel

# from sqlalchemy import select
from sqlalchemy.future import select
from sqlalchemy import update, func
from sqlalchemy.ext.asyncio import AsyncSession
from common.crypt import get_hash_password

from models.users import Users


async def get_user_by_username(session: AsyncSession, username: str):
    user = await session.execute(select(Users).where(Users.username == username))
    return user.scalars().first()


async def get_user_by_mobile(session: AsyncSession, mobile: str):
    user = await session.execute(select(Users).where(Users.mobile == mobile))
    return user.scalars().first()


async def get_user_by_email(session: AsyncSession, email: str):
    user = await session.execute(select(Users).where(Users.email == email))
    return user.scalars().first()


async def update_user_login_time(session: AsyncSession, username: str) -> int:
    user = await session.execute(
        update(Users)
        .where(Users.username == username)
        .values(last_login=func.now())
    )
    return user.rowcount


async def create_user(session: AsyncSession, form_data: BaseModel):
    form_data.password = await get_hash_password(form_data.password)
    user = Users(**form_data.model_dump())
    session.add(user)
