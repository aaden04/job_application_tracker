from lib.progress import Progress
from lib.progress_repository import ProgressRepository
from datetime import datetime    # Convert the date string to a datetime.date object

class TestProgressRepository:
    def test_find__user_applications(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ProgressRepository(db_connection, applications_id=1)
        result = repository.find_user_application(1)
        
       
        from datetime import datetime
        expected_date = datetime.strptime("2023-01-01", "%Y-%m-%d").date()
        expected = [Progress(1, "Applied", expected_date, "Accepted", 1)]
        
        assert result == expected
        print(expected)