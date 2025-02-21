from lib.progress import Progress
from lib.database_connection import *

class ProgressRepository:
    def __init__(self, connection):
        self._connection = connection    

    def find_user_application(self, application_id):
        with self._connection.connection.cursor() as cursor:
            cursor.execute("""
                SELECT p.id, p.status, p.date, p.outcome, p.applications_id 
                FROM progress p
                WHERE p.applications_id = %s
            """, [application_id])
            result = cursor.fetchall()
        return [Progress(row[0], row[1], row[2], row[3], row[4]) for row in result]

    def add_progress(self, company, title, location, salary, date_applied, user_id):
        with self._connection.connection.cursor() as cursor:
            cursor.execute("""
                INSERT INTO applications (company, title, location, salary, date_applied, user_id) 
                VALUES (%s, %s, %s, %s, %s, %s) RETURNING id
            """, [company, title, location, salary, date_applied, user_id])
            application_id = cursor.fetchone()[0]
            cursor.execute("""
                INSERT INTO progress (status, date, outcome, applications_id)
                VALUES ('Applied', %s, 'Pending', %s)
            """, [date_applied, application_id])
            self._connection.connection.commit()