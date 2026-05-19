# Cars Django App

A simple Django app to manage cars with brand and year.

## Features

- List cars with search and pagination
- Add and edit cars
- Delete cars directly from the list page

## Setup

1. Create and activate a virtual environment:

2. Install django:

```bash
pip install django
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

5. Visit app in:http://127.0.0.1:8000/

## Files to know

- `project/` – Django settings and URLs
- `car/` – app logic, models, views, forms, templates, static files
- `templates/base.html` – base layout

## Notes

- Delete is handled inline from the list page using a POST form.
- The app uses Bootstrap for styling.
