from pydantic import BaseModel, Field


class SuccessSchema(BaseModel):
    code: int = 200
    message: str = "Success."


class FailSchema(BaseModel):
    code: int = 0
    message: str = "Request unsuccessful."
