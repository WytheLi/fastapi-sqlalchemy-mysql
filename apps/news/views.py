from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from common.response import response_success
from db.async_engine import get_async_session
from . import services
from . import repo
from .schemas.request import CategoryRequest
from .routers import news_router


@news_router.post("/category", name="创建分类", tags=["新闻分类"])
async def create_category(param: CategoryRequest,
                          session: AsyncSession = Depends(get_async_session)):
    await repo.create_category(session, param)
    return response_success(msg="Category create successful.")


@news_router.delete("/category/{cid}", name="删除分类", tags=["新闻分类"])
async def delete_category(cid: int, session: AsyncSession = Depends(get_async_session)):
    await repo.delete_category(session, cid)
    return response_success(msg="Category delete successful.")


@news_router.get("/category/{cid}", name="查询某个分类项", tags=["新闻分类"])
async def get_category_by_id(cid: int, session: AsyncSession = Depends(get_async_session)):
    category = await repo.get_category_by_id(session, cid)
    data = await category.get_info()
    return await response_success(data=data)


@news_router.get("/category", name="新闻分类列表", tags=["新闻分类"])
async def get_category(session: AsyncSession = Depends(get_async_session)):
    items, page_info = await services.get_category(session)
    data = {
        "items": [{"id": c.id, "name": c.name} for c in items],
        "page_info": page_info
    }
    return await response_success(data=data)
