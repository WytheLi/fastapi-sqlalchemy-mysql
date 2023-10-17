#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 14:31
# @SoftWare: PyCharm
from typing import Optional

from pydantic import BaseModel


class LoggedInSchema(BaseModel):
    code: int = 200
    msg: str = 'Success'
    access_token: str = ''
