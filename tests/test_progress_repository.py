from lib.progress import Progress
from lib.progress_repository import ProgressRepository
from datetime import datetime

class TestProgressRepository:
    def test_find_user_applications(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ProgressRepository(db_connection)
        result = repository.find_user_application(1)
        
        expected_date = datetime.strptime("2023-01-01", "%Y-%m-%d").date()
        expected = [Progress(1, "Applied", expected_date, "Accepted", 1)]
        
        assert result == expected

    def test_add_progress(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ProgressRepository(db_connection)
        
        date_applied = datetime.strptime("2023-12-01", "%Y-%m-%d").date()
        repository.add_progress("Google", "Software Engineer", "London", "£80000", date_applied, 1)
        
        result = repository.find_user_application(1)
        assert len(result) > 0     