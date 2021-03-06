""" Module for flask application configuration. """
from .env import (
    SECRET_KEY, SQLALCHEMY_DATABASE_URI_TESTING, SQLALCHEMY_DATABASE_URI
)


def apply_configuration(app, test_env=False):
    """
    Adds configuration values to flask app.

    Args:
        app(Flask): flask application.
    """

    database_uri = (
        SQLALCHEMY_DATABASE_URI_TESTING
        if test_env else SQLALCHEMY_DATABASE_URI
    )

    # Secret key fro various stuff
    app.config['SECRET_KEY'] = SECRET_KEY

    # Set TESTING env var
    app.config['TESTING'] = test_env

    # The postgres database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

    # A deprecated SQLAlchemy feature that needs to be turned off
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Prevents flask restful from appending message to 404 response
    app.config['ERROR_404_HELP'] = False
