from lib.user_repository import UserRepository
from lib.user import User

def test_user_repository_gets_all_records(db_connection):
    db_connection.seed("seeds/Jobs.sql")
    repository = UserRepository(db_connection)
    users = repository.all()
    assert len(users) == 5
    first_user = users[0]
    assert first_user.id == 1
    assert first_user.name == "John"
    assert first_user.email == "john@gmail.com"
    assert first_user.password == "password"

def test_create_user(db_connection):
    db_connection.seed("seeds/Jobs.sql")
    repository = UserRepository(db_connection)
    repository.create("Bobby", "bobby@gmail.com", "password")
    users = repository.all()
    assert len(users) == 6
    new_user = users[-1]
    assert new_user.name == "Bobby"
    assert new_user.email == "bobby@gmail.com"

def test_check_password_success(db_connection):
    db_connection.seed("seeds/Jobs.sql")
    repository = UserRepository(db_connection)
    result = repository.check_password("john@gmail.com", "password")
    assert result == True

def test_check_password_failure(db_connection):
    db_connection.seed("seeds/Jobs.sql")
    repository = UserRepository(db_connection)
    result = repository.check_password("john@gmail.com", "wrongpassword")
    assert result == False

def test_find_by_email_exists(db_connection):
    db_connection.seed("seeds/Jobs.sql")
    repository = UserRepository(db_connection)
    user = repository.find_by_email("john@gmail.com")
    assert user.name == "John"
    assert user.email == "john@gmail.com"

def test_find_by_email_not_found(db_connection):
    db_connection.seed("seeds/Jobs.sql")
    repository = UserRepository(db_connection)
    user = repository.find_by_email("nonexistent@gmail.com")
    assert user is None

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


