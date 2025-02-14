from lib.job_application import Application

class TestApplication:
    def test_application_constructs(self):
        application = Application(1, "Google", "Software Engineer", "London", 100000, "2023-01-01")
        assert application.id == 1
        assert application.company == "Google"
        assert application.title == "Software Engineer"
        assert application.location == "London"
        assert application.salary == 100000
        assert application.date_applied == "2023-01-01"

    def test_applications_format_nicely(self):
        application = Application(1, "Google", "Software Engineer", "London", 100000, "2023-01-01")
        assert str(application) == "This is application no. 1 at Google for a Software Engineer. This role is in London and the salary is 100000. This application was submitted on 2023-01-01"
    
    def test_applications_are_equal(self):
        application1 = Application(1, "Google", "Software Engineer", "London", 100000, "2023-01-01")
        application2 = Application(1, "Google", "Software Engineer", "London", 100000, "2023-01-01")
        assert application1 == application2
