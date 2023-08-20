#!/usr/bin/python3
"""
Definition of the state class and Base instance

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):

    """
    State class that links to the MySQL table states

    Represents a state for a MySQL database.

    Attributes:
    __table__ (str): The name of the MySQL table to store States.
    id (sqlalchemy.Integer): The state's id.
    name (sqlalchemy.string): The state's name.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
