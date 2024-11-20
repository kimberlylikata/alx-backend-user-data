#!/usr/bin/env python3
"""
Module for the User class model to interact with the users table.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    """
    The User class defines the mapping between the User object and the 'users' table in the database.
    
    Attributes:
        id (int): The unique identifier of the user (Primary Key).
        email (str): The email address of the user.
        hashed_password (str): The hashed password for authentication.
        session_id (str): The session identifier for user login.
        reset_token (str): The reset token used for password reset.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
