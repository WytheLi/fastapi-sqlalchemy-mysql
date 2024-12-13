#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 14:30
# @SoftWare: PyCharm
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from common.response import response_success
from db.async_engine import get_async_session

from .routers import account_router
from .schemas.request import RegisterSchema
from . import services


@account_router.post("/register", tags=["用户"], name="注册")
async def register(form_data: RegisterSchema, session: AsyncSession = Depends(get_async_session)):
    await services.register(session, form_data)
    return await response_success(msg="registered successful.")


@account_router.post("/login", tags=["用户"], name="登录")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_async_session)):
    token = await services.login(session, form_data)
    return await response_success(data={"access_token": token})
