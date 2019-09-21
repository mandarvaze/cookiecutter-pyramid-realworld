"""Models related to auth."""

from __future__ import annotations
from passlib.hash import argon2
from pyramid.request import Request
from pyramid_deferred_sqla import Base
from pyramid_deferred_sqla import Model
from pyramid_deferred_sqla import model_config
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import TypeDecorator
from sqlalchemy import Unicode
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql.psycopg2 import PGDialect_psycopg2
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import Session

import typing as t

__all__ = ["User"]


class LowerCaseString(TypeDecorator):
    """Converts strings to lower case on the way in."""

    impl = String

    def process_bind_param(self, value: str, dialect: PGDialect_psycopg2):
        return value.lower()


@model_config(Base)
class User(Model):
    """A logged-in user."""

    __tablename__ = "users"

    def __json__(self, request: Request) -> t.Dict[str, str]:
        """JSON renderer support."""
        return {
            "username": self.username,
            "email": self.email,
            "bio": self.bio,
            "token": request.create_jwt_token(str(self.id)),
            "image": self.image,
        }

    email = Column(LowerCaseString, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    password_hash = Column(String, nullable=False)
    bio = Column(Unicode)
    image = Column(String)

    @classmethod
    def by_id(cls: t.Type[User], uuid: str, db: Session) -> t.Optional[User]:
        """Get User by id."""
        q = db.query(cls)
        q = q.filter(cls.id == uuid)
        return q.one_or_none()

    @classmethod
    def by_username(cls: t.Type[User], username: str, db: Session) -> t.Optional[User]:
        """Get User by username."""
        q = db.query(cls)
        q = q.filter(cls.username == username)
        return q.one_or_none()

    @classmethod
    def by_email(cls: t.Type[User], email: str, db: Session) -> t.Optional[User]:
        """Get User by email."""
        q = db.query(cls)
        q = q.filter(cls.email == email)
        return q.one_or_none()

    def verify_password(self, password: str) -> bool:
        """Verify given password against the hash stored in db."""
        return argon2.verify(password, self.password_hash)
