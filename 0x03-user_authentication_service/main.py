#!/usr/bin/env python3
"""
Main file to test the User model and interact with the database.
"""

from db import DB
from user import User

# Initialize DB instance
my_db = DB()

# Add users and print their IDs
user_1 = my_db.add_user("test@test.com", "SuperHashedPwd")
print(f"User 1 ID: {user_1.id}")  # Output ID of the first user

user_2 = my_db.add_user("test1@test.com", "SuperHashedPwd1")
print(f"User 2 ID: {user_2.id}")  # Output ID of the second user
