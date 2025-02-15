class Application:
    def __init__(self, id, company, title, location, salary, date_applied, user_id):
        self.id = id
        self.company = company
        self.title = title
        self.location = location
        self.salary = salary
        self.date_applied = date_applied
        self.user_id = user_id  

    def __eq__(self, other):
        return (
            self.id == other.id and
            self.company == other.company and
            self.title == other.title and
            self.location == other.location and
            self.salary == other.salary and
            self.date_applied == other.date_applied and
            self.user_id == other.user_id
        )

    def __repr__(self):
        return f"Application(id={self.id}, company='{self.company}', title='{self.title}', location='{self.location}', salary={self.salary}, date_applied='{self.date_applied}', user_id={self.user_id})"
