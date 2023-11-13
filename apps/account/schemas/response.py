from pydantic import BaseModel
from common.schemas import SuccessSchema


class TokenSchema(BaseModel):
    access_token: str


class RegisterResponse(SuccessSchema):
    message: str = "registered successful."


class LoggedInSchema(SuccessSchema):
    data: TokenSchema
    