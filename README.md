# 🧑‍💼 Job Portal Web Application

A **mobile-responsive job portal web application** built with Python Flask, SQLite, and Bootstrap. It features **role-based access** for Admin, Employer, and Jobseeker with a clean UI and dynamic dashboard.

---

## 🚀 Features

- ✅ User roles: Admin, Employer, Jobseeker
- ✅ Admin Dashboard: Manage jobs, employers, jobseekers, and view stats (daily, weekly, monthly, yearly)
- ✅ Employers: Post jobs, view applications
- ✅ Jobseekers: Apply to jobs, view application history
- ✅ Secure Authentication & Role-based Access
- ✅ Mobile-Responsive UI with Bootstrap
- ✅ Slide-out Sidebar Navigation

---

## 🛠️ Tech Stack

- **Backend:** Python Flask
- **Database:** SQLite (SQLAlchemy ORM)
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Authentication:** Flask-Login
- **Data Visualization:** Chart.js (for dashboard stats)

---

## 📁 Project Structure

job_portal/
│
├── app/
│ ├── templates/
│ ├── static/
│ ├── routes/
│ ├── models.py
│ ├── forms.py
│ └── init.py
├── migrations/
├── create_admin.py
├── run.py
├── requirements.txt
└── README.md





---

## ⚙️ Installation & Setup

### 📌 Prerequisites

- Python 3.7+
- pip

### 🧰 Setup Steps

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/job_portal.git
cd job_portal

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run and create database 
flask shell
>>> from app import db
>>> db.create_all()
>>> exit()


# 5. (Optional) Create an Admin User
python create_admin.py

# 6. Run the application
flask run

