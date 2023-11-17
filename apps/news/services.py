from sqlalchemy.ext.asyncio import AsyncSession

from common.paginator import Paginator
from . import repo


async def get_category(session: AsyncSession):
    query = await repo.get_category()
    paginator = Paginator(session, query)
    items = await paginator.pagination()
    page_info = await paginator.page_info()
    return items, page_info
