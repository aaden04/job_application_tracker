from lib.progress import Progress
from lib.database_connection import *

class ProgressRepository:
    def __init__(self, connection, applications_id=None):
        self.applications_id = applications_id
        self._connection = connection    
    def find_user_application(self, application_id):
        result = self._connection.execute("SELECT * FROM progress WHERE applications_id = %s", [application_id])
        return [ Progress(
            progess["applications_id"],
            progess["status"],
            progess["interview_date"],
            progess["decison"],
           
        ) for progess in result ]
 

