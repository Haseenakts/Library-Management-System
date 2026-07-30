# Library Management System

A simple Django-based library management system for managing books, members, and issued books.

## Features
- Add and view books
- Manage library members
- Track issued books
- Simple dashboard interface

## Requirements
- Python 3.10+
- Django

## Setup
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:
   ```bash
   pip install django
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage
Open your browser and visit:
```text
http://127.0.0.1:8000/
```

## Project Structure
- `library/` - app logic, models, views, templates
- `library_project/` - Django project settings and URLs
