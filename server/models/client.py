""" Module implementing the Client model. """
from .db import db
from .base import BaseModel


class Client(BaseModel):
    """
    Represents client database information.
    """
    username = db.Column(db.String(60), unique=True, nullable=False)
    avatar_url = db.Column(db.String(250), nullable=False)
    # Relationships
    requests = db.relationship('Request', back_populates='client')
