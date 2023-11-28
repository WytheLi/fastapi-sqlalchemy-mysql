#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 14:30
# @SoftWare: PyCharm
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from common.response import response_success

from .routers import account_router
from .schemas.request import RegisterSchema
from . import services


@account_router.post("/register", tags=["用户"], name="注册")
async def register(form_data: RegisterSchema):
    await services.register(form_data)
    return response_success(msg="registered successful.")


@account_router.post("/login", tags=["用户"], name="登录")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = await services.login(form_data)
    return response_success(data={"access_token": token})
