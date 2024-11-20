#!/usr/bin/env python3
"""
Main file to test the User model and interact with the database.
"""

from user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup the database engine (for testing, use SQLite in-memory database)
engine = create_engine('sqlite:///:memory:', echo=True)

# Create all tables (create the users table in this case)
User.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Print the table name
print(User.__tablename__)

# Print column names and types
for column in User.__table__.columns:
    print("{}: {}".format(column, column.type))
