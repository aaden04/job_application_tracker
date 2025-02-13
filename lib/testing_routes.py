from lib.database_connection import *
import hashlib
from lib.user import *
from lib.user_repository import *

# Create an instance of DatabaseConnection
db_connection = DatabaseConnection()

# Create an instance of UserRepository
user_repo = UserRepository(db_connection)

# Test create function
user_repo.create("Test User", "testuser@example.com", "password123")

# Verify the user is in the database by checking manually or using the 'all' function