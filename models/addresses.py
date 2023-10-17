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


class Addresses(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    province = Column(String(16), doc="省")
    city = Column(String(30), doc="城市")
    area = Column(String(30), doc="区域")
    address = Column(String(128), doc="详细地址")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r})"
