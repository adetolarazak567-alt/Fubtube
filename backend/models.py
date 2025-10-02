from sqlalchemy import Column, String, Integer, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)   # you can use UUID strings
    username = Column(String, unique=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Video(Base):
    __tablename__ = "videos"
    id = Column(String, primary_key=True)  # generate UUID client or server
    title = Column(String)
    description = Column(Text)
    s3_key = Column(String, nullable=False)   # key in S3
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    views = Column(Integer, default=0)

class Like(Base):
    __tablename__ = "likes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    video_id = Column(String, ForeignKey("videos.id", ondelete="CASCADE"))
    user_id = Column(String, ForeignKey("users.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    video_id = Column(String, ForeignKey("videos.id", ondelete="CASCADE"))
    user_id = Column(String, nullable=True)
    text = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class View(Base):
    __tablename__ = "views"
    id = Column(Integer, primary_key=True, autoincrement=True)
    video_id = Column(String, ForeignKey("videos.id", ondelete="CASCADE"))
    user_id = Column(String, nullable=True)
    bytes = Column(Integer, nullable=True)
    duration = Column(Integer, nullable=True)  # seconds watched
    created_at = Column(DateTime(timezone=True), server_default=func.now())
