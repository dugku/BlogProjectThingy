from sqlalchemy import Column, Integer, String, Boolean, DateTime, func, Text

from databases import Base

class Post(Base):
    __tablename__ = 'myPost'

    postId = Column(Integer, primary_key=True)
    Post = Column(Text)
    DatePosted = Column(DateTime, server_default=func.now())
    Author = Column(String)
    Title = Column(String)
    Likes = Column(Integer, default=0)
    Dislike = Column(Integer, default=0)