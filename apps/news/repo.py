from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import delete
from sqlalchemy.future import select

from models.users import Category
from .schemas.request import CategoryRequest


async def create_category(session: AsyncSession, param: CategoryRequest):
    category = Category(**param.model_dump())
    session.add(category)


async def delete_category(session: AsyncSession, cid: int):
    ret = await session.execute(
        delete(Category).where(Category.id == cid)
    )
    return ret.rowcount


async def get_category_by_id(session: AsyncSession, cid: int):
    category = await session.execute(select(Category).where(Category.id == cid))
    return category.scalars().first()


async def get_category():
    query = select(Category).order_by(Category.id)
    return query