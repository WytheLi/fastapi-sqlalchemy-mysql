#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 14:17
# @SoftWare: PyCharm
import uvicorn
from fastapi import FastAPI, APIRouter
from fastapi.logger import logger

from common.conf import settings
from common.register import create_app
from db.engine import async_engine
from models.base import Base


app = create_app()


if __name__ == '__main__':
    try:
        logger.info(
            """\n
 /$$$$$$$$                   /$$      /$$$$$$  /$$$$$$$  /$$$$$$
| $$_____/                  | $$     /$$__  $$| $$__  $$|_  $$_/
| $$    /$$$$$$   /$$$$$$$ /$$$$$$  | $$  | $$| $$  | $$  | $$  
| $$$$$|____  $$ /$$_____/|_  $$_/  | $$$$$$$$| $$$$$$$/  | $$  
| $$__/ /$$$$$$$|  $$$$$$   | $$    | $$__  $$| $$____/   | $$  
| $$   /$$__  $$ |____  $$  | $$ /$$| $$  | $$| $$        | $$  
| $$  |  $$$$$$$ /$$$$$$$/  |  $$$$/| $$  | $$| $$       /$$$$$$
|__/   |_______/|_______/    |___/  |__/  |__/|__/      |______/

            """
        )
        uvicorn.run('manage:app', host=settings.UVICORN_HOST, port=settings.UVICORN_PORT, reload=False, workers=1)  # TEST
        # uvicorn.run('main:app', host='0.0.0.0', port=8085, reload=True, workers=4)
    except Exception as e:
        logger.error(f'❌ FastAPI start filed: {e}')
