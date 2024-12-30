import re
from pydantic import BaseModel, Field, field_validator
from email_validator import validate_email, EmailNotValidError
from pydantic_core.core_schema import ValidationInfo


class RegisterSchema(BaseModel):
    
    username: str = Field(..., example="willi", description="用户名")
    mobile: str = Field(min_length=11, max_length=11, description="手机号")
    password: str = Field(min_length=8, description="密码")
    email: str = Field(example="wytheli168@163.com", description="邮箱")
    
    @field_validator('email')
    @classmethod
    def email_validate(cls, email: str, config: ValidationInfo):
        try:
            validate_email(email, check_deliverability=False).email
        except EmailNotValidError:
            raise ValueError('邮箱格式错误')
        return email

    @field_validator('mobile')
    @classmethod
    def mobile_validate(cls, mobile: str, config: ValidationInfo):
        pattern = r'^(?:\+?86)?1(?:3\d{3}|5[^4\D]\d{2}|8\d{3}|7(?:[235-8]\d{2}|4(?:0\d|1[0-2]|9\d))|9[189]\d{2}|6[2567]\d{2}|4(?:[14]0\d{3}|[68]\d{4}|[579]\d{2}))\d{6}$'  
        if not re.match(pattern, mobile):  
            raise ValueError('手机号码格式错误')
        return mobile
