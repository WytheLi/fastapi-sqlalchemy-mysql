#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 14:37
# @SoftWare: PyCharm
from fastapi.security import OAuth2PasswordRequestForm

import common.exceptions as exceptions
from common import signature
from . import repo
from db.engine import async_session


async def login(form_data: OAuth2PasswordRequestForm):
    async with async_session() as session:
        current_user = await repo.get_user_by_username(session, form_data.username)
        if not current_user:
            raise exceptions.NotFoundError(msg='用户名不存在')
        elif not await signature.verity_password(form_data.password, current_user.password):
            raise exceptions.AuthorizationError(msg='密码错误')
        elif not current_user.is_active:
            raise exceptions.AuthorizationError(msg='该用户已被锁定，无法登录')
        # 更新登陆时间
        await repo.update_user_login_time(session, form_data.username)
        # 创建token
        access_token = await signature.create_access_token(current_user.id)
        return access_token

async def register(form_data):
    async with async_session() as session:
        user = await repo.get_user_by_username(session, form_data.username)
        if user:
            raise exceptions.ForbiddenError("该用户名已注册！")
        
        user = await repo.get_user_by_mobile(session, form_data.mobile)
        if user:
            raise exceptions.ForbiddenError("该手机号已注册！")
        
        user = await repo.get_user_by_email(session, form_data.email)
        if user:
            raise exceptions.ForbiddenError("该邮箱已注册！")
        
        await repo.create_user(session, form_data)
        await session.commit()
