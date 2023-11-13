### fastapi结合sqlalchemy 2.x开发的一个异步Web Service应用
- python3.9
- fastapi
- sqlalchemy 2.x


> 参考项目：https://gitee.com/wu_cl/fastapi_sqlalchemy_mysql
> 由于以上项目没有定义关联模型（一对多、多对多模型的定义以及操作）、sqlalchemy异步事务等，这里补充


### 文献参考
1. https://gitee.com/wu_cl/fastapi_sqlalchemy_mysql
2. ImportError: cannot import name 'field_validator' from 'pydantic'. (pydantic包版本太低导致。升级pydantic包`pip install --upgrade pydantic -i https://pypi.douban.com/simple`)
2. pydantic.errors.PydanticImportError: `BaseSettings` has been moved to the `pydantic-settings` package. See https://docs.pydantic.dev/2.4/migration/#basesettings-has-moved-to-pydantic-settings for more details. （升级pydantic包版本导致。BaseSettings设置类 已移至单独的包 pydantic-settings）

