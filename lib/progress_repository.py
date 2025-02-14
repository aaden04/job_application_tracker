from lib.progress import Progress
from lib.database_connection import *

class ProgressRepository:
    def __init__(self, connection):
        self._connection = connection
    
 def find_user_application(self, application_id):
        result = self._connection.execute("SELECT * FROM progess WHERE application_id = %s", [application_id])
        return [ Applications(
            progess["applications_id"],
            progess["status"],
            progess["interview_date"],
            progess["decison"],
           
        ) for progess in result ]
 

