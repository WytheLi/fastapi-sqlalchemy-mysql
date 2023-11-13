from loguru import logger

from common.conf import settings



def configure_logger():
    logger.add(
        settings.LOG_PATH,
        level=settings.LOG_LEVEL,
        format=settings.LOG_FORMATTER,
        rotation='10 MB',   # 按照时间或文件大小进行轮换
        retention='15 days',    # 设置保留的日志文件数量
        compression='tar.gz',   # 对日志文件进行压缩以节省存储空间
        enqueue=True,   # 日志记录会异步进行，不会阻塞主程序
        backtrace=False,    # 日志中记录异常的堆栈跟踪信息
        diagnose=False,     # 日志中记录诊断信息
    )
    return logger


logger = configure_logger()
