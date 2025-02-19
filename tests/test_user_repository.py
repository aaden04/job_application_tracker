from lib.user_repository import UserRepository
from lib.user import User

def test_user_repository_gets_all_records(db_connection):
    db_connection.seed("seeds/Jobs.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert len(users) == 1
    assert users[0].name == "John"
    assert users[0].email == "john@gmail.com"

def test_create_user(db_connection):
    db_connection.seed("seeds/Jobs.sql")
    repository = UserRepository(db_connection)
    repository.create("Bobby", "bobby@gmail.com", "qwerty123")
    result = repository.all()
    assert len(result) == 2
    new_user = result[-1]
    assert new_user.name == "Bobby"
    assert new_user.email == "bobby@gmail.com"


def test_get_user(db_connection):
    db_connection.seed("seeds/Jobs.sql")
    repository = UserRepository(db_connection)
    user = repository.get_user(1)
    assert user['name'] == "John"
    assert user['email'] == "john@gmail.com"

def test_update_user(db_connection):
    db_connection.seed("seeds/Jobs.sql")
    repository = UserRepository(db_connection)
    repository.update_user(1, "Updated John", "updated.john@gmail.com")
    updated_user = repository.get_user(1)
    assert updated_user['name'] == "Updated John"
    assert updated_user['email'] == "updated.john@gmail.com"

def test_delete_user(db_connection):
    db_connection.seed("seeds/Jobs.sql")
    repository = UserRepository(db_connection)
    initial_count = len(repository.all())
    repository.delete_user(1)
    assert len(repository.all()) == initial_count - 1