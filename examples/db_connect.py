from sqlalchemy.orm import DeclarativeBase, sessionmaker, relationship
from sqlalchemy import create_engine, mapped_column, Mapped, ForeignKey
from typing import List


class Base(DeclarativeBase):
    pass


engine = create_engine("sqlite:///demo.db", echo=True)


class TikTokUsers(Base):
    __tablename__ = "tiktok_users"
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    subscribers: Mapped[int] = mapped_column(default=0)
    videos: Mapped[List["Video"]] = relationship(
        "Video", back_populates="author")


class Video(Base):
    __tablename__ = "videos"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    views: Mapped[int] = mapped_column(default=0)
    creator_id: Mapped[int] = mapped_column(ForeignKey("tiktok_users.id"))
    author: Mapped["TikTokUsers"] = relationship(
        "TikTokUsers", back_populates="videos")


# Создаем таблицы
Base.metadata.create_all(engine)

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()
