# 📚 Library Management System

A web-based **Library Management System** designed to manage books, categories, rentals, sales, and track library statistics through an interactive dashboard.

The system provides an admin-friendly interface with visual analytics (charts), book status tracking, and easy book management.

---

## ✨ Features

* 📊 **Dashboard with statistics**

  * Total number of books
  * Available / Sold / Rented books
  * Profits from book sales and rentals
* 📚 **Book Management**

  * Add new books
  * Categorize books (History, Science, Art, Novels, etc.)
  * Track book status (Available, Sold, Rented)
* 🔍 **Search functionality**
* 🗂 **Category-based filtering**
* 📈 **Charts & Visual Reports**

  * Bar charts for profits
  * Pie charts for book availability
* 🌐 **Arabic UI support**
* 🧑‍💼 **Admin sidebar navigation**

---

## 🛠️ Tech Stack

> *(Edit this section if needed)*

* **Backend:** Django
* **Frontend:** HTML, CSS, Bootstrap
* **Charts:** Chart.js
* **Database:** SQLite

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/Yassin76648/Library-Management-System.git
cd library-management-system
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Start the server**

```bash
python manage.py runserver
```

6. Open your browser:

```
http://127.0.0.1:8000/
```

---

## 📂 Project Structure

```text
library-management-system/
│
├── lms_app/
│   ├── models.py
│   ├── views.py
│ 
├── static/
│   ├── css/
│   ├── js/
│
├── templates/
│   └── dashboard.html
│   ├── pages/
│   ├── parts/
│   └── base.html
├── manage.py
└── README.txt
```

---

## 🚀 Future Improvements

* User roles (Admin / Librarian / Student)
* Book reservation system
* Export reports (PDF / Excel)
* Notifications for overdue rentals
* REST API integration

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use and modify it.

---