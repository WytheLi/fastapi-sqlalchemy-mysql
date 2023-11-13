#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @DateTime: 2023/10/17 14:17
# @SoftWare: PyCharm
import uvicorn
from fastapi.logger import logger

from common.conf import settings
from common.register import create_app


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
        # uvicorn.run('manage:app', host=settings.UVICORN_HOST, port=settings.UVICORN_PORT, reload=False, workers=1)
        uvicorn.run('manage:app', host='0.0.0.0', port=8080, reload=False, workers=1)  # TEST
    except Exception as e:
        logger.error(f'❌ FastAPI start filed: {e}')
