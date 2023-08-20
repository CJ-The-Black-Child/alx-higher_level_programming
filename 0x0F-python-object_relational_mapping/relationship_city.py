#!/usr/bin/python3
"""
Defines a City model which inherits from SQLAlchemy Base and afterwards
links it to MySQL table name cities.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    """
    Represents a city for a MySQL database.

    Attributes:
        id (str): The id of the city.
        name (sqlalchemy.Integer): The name of the city.
        state_id (sqlalchemy.String): The state's id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
