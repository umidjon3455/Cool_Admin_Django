# University Management System

A Django-based web application for managing university administrative data including faculties, departments, teachers, subjects, groups, and students.

## 📋 Project Overview

This system provides a comprehensive solution for university administration with the following main features:
- Faculty and department management
- Teacher and staff management
- Subject and course management
- Student group management
- Student enrollment and records

## 🚀 Technologies Used

- **Backend**: Django 5.2.14
- **Database**: SQLite (development), PostgreSQL (production ready)
- **Frontend**: Django Templates with HTML, CSS, JavaScript
- **Additional**: Django Humanize for better data presentation

## 📁 Project Structure

```
PythonProject3/
├── adminapp/                 # Main application
│   ├── models.py            # Database models
│   ├── views.py             # View logic
│   ├── forms.py             # Django forms
│   ├── urls.py              # URL patterns
│   └── ...
├── config/                  # Project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   └── ...
├── templates/               # HTML templates
│   ├── sidebar.html
│   └── student/
│       ├── form.html
│       └── list.html
├── static/                  # Static files (CSS, JS, images)
├── db.sqlite3              # SQLite database (development)
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🗄️ Database Models

The system includes the following main models:

### **Faculty**
- University faculties
- Fields: name

### **Kafedra (Department)**
- Academic departments
- Fields: name, faculty (ForeignKey)

### **Teacher**
- Teacher information
- Fields: first_name, last_name, email, phone, kafedra, hire_date

### **Subject**
- Course subjects
- Fields: name, code, credits, kafedra, description

### **Group**
- Student groups
- Fields: name, faculty, created_year, is_active

### **Student**
- Student records
- Fields: first_name, last_name, email, phone, birth_date, group, enrollment_date, student_id

## 🛠️ Installation and Setup

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd PythonProject3
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Main application: http://127.0.0.1:8000/
   - Admin panel: http://127.0.0.1:8000/admin/

## 📊 Database Configuration

### Development (SQLite)
The project comes pre-configured with SQLite for development.

### Production (PostgreSQL)
To use PostgreSQL in production, update the `DATABASES` setting in `config/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'univercity_db',
        'USER': 'admin',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '5433',
    }
}
```

## 🔧 Configuration

### Environment Variables
For production, consider using environment variables for sensitive settings:
- `SECRET_KEY`
- `DATABASE_PASSWORD`
- `DEBUG` (set to False in production)

### Static Files
Static files are configured to be served from `/static/` URL and stored in the `static/` directory.

## 📝 Features

### Current Features
- ✅ Faculty management
- ✅ Department (Kafedra) management
- ✅ Teacher management with CRUD operations
- ✅ Subject management with credit system
- ✅ Student group management
- ✅ Student enrollment and records
- ✅ Responsive web interface
- ✅ Admin panel integration

### Future Enhancements
- 🔄 User authentication and authorization
- 🔄 Grade management system
- 🔄 Attendance tracking
- 🔄 Schedule management
- 🔄 Reporting system
- 🔄 API endpoints for mobile integration

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions, please contact:
- Email: [your-email@example.com]
- GitHub Issues: [repository-url]/issues

## 🔄 Version History

- **v1.0.0** - Initial release with basic CRUD operations
  - Faculty, Department, Teacher, Subject, Group, and Student management
  - SQLite database integration
  - Basic web interface

---

**Note**: This is a university management system designed for educational institutions to streamline their administrative processes.
