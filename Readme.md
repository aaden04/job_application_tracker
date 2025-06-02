# Job Application Tracker

A web-based application built with Flask that helps users track their job applications, manage their profile, and monitor application progress.

## Features

- **User Authentication**: Secure login and signup functionality
- **Dashboard**: Overview of all job applications
- **Job Management**: Add, update, and delete job applications
- **Profile Management**: Update user profile information
- **Progress Tracking**: Monitor the status of job applications
- **Session Management**: Secure user sessions with logout functionality

## Tech Stack

- **Backend**: Python Flask
- **Database**: PostgreSQL/MySQL (configurable)
- **Frontend**: HTML templates with Jinja2
- **Authentication**: Session-based authentication
- **Environment Management**: python-dotenv

## Project Structure

```
job_application_tracker/
├── app.py                 # Main Flask application
├── lib/
│   ├── database_connection.py
│   ├── user_repository.py
│   ├── user.py
│   ├── job_application_repository.py
│   ├── job_application.py
│   ├── progress_repository.py
│   └── progress.py
├── frontend/
│   ├── templates/
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── dashboard.html
│   │   ├── myprofile.html
│   │   ├── add_jobs.html
│   │   └── view_progress.html
│   └── static/           # CSS, JS, images
├── .env                  # Environment variables
└── requirements.txt      # Python dependencies
```

## Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd job_application_tracker
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**
Create a `.env` file in the root directory:
```env
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-database-connection-string
```

5. **Set up the database**
Ensure your database is running and create the necessary tables:
- `users` table for user authentication
- `applications` table for job applications
- `progress` table for tracking application status

6. **Run the application**
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Usage

### Getting Started
1. **Sign Up**: Create a new account or log in with existing credentials
2. **Dashboard**: View all your job applications at a glance
3. **Add Jobs**: Submit new job applications with company details
4. **Manage Applications**: Edit or delete existing applications
5. **Track Progress**: Monitor the status of your applications

### Routes
- `/` - Login page
- `/signup` - User registration
- `/dashboard` - Main dashboard with application overview
- `/addjobs` - Add new job applications
- `/myprofile` - Manage profile and applications
- `/view_progress/<id>` - View progress for specific application
- `/logout` - End user session

## Database Schema

### Users Table
- `id` - Primary key
- `name` - User's full name
- `email` - User's email (unique)
- `password` - Hashed password

### Applications Table
- `id` - Primary key
- `company` - Company name
- `title` - Job title
- `location` - Job location
- `salary` - Expected/offered salary
- `date_applied` - Application date
- `user_id` - Foreign key to users table

### Progress Table
- `id` - Primary key
- `application_id` - Foreign key to applications table
- `status` - Current application status
- `notes` - Additional notes
- `updated_at` - Last update timestamp

## Security Features

- Password hashing for user authentication
- Session-based authentication
- CSRF protection through Flask's built-in features
- Environment variable management for sensitive data
- Input validation and sanitization

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Requirements

```txt
Flask==2.3.3
python-dotenv==1.0.0
psycopg2-binary==2.9.7  # For PostgreSQL
# or
PyMySQL==1.1.0          # For MySQL
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Flask secret key for sessions | Yes |
| `DATABASE_URL` | Database connection string | Yes |

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support or questions, please open an issue in the GitHub repository.


![Excalidraw Diagram](Job_Application_Tracker.png)





