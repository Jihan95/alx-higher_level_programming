#!/usr/bin/python3
"""
This modulecontains the class definition of a State
and an instance Base = declarative_base.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """
    define state class that links to state table in database

    Attributes:

    id(integer): represents a column of an auto-generated, unique integer,
    can’t be null and is a primary key
    name(CHAR): represents a column of a string with maximum
    128 characters and can’t be null
    """
    __tablename__ = "states"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __int__(self, name):
        """
        constructor for State class
        """
        self.name = name
