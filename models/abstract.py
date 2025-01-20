#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 11:53
# @SoftWare: PyCharm
from sqlalchemy import Column, DateTime, func

from db import Base


class BaseModel(Base):
    __abstract__ = True

    create_time = Column(DateTime, default=func.now(), doc='创建时间')
    update_time = Column(DateTime, default=func.now(), onupdate=func.now(), doc='更新时间')
