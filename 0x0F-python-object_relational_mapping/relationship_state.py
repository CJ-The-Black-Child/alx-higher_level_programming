#!/usr/bin/python3
"""
Defines a State Model which in turn inherits from SQLAlchemy Base and
after that links to MySQL table name states.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL db.

    Attributes:
        id (str): The id of the state.
        name (sqlalchemy.Integer): The name of the state.
        cities (sqlalchemy.relationship): The relationship with City objects.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", cascade="all, delete-orphan", backref="state"
            )
