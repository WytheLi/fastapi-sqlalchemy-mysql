from typing import Any
from fastapi import status
from fastapi.responses import JSONResponse


async def response_success(code: int = 200, 
                           msg: str = "Request successful.", 
                           data: Any = None):
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "code": 200,
            "message": msg,
            "data": data
        }
    )


async def response_fail():
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "code": 0,
            "message": "Request unsuccessful."
        }
    )
