#!/usr/bin/python3
"""
This module contains the class definition of a City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import State, Base


class City(Base):
    """
    define city class that links to city table in database

    Attributes:

    id(integer): represents a column of an auto-generated, unique integer,
    can’t be null and is a primary key
    name(CHAR): represents a column of a string with maximum
    128 characters and can’t be null
    state_id(Integer): represents a column of an integer, can’t be null
    and is a foreign key to states.id
    """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("States.id"), nullable=False)

    def __init__(self, name, state_id):
        """
        class constructor
        """
        self.name = name
        self.state_id = state_id
