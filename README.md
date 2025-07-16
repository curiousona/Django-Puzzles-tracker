# 🧩 Django Puzzle Tracker App

> *Track your puzzle-solving journey while learning Django! This app helps you organize, categorize, and track your progress across different types of puzzles.*

A web application to track, categorize, and mark the completion of logic, math, arrangement, shape, and other puzzles. Built with Django, featuring an interactive dashboard, admin management, CSV export, and live progress tracking.

---

## 🚀 Features

* **Puzzle Categories:** Logical, Mathematical, Arrangement, Shape, Other
* **Admin Panel:** Add/edit puzzles, filter by category/solved status, search, inline toggle
* **Dashboard:**

  * Completion stats per category and overall
  * Interactive checklist to mark puzzles as solved/unsolved
  * Puzzles grouped by category, with "Asked in" info
  * Live updating of stats as you check/uncheck puzzles
* **CSV Export:** Download your puzzle checklist
* **Fixtures:** Preloaded puzzles for instant setup

---

## 🖼️ UI Walkthrough

### Dashboard

![Dashboard Screenshot](<img width="1269" height="852" alt="Screenshot 2025-07-16 at 5 10 07 PM" src="https://github.com/user-attachments/assets/a343b34d-d6e7-46fb-a590-fd15a4659480" />)

* **Top Table:** Solved / Total / % per category and overall
* **Checklist:** Check/uncheck puzzles to mark as solved/unsolved — updates stats live
* **"Asked in":** Shows interview/company where the puzzle was asked

### Admin Panel

* Add, edit, or delete puzzles
* Filter by category or solved status
* Search by title or "Asked in"
* Inline solved toggle

---

## 🛠️ Setup & Running

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
```

### 2️⃣ Install Dependencies

```bash
pip install django
```

### 3️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4️⃣ Load Sample Puzzles

```bash
python manage.py loaddata puzzles/fixtures.json
```

### 5️⃣ Create Superuser (for Admin)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Server

```bash
python manage.py runserver
```

### 7️⃣ Access the App

* **Dashboard:** [https://django-puzzles-tracker.onrender.com/puzzles/dashboard/](https://django-puzzles-tracker.onrender.com/puzzles/dashboard/)
* **Admin Panel:** [https://django-puzzles-tracker.onrender.com/admin/puzzles/puzzle/](https://django-puzzles-tracker.onrender.com/admin/puzzles/puzzle/)

---

## 🧑‍💻 Implementation Overview

### Models

* `Puzzle`: title, asked\_in, category, solved

### Views

* `dashboard`: Puzzle checklist with stats
* `toggle_solved`: AJAX endpoint for live updates
* `export_csv`: Export puzzles as CSV

### Templates & Static

* Clean, responsive dashboard
* Custom CSS for a modern look

### Fixtures

* `puzzles/fixtures.json` for preloaded puzzles

---

## 📦 Project Structure

```
puzzle_tracker/
├── manage.py
├── puzzle_tracker/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── puzzles/
    ├── admin.py
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── fixtures.json
    ├── static/puzzles/dashboard.css
    ├── templates/puzzles/dashboard.html
```

---

## 🙋 FAQ

**Q: Can I use this with PostgreSQL/MySQL?**
✅ Yes! Update `settings.py` for your DB and use fixtures.

**Q: How do I add more puzzles?**
✅ Use Django Admin or edit `fixtures.json` and reload.

**Q: Can I make this user-specific?**
🔧 Currently global; user-specific tracking requires extending the models (feel free to ask!).

---

## 🧑‍💻 Contributing

Open to contributions! Suggestions and PRs welcome.

---

## 📄 License

MIT License

---
