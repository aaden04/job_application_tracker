from lib.job_application_repository import ApplicationsRepository
from datetime import datetime

class TestApplicationsRepository:
    def test_add_application(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ApplicationsRepository(db_connection)
        repository.add_application(
            "Netflix", 
            "DevOps Engineer", 
            "Remote", 
            120000, 
            "2024-03-15",
            1  # Added user_id parameter
        )
        
        applications = repository.get_user_applications(1)
        assert applications[-1]["company"] == "Netflix"
        assert applications[-1]["title"] == "DevOps Engineer"

    def test_get_user_applications(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ApplicationsRepository(db_connection)
        applications = repository.get_user_applications(1)
    
        expected_date = datetime.strptime("2023-01-01", "%Y-%m-%d").date()
        assert applications[0]["company"] == "Google"
        assert applications[0]["title"] == "Software Engineer"

    def test_delete_application(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ApplicationsRepository(db_connection)
        
        # Get initial count
        initial_applications = repository.get_user_applications(1)
        initial_count = len(initial_applications)
        
        # Delete an application
        repository.delete_application(1, 1)
        
        # Get new count
        remaining_applications = repository.get_user_applications(1)
        
        # Assert we have one less application
        assert len(remaining_applications) == initial_count - 1

    def test_update_application(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ApplicationsRepository(db_connection)
    
        repository.update_application(
            "Updated Company", 
            "Updated Title", 
            "Remote", 
            150000, 
            "2024-03-15",
            1, 
            1,
        )
    
        applications = repository.get_user_applications(1)
        updated_app = next((app for app in applications if app["company"] == "Updated Company"), None)
        assert updated_app is not None
        assert updated_app["title"] == "Updated Title"

    def test_find_by_company_name(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ApplicationsRepository(db_connection)
        applications = repository.find_by_company_name("Google", 1)
    
        assert len(applications) == 1
        assert applications[0]["company"] == "Google"

    def test_find_by_job_title(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ApplicationsRepository(db_connection)
        applications = repository.find_by_job_title("Software Engineer", 1)
    
        assert len(applications) > 0
        assert all(app["title"] == "Software Engineer" for app in applications)