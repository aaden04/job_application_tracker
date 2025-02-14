
from lib.progress_repository import ProgressRepository

class TestProgressRepository:

    def test_find__user_applications(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ProgressRepository(db_connection)
        
        result = repository.find(1)
        assert result == Progress(1, "Applied", "2023-01-01", "Accepted", 1)
    

