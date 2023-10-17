#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 14:37
# @SoftWare: PyCharm
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt

import exceptions
from common import utils
from . import repo
from db.engine import async_session


async def login(form_data: OAuth2PasswordRequestForm):
    async with async_session() as db:
        current_user = await repo.get_user_by_username(db, form_data.username)
        if not current_user:
            raise exceptions.NotFoundError(msg='用户名不存在')
        elif not await utils.verity_password(form_data.password, current_user.password):
            raise exceptions.AuthorizationError(msg='密码错误')
        elif not current_user.is_active:
            raise exceptions.AuthorizationError(msg='该用户已被锁定，无法登录')
        # 更新登陆时间
        await repo.update_user_login_time(db, form_data.username)
        # 创建token
        access_token = await utils.create_access_token(current_user.id)
        return access_token
