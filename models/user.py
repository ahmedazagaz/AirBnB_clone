#!/usr/bin/python3
"""The User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a User.

    Attribut:
        email: The user email.
        password : The user password .
        first_name : The user first name .
        last_name : The user last name .
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
