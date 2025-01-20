#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from .users import *
from .addresses import *

# 新增的Model请在以上导入，alembic env.py中的Base类将从这里导入，确保所有定义的Model都被alembic加载
from db import Base
