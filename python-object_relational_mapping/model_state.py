#!/usr/bin/python3
"""
Python file that contains the class definition of a State and
an instance Base = declarative_base().
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """
    State class that creates a table.
    """
    __tablename__ = 'states'

    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
