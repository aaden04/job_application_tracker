from lib.job_application import Application

class TestApplication:
    def test_application_constructs(self):
        application = Application(1, "Google", "Software Engineer", "London", 100000, "2023-01-01", 1)
        assert application.id == 1
        assert application.company == "Google"
        assert application.title == "Software Engineer"
        assert application.location == "London"
        assert application.salary == 100000
        assert application.date_applied == "2023-01-01"
        assert application.user_id == 1

    def test_applications_format_nicely(self):
        application = Application(1, "Google", "Software Engineer", "London", 100000, "2023-01-01", 1)
        expected = "Application(id=1, company='Google', title='Software Engineer', location='London', salary=100000, date_applied='2023-01-01', user_id=1)"
        assert str(application) == expected
    
    def test_applications_are_equal(self):
        application1 = Application(1, "Google", "Software Engineer", "London", 100000, "2023-01-01", 1)
        application2 = Application(1, "Google", "Software Engineer", "London", 100000, "2023-01-01", 1)
        assert application1 == application2