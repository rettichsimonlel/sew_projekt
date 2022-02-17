import sqlalchemy

from model import Base, Person, Email

def test_register(session_factory):
    _user_name = input("User name: ")
    _password = input("Password: ")
    _first_name = input("First Name: ")
    _last_name = input("Last Name: ")
    _email = input("Email: ")
    with session_factory() as session:
        new_person = Person(first_name=_first_name, last_name=_last_name,
                            user_name=_user_name, password=_password)
        session.add(new_person)
        session.expire_on_commit = False
        session.commit()
    with session_factory() as session:
        new_email = Email(email=_email,
                        person_id=new_person._id)
        session.add(new_email)
        session.expire_on_commit = True
        session.commit()

def test_login(session_factory):
    _user_name = input("User name: ")
    _password = input("Password: ")
    ye = False

    with session_factory() as session:
        table = Base.__subclasses__()
        for t in table:
            rows = session.query(t)
            for r in rows:
                try:
                    if r.user_name == _user_name and r.password == _password:
                        print("Ye")
                        ye = True
                except:
                    pass

    if ye == False:
        print("No no no")

def main():
    """Run Main function."""
    db_connection = database_connections("sqlite:///kek.db")
    session_factory = session_creation(db_connection)
    _answer = int(input("1: register; 2: login; ::"))
    if _answer == 1:
        test_register(session_factory)
    elif _answer == 2:
        test_login(session_factory)

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
