import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy.orm import relationship

Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    """Person representation"""

    __tablename__ = "person"
    _id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String)
    last_name = sqlalchemy.Column(sqlalchemy.String)
    user_name = sqlalchemy.Column(sqlalchemy.String, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String)
    person_email = relationship("Email", backref="person_email")

    def __repr__(self):
        """Get representation"""
        return "<Person: %s %s>" % (self.first_name, self.last_name)


class Email(Base):
    """Email representation."""

    __tablename__ = "email"
    _id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    email = sqlalchemy.Column(sqlalchemy.String)
    person_id = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey("person._id"),
                                  nullable=False, unique=True)

