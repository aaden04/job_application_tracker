from lib.progress import Progress
from lib.database_connection import *

class ProgressRepository:
    def __init__(self, connection):
        self._connection = connection    

    def find_user_application(self, application_id):
        with self._connection.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM progress WHERE applications_id = %s", [application_id])
            result = cursor.fetchall()

        return [Progress(row[0], row[1], row[2], row[3], row[4]) for row in result]  
