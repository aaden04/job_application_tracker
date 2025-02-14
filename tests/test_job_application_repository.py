from lib.job_application_repository import ApplicationsRepository
from lib.job_application import Application
from datetime import datetime

class TestApplicationsRepository:
    def test_add_application(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ApplicationsRepository(db_connection)
        repository.add_application("Netflix", "DevOps Engineer", "Remote", 120000, "2024-03-15")
        
        applications = repository.all_applications()
        assert applications[-1].company == "Netflix"
        assert applications[-1].title == "DevOps Engineer"

    def test_all_applications(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ApplicationsRepository(db_connection)
        applications = repository.all_applications()
    
        expected_date = datetime.strptime("2023-01-01", "%Y-%m-%d").date()
        assert applications[0] == Application(1, "Google", "Software Engineer", "London", 100000, expected_date)

    def test_delete_application(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ApplicationsRepository(db_connection)
        repository.delete_application(1)
        applications = repository.all_applications()
        
        assert len(applications) == 5

    def test_update_application(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ApplicationsRepository(db_connection)
    
        # Update the first application
        repository.update_application("Updated Company", "Updated Title", "Remote", 150000, "2024-03-15", 1)
    
        # Find the updated application directly
        updated_applications = repository.find_by_company_name("Updated Company")
        assert len(updated_applications) == 1
        assert updated_applications[0].company == "Updated Company"
        assert updated_applications[0].title == "Updated Title"
    def test_find_by_company_name(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ApplicationsRepository(db_connection)
        applications = repository.find_by_company_name("Google")
        
        assert len(applications) == 1
        assert applications[0].company == "Google"

    def test_find_by_job_title(self, db_connection):
        db_connection.seed("seeds/Jobs.sql")
        repository = ApplicationsRepository(db_connection)
        applications = repository.find_by_job_title("Software Engineer")
        
        assert len(applications) == 5
        assert all(app.title == "Software Engineer" for app in applications)
