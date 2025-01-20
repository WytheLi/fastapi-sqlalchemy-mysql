#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, declared_attr
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


# class Base(AsyncAttrs, DeclarativeBase):
#
#     @declared_attr.directive
#     def __tablename__(cls) -> str:
#         return cls.__name__.lower()
