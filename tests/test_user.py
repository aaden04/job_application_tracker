from lib.user import User

class TestUser:
    def test_user_constructs(self):
        user = User(1, "John", "john@gmail.com", "password123")
        assert user.id == 1
        assert user.name == "John"
        assert user.email == "john@gmail.com"
        assert user.password == "password123"
    def test_users_format_nicely(self):
          user = User(1, "John", "john@gmail.com", "password123")
          expected = "User(id=1, name='John', email='john@gmail.com')"
          assert str(user) == expected
    def test_users_are_equal(self):
        user1 = User(1, "John", "john@gmail.com", "password123")
        user2 = User(1, "John", "john@gmail.com", "password123")
        assert user1 == user2
