import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    ID = Column(Integer, primary_key=True)
    user_name = Column(String(30))
    first_name = Column(String(30))
    last_name = Column(String(30))
    email = Column(String(40))
    name = Column(String(250), nullable=False)

class Follower(Base):
    __tablename__ = 'Follower'
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('User.id'))
    user_to_id = Column(Integer, ForeignKey('User.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'Post'
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'Media'
    ID = Column(Integer, primary_key=True)
    type = Column(String(100))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('Post.id'))
    post = relationship(Post)

class Comment(Base):
    __tablename__ = 'Comment'
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(300))
    author_id = Column(Integer, ForeignKey('User.id'))
    post_id = Column(Integer, ForeignKey('Post.id'))
    post = relationship(Post)
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e