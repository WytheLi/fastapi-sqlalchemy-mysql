#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 14:30
# @SoftWare: PyCharm
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm

from .routers import account_router
from .schemas.request import RegisterSchema
from .schemas.response import LoggedInSchema, RegisterResponse
from . import services


@account_router.post("/register", response_model=RegisterResponse, tags=["用户"], name="注册")
async def register(form_data: RegisterSchema):
    await services.register(form_data)
    return RegisterResponse()


@account_router.post("/login", response_model=LoggedInSchema, tags=["用户"], name="登录")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    token = await services.login(form_data)
    return LoggedInSchema(data={"access_token": token})
