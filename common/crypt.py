from passlib.context import CryptContext
from asgiref.sync import sync_to_async  # 将同步函数转化成异步函数


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@sync_to_async
def get_hash_password(password: str) -> str:
    """
    使用hash算法加密密码

    :param password: 密码
    :return: 加密后的密码
    """
    return pwd_context.hash(password)


@sync_to_async
def password_verify(password: str, hashed_password: str) -> bool:
    """
    密码校验

    :param password: 要验证的密码
    :param hashed_password: 要比较的hash密码
    :return bool: 密码校验的结果 
    """
    return pwd_context.verify(password, hashed_password)
