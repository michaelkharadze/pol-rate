# Pol‑Rate

A Django web app built during a hackathon to help young voters learn about politicians and make informed choices.

---

## Table of contents

* [Features](#features)
* [Tech stack](#tech-stack)
* [Getting started](#getting-started)
* [Project structure](#project-structure)

---

## Features

* Browse **politician profiles** with bios, positions, and links.
* **Rate / endorse** and discuss candidates.
* **Search** by name, party, or topic.
* **User accounts** for posting and voting.
* **Admin** interface for managing politicians and content.

---

## Tech stack

* **Framework:** Django (Python). The repo includes `manage.py` and Django app directories.
* **Languages:** Python, TypeScript, HTML, CSS
* **Database:** SQLite for development
* **Hosting:** Heroku — repo includes a `Procfile` (Heroku apps require one; Heroku recommends **Gunicorn** as the web server).

---

## Getting started

### 1) Clone and set up

```bash
git clone https://github.com/michaelkharadze/pol-rate.git
cd pol-rate

# (Recommended) create & activate a virtualenv
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.\.venv\Scripts\activate

pip install -r requirements.txt
```

Django uses `manage.py` for common tasks.

### 2) Apply migrations & create an admin

```bash
python manage.py migrate
python manage.py createsuperuser
```

`migrate` applies database schema; `createsuperuser` adds an admin user.

### 3) Run the app

```bash
python manage.py runserver
```

The dev server starts on `http://127.0.0.1:8000/` by default.

---

## Project structure

```
pol-rate/
├── hackathon_election/   # Django project config (settings, wsgi, urls)
├── politicians/          # App: politician data and views
├── users/                # App: authentication/user features
├── manage.py
├── requirements.txt
├── Procfile
├── db.sqlite3
└── README.md
```

Top‑level files and directories are visible in the repository, including `Procfile`, `requirements.txt`, `db.sqlite3`, and the three Django modules above.
