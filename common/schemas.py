from typing import Any
from pydantic import BaseModel


class SuccessSchema(BaseModel):
    code: int = 200
    message: str = "Request successful."
    data: Any = None


class FailSchema(BaseModel):
    code: int = 0
    message: str = "Request unsuccessful."
