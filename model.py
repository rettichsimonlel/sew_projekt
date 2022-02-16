import sqlalchemy
import sqlalchemy.ext.declarative
from sqlalchemy.orm import relationship

Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    """Person representation"""

    __tablename__ = "person"
    person_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String)
    last_name = sqlalchemy.Column(sqlalchemy.String)
    user_name = sqlalchemy.Column(sqlalchemy.String)
    password = sqlalchemy.Column(sqlalchemy.String)
    email = relationship("Email", backref="Email")

    def __repr__(self):
        """Get representation"""
        return "<Person: %s %s>" % (self.first_name, self.last_name)


class Email(Base):
    """Email representation."""

    __tablename__ = "email"
    email_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    email = sqlalchemy.Column(sqlalchemy.String)
    person_id = sqlalchemy.Column(sqlalchemy.Integer,
                                  sqlalchemy.ForeignKey("person.person_id"),
                                  nullable=False))

