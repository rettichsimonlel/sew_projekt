import sqlalchemy

from model import Base, Person

def main():
    """Run Main function."""
    db_connection = database_connections("sqlite:///kek.db")
    session_factory = session_creation(db_connection)

    # add something to the table
    with session_factory() as session:
        for i in range(2):
            new_person = Person(first_name="Simon", last_name="Retter",
                                user_name="pastperfekt", password="kekw",
                                email="simon.kek@lel.com")
            session.add(new_person)
            session.commit()


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

