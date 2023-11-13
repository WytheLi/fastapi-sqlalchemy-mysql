#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 11:53
# @SoftWare: PyCharm
from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    String,
    Float,
    Text,
    Date,
    DateTime,
    func,
    Index
)
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    create_time = Column(DateTime, default=func.now(), doc='创建时间')
    update_time = Column(DateTime, default=func.now(), onupdate=func.now(), doc='更新时间')

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
