#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import enum
from sqlalchemy import (
    Boolean,
    Column,
    Enum,
    ForeignKey,
    Integer,
    SmallInteger,
    String,
    Float,
    Table,
    Text,
    Date,
    DateTime,
    func,
    Index
)
from sqlalchemy.orm import relationship, backref

from models.abstract import Base, BaseModel


user_collection_rel = Table(
    "user_collection_rel",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id"), primary_key=True, doc="用户id"),
    Column("news_id", Integer, ForeignKey("news.id"), primary_key=True, doc="新闻id"),
    Column("create_time", DateTime, default=func.now(), doc="收藏创建时间")
)

user_follower_rel = Table(
    "user_follower_rel",
    Base.metadata,
    Column('follower_id', Integer, ForeignKey('users.id'), primary_key=True, doc="粉丝id"),
    Column('followed_id', Integer, ForeignKey('users.id'), primary_key=True, doc="被关注人的id"),
    Column("create_time", DateTime, default=func.now(), doc="创建时间")
)


class Users(BaseModel):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(32), unique=True, nullable=False, doc="用户名")
    password = Column(String(255), nullable=False, doc="非明文密码")
    mobile = Column(String(11), unique=True, nullable=False)
    email = Column(String(32), unique=True)
    avatar_url = Column(String(256), doc="用户头像")
    gender = Column(SmallInteger, default=0, doc="性别，0：未透露性别，1：男性，2：女性")
    is_active = Column(Boolean, default=True, doc="有效用户")
    is_admin = Column(Boolean, default=False, doc="管理员")
    last_login = Column(DateTime, onupdate=func.now(), doc="最近登录时间")
    news = relationship('News', backref='users', lazy='dynamic')     # 当前用户所发布的新闻
    collection_news = relationship("News", secondary=user_collection_rel, lazy="dynamic")  # 当前用户收藏的所有新闻lazy="dynamic"
    followers = relationship('Users',
                                secondary=user_follower_rel,
                                primaryjoin=id == user_follower_rel.c.followed_id,
                                secondaryjoin=id == user_follower_rel.c.follower_id,
                                backref=backref('followed', lazy='dynamic'),
                                lazy='dynamic')     # 用户所有的粉丝，添加了反向引用followed，代表用户都关注了哪些人

    def __repr__(self) -> str:
        return f"User(id={self.id!r})"


class Category(BaseModel):
    """新闻分类"""
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(8), nullable=False, doc="分类名")
    news = relationship('News', backref='category', lazy='dynamic')

    async def get_info(self):
        return {
            "id": self.id,
            "name": self.name
        }
        


class News(BaseModel):
    """新闻"""
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(64), nullable=False, doc="新闻标题")
    source = Column(String(16), nullable=False, doc="新闻来源")
    digest = Column(String(32), nullable=False, doc="新闻摘要")
    content = Column(Text, nullable=False, doc="新闻内容")
    pageviews = Column(Integer, default=0, doc="浏览量")
    image_url = Column(String(256), doc="新闻列表图片路径")
    category_id = Column(Integer, ForeignKey("category.id"), doc="新闻所属的类别id")
    user_id = Column(Integer, ForeignKey("users.id"), doc="当前新闻的作者id")
    status = Column(SmallInteger, default=0, doc="当前新闻状态。如果为1代表审核通过，0代表审核中，-1代表审核不通过")
    reason = Column(String(256), doc="未通过原因，status = -1 的时候使用")
    comments = relationship("Comment", lazy="dynamic")  # 当前新闻的所有评论


class Comment(BaseModel):
    """评论"""
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, doc="用户id")
    news_id = Column(Integer, ForeignKey("news.id"), nullable=False, doc="新闻id")
    content = Column(Text, nullable=False, doc="评论内容")
    parent_id = Column(Integer, ForeignKey("comment.id"), doc="父评论id")
    parent = relationship("Comment", remote_side=[id])  # 自关联，父id
    up_count = Column(Integer, default=0, doc="点赞条数")


class CommentUp(BaseModel):
    """评论点赞"""
    __tablename__ = "comment_user_up_rel"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    comment_id = Column("comment_id", Integer, ForeignKey("comment.id"), primary_key=True, doc="评论id")
    user_id = Column("user_id", Integer, ForeignKey("users.id"), primary_key=True, doc="用户id")
