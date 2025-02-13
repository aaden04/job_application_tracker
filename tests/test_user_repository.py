
from lib.user_repository import UserRepository
from lib.user import User

def test_user_repository_gets_all_records(db_connection):
    db_connection.seed("seeds/Jobs.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert len(users) == 6
    assert users[0].name == "John"
    assert users[0].email == "john@gmail.com"

def test_create_user(db_connection):
    db_connection.seed("seeds/Jobs.sql")
    repository = UserRepository(db_connection)

    repository.create("Bobby", "bobby@gmail.com", "qwerty123")
    
    result = repository.all()
    assert len(result) == 7
    new_user = result[-1]
    
    assert new_user.name == "Bobby"
    assert new_user.email == "bobby@gmail.com"
    assert new_user.password == "qwerty123"
