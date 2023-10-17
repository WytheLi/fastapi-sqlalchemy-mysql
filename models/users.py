#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
from sqlalchemy.orm import relationship

from models.base import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(32), nullable=False, doc="用户名")
    password = Column(String(255), doc="非明文密码")
    is_active = Column(Boolean, default=True, doc="有效用户")
    last_login = Column(DateTime, onupdate=func.now(), doc="最近登录时间")

    # addresses = relationship(back_populates="user", cascade="all, delete-orphan")

    def __repr__(self) -> str:
        return f"User(id={self.id!r})"
