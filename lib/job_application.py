class Application:

    def __init__(self, id, comapny, title, location, salary, date_applied,):
        self.id = id
        self.company = comapny
        self.title = title
        self.location = location
        self.salary = salary
        self.date_applied = date_applied

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"This is application no. ({self.id} at {self.company} for a {self.title}. 
        This role is in, {self.location} and the salary is {self.salary}. 
        This application was submitted on {self.date_applied})"
    