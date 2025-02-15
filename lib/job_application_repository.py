class ApplicationsRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_user_applications(self, user_id):
        with self._connection.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM applications WHERE user_id = %s", [user_id])
            return cursor.fetchall()

    def add_application(self, company, title, location, salary, date_applied, user_id):
        with self._connection.connection.cursor() as cursor:
            cursor.execute(
            "INSERT INTO applications (company, title, location, salary, date_applied, user_id) VALUES (%s, %s, %s, %s, %s, %s)",
            [company, title, location, salary, date_applied, user_id]
        )
        self._connection.connection.commit()  # <-- Ensure commit is on actual connection


    def delete_application(self, application_id, user_id):
        with self._connection.connection.cursor() as cursor:
            cursor.execute("DELETE FROM applications WHERE id = %s AND user_id = %s", [application_id, user_id])

    def update_application(self, company, title, location, salary, date_applied, application_id, user_id):
        with self._connection.connection.cursor() as cursor:
            cursor.execute(
                "UPDATE applications SET company = %s, title = %s, location = %s, salary = %s, date_applied = %s WHERE id = %s AND user_id = %s",
                [company, title, location, salary, date_applied, application_id, user_id]
            )
