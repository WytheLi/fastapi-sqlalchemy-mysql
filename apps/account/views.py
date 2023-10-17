#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 14:30
# @SoftWare: PyCharm
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from .routers import account_router
from .schemas import LoggedInSchema
from . import services


@account_router.post("/login", response_model=LoggedInSchema, description="登录")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = await services.login(form_data)
    return LoggedInSchema(access_token=token)
