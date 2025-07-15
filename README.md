# Django Puzzle Tracker App

> _This project was born out of my journey solving puzzles and learning Django. As I explored both, I realized I wanted a way to track my progress, categorize puzzles, and visualize my learning—all in one place. That's how this app came to life!_

A web application to track, categorize, and mark completion of logic, math, arrangement, shape, and other puzzles. Built with Django, featuring an interactive dashboard, admin management, CSV export, and live progress tracking.

---

## 🚀 Features

- **Puzzle Categories:** Logical, Mathematical, Arrangement, Shape, Other
- **Admin Panel:** Add/edit puzzles, filter by category/solved, search, inline toggle
- **Dashboard:**
  - Completion stats per category and overall
  - Interactive checklist to mark puzzles as solved/unsolved
  - Puzzles grouped by category, with "Asked in" info
  - Live updating of stats as you check/uncheck puzzles
- **CSV Export:** Download your puzzle checklist
- **Fixtures:** Preloaded puzzles for instant setup

---

## 🖼️ UI Walkthrough

### Dashboard
![Dashboard Screenshot](docs/dashboard.png)
- **Top Table:** Shows solved/total/percent for each category and overall
- **Checklist:** Each puzzle is a checkbox grouped by category. Check/uncheck to mark as solved/unsolved. Stats update instantly!
- **"Asked in":** Shows where each puzzle was featured/interviewed

### Admin Panel
- Add, edit, or delete puzzles
- Filter by category or solved status
- Search by title or asked-in
- Inline toggle for solved

---

## 🛠️ Setup & Running

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2. Install dependencies
```bash
pip install django
```

### 3. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Load sample puzzles
```bash
python manage.py loaddata puzzles/fixtures.json
```

### 5. Create a superuser (for admin)
```bash
python manage.py createsuperuser
```

### 6. Run the server
```bash
python manage.py runserver
```

### 7. Open in your browser
- Dashboard: [http://127.0.0.1:8000/puzzles/](http://127.0.0.1:8000/puzzles/)
- Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🧩 Implementation Details

- **Models:**
  - `Puzzle`: title, asked_in, category, solved
- **Views:**
  - `dashboard`: Shows stats and interactive checklist
  - `toggle_solved`: AJAX endpoint to update puzzle status and stats
  - `export_csv`: Download all puzzles as CSV
- **Templates:**
  - Clean, responsive dashboard with live stats
- **Static:**
  - Custom CSS for a modern look
- **Fixtures:**
  - `puzzles/fixtures.json` contains all puzzles, ready to load

---

## 📝 Notes
- The checklist is interactive and updates stats live (no page reload needed)
- All data is stored in your database (SQLite by default, but works with any Django-supported DB)
- You can add/edit puzzles via the admin or by editing/loading fixtures

---

## 📦 Project Structure
```
puzzle_tracker/
├── manage.py
├── puzzle_tracker/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── puzzles/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── fixtures.json
    ├── static/puzzles/dashboard.css
    ├── templates/puzzles/dashboard.html
    ├── migrations/
    └── __init__.py
```

---

## 🙋 FAQ

**Q: Can I use this with PostgreSQL/MySQL?**  
A: Yes! Just update your `settings.py` database config and use the same fixtures.

**Q: How do I add more puzzles?**  
A: Use the Django admin or add to `fixtures.json` and reload.

**Q: Can I track puzzles per user?**  
A: This version is global, but you can extend it for user-specific tracking (ask for help!).

---

## 🧑‍💻 Contributing
Pull requests and suggestions welcome!

---

## 📄 License
MIT 
