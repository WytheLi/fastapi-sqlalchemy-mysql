#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import enum
from sqlalchemy import (
    Boolean,
    Column,
    Enum,
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
from sqlalchemy.orm import relationship

from models.base import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(32), unique=True, nullable=False, doc="用户名")
    password = Column(String(255), nullable=False, doc="非明文密码")
    mobile = Column(String(11), unique=True, nullable=False)
    email = Column(String(32), unique=True)
    avatar_url = Column(String(256), doc="用户头像")
    # Enum((0, 'Undefined'), (1, 'Male'), (2, 'Female'))
    gender = Column(Integer, default=0, doc="性别，0：未透露性别，1：男性，2：女性")
    is_active = Column(Boolean, default=True, doc="有效用户")
    last_login = Column(DateTime, onupdate=func.now(), doc="最近登录时间")

    # addresses = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id={self.id!r})"
