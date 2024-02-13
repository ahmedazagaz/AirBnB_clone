#!/usr/bin/python3
"""Defines the User class."""
from models.base_model import BaseModel
class User(BaseModel):
    """Represent a User.
    Attribute:
        Email: The email of the user.
        Password (str): The password of the user.
        First_name (str): The first name of the user.
        Last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
