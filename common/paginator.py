import math

from fastapi import Query
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.selectable import Select


class Paginator(object):
    """
        基于sqlalchemy2.x 异步引擎的分页组件
    """
    page: int = Query(1, ge=1, description='Page number')
    size: int = Query(20, gt=10, le=100, description='Page size')  # 默认 20 条记录

    def __init__(self, session: AsyncSession, sqlalchemy_query: Select):
        """
        :param sqlalchemy_query:  sqlalchemy_query 查询语句
        """
        self.page = self.page.default
        self.size = self.size.default
        self.sqlalchemy_query = sqlalchemy_query
        self.session = session

    @property
    async def total(self):
        query = select(func.count()).select_from(self.sqlalchemy_query)
        res = await self.session.execute(query)
        return res.scalars().first()

    @property
    async def pages(self):
        return math.ceil(await self.total / self.size)

    async def page_info(self):
        """
            分页信息
        """
        return {
            "total": await self.total,
            "pages": await self.pages,
            "page": self.page,
            "size": self.size
        }

    async def pagination(self):
        query = self.sqlalchemy_query.limit(self.size).offset((self.page - 1) * self.size)
        res = await self.session.execute(query)
        return res.scalars().all()
