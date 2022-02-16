import sqlalchemy

from model import Base, Person, Email

def main():
    """Run Main function."""
    db_connection = database_connections("sqlite:///kek.db")
    session_factory = session_creation(db_connection)
    with session_factory() as session:
        new_person = Person(first_name="Simon", last_name="Retter",
                            user_name="pastperfekt", password="kekw")
        session.add(new_person)
        session.commit()
    with session_factory() as session:
        for tmp_person in session.execute(sqlalchemy.select(Person)):
            old_person = tmp_person[0]
            new_email = Email(email="ASDF@wonderland.net",
                              person_id=old_person._id)
            session.add(new_email)
            session.commit()
            break

def database_connections(database_url):
    """Connect to database."""
    return sqlalchemy.create_engine(database_url)


def session_creation(db_connection):
    """Create session factory."""
    Base.metadata.create_all(db_connection)
    session_factory = sqlalchemy.orm.sessionmaker()
    session_factory.configure(bind=db_connection)
    return session_factory


if __name__ == "__main__":
    main()

