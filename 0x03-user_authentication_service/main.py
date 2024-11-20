#!/usr/bin/env python3
"""
Main file to test DB functionality.
"""

from db import DB
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

# Initialize DB instance
my_db = DB()

# Add a user
user = my_db.add_user("test@test.com", "PwdHashed")
print(f"Added User ID: {user.id}")

# Find a user by email
try:
    found_user = my_db.find_user_by(email="test@test.com")
    print(f"Found User ID: {found_user.id}")
except NoResultFound:
    print("User not found")
except InvalidRequestError:
    print("Invalid query parameters")

# Attempt to find a non-existent user
try:
    my_db.find_user_by(email="notfound@test.com")
except NoResultFound:
    print("User not found")

# Attempt to find a user with invalid field
try:
    my_db.find_user_by(nonexistent_field="value")
except InvalidRequestError:
    print("Invalid query parameters")
