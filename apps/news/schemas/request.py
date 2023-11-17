from pydantic import BaseModel, Field


class CategoryRequest(BaseModel):
    name: str = Field(example="消息", max_length=8, description="新闻类型")
