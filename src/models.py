import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(String(8), nullable=False)

class UserFavorites(Base):
    __tablename__ = 'user_favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship(User)
    character = relationship('Character')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    status = Column(String(80))
    species = Column(String(80))
    character_type = Column(String(80))
    gender = Column(String(80))
    image = Column(String(150))
    
class Episode(Base):
    __tablename__='episode'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    air_date = Column(String(80))
    episode_number = Column(String(80))

class CharacterEpisode(Base):
    __tablename__='character_episode'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer,  ForeignKey('character.id'))
    episode_id = Column(Integer, ForeignKey('episode.id'))
    character = relationship(Character)
    episode = relationship(Episode)
    
    def to_dict(self):
        return {}

render_er(Base, 'diagram.png')