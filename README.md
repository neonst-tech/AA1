# AA1 — Internal Company Announcements Portal

Starter repository for the **Internal Company Announcements Portal** project.

This repository intentionally contains only the basic Django application structure needed to begin development. The project requirements are provided separately by Neonst.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/neonst-tech/AA1.git
cd AA1
```

### 2. Create and activate a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run migrations

```bash
python manage.py migrate
```

### 5. Create an admin account

```bash
python manage.py createsuperuser
```

### 6. Start the development server

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

The Django admin is available at `http://127.0.0.1:8000/admin/`.

## Project Structure

```text
AA1/
├── announcements/       # Main application
├── config/              # Django project configuration
├── templates/           # Shared HTML templates
├── manage.py
├── requirements.txt
└── README.md
```

## Development Notes

- The application uses Django.
- Bootstrap is available through the base template.
- The `Announcement` model and Django admin registration provide the initial backend foundation.
- Public-facing pages are intentionally kept minimal. The remaining application behaviour and presentation should be implemented from the project requirements.
- Do not commit the virtual environment, database file, or secret configuration files.

## Before Submission

- Test the application from a clean environment.
- Make sure all required pages are reachable through navigation.
- Remove unused files and code.
- Check that migrations are included.
- Add screenshots of the completed application as requested in the project requirements.
