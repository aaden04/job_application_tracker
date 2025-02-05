from lib.job_application import *


class ApplicationsRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def add_application(self, application):
        self._connection.execute(
            'INSERT INTO applications (company, title, location, salary, date_applied) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
            [
                application.company,
                application.title,
                application.location,
                application.salary,
                application.date_applied,
            ]
        )
        return None
    
    def all_applications(self):
        rows = self._connection.execute('SELECT * FROM applications')
        applications = []
        for row in rows:
            item = Applications(row['id'], row['company'], row['title'], row['location'], row['salary'], row['date_applied'])
            applications.append(item)
        return applications
    
    def delete_application(self, id):
        self._connection.execute(
            'DELETE FROM applications WHERE id = %s',
            [id]
        )
        return None
    
    def update_application(self, application):
        self._connection.execute(
            'UPDATE applications SET company = %s, title = %s, location = %s, salary = %s, date_applied = %s',
            [
                application.company,
                application.title,
                application.location,
                application.salary,
                application.date_applied,
            ]
        )
        return None
    
    def find_by_company_name(self, company):
        rows = self._connection.execute(
            'SELECT * FROM applications WHERE company = %s',
            [company]
        )
        applications = []
        for row in rows:
            item = Applications(row['id'], row['company'], row['title'], row['location'], row['salary'])
            applications.append(item)
        return applications
    
    def find_by_job_title(self, title):
        rows = self._connection.execute(
            'SELECT * FROM applications WHERE title = %s',
            [title]
        )
        applications = []
        for row in rows:
            item = Applications(row['id'], row['company'], row['title'], row['location'], row['salary'])
            applications.append(item)
        return applications
    

        
    
    
    
    

    

