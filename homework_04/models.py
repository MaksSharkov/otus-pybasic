"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey,
)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    scoped_session,
    Session as SessionType,
    relationship,
)
from mixins import (
    CreatedMixin,
    BaseMixin,
)

PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://makssh:derporol@localhost/homework_04"
)
DB_SYNC_URI = "postgresql+psycopg2://makssh:derporol@localhost/homework_04"
DB_ECHO = True

engine = create_engine(url=DB_SYNC_URI, echo=DB_ECHO)

async_engine = create_async_engine(
    url=PG_CONN_URI,
    echo=DB_ECHO,
)

async_session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

Session = async_session
Base = declarative_base(bind=engine)


class User(BaseMixin, CreatedMixin, Base):
    username = Column(String(50), unique=True)
    name = Column(String(50))
    email = Column(String(50))

    posts = relationship("Post", back_populates="user", uselist=True)


class Post(BaseMixin, CreatedMixin, Base):
    user_id = Column(Integer, ForeignKey("users.id"))
    title = Column(String)
    body = Column(String)

    user = relationship("User", back_populates="posts", uselist=False)


async def init_db():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
