#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 14:24
# @SoftWare: PyCharm
from fastapi import APIRouter

from apps.account import account_router
from apps.news import news_router

router = APIRouter(prefix='/v1')

router.include_router(account_router, prefix='/users', tags=['用户管理'])
router.include_router(news_router, prefix='/news', tags=['新闻管理'])
