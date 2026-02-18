# alx-Social-Media-Feed-Backend

A **Django-powered Social Media Backend API** built with GraphQL and Django REST Framework.
This project allows users to register, create posts, comment, and like posts.

---

## 🚀 Features

* User Authentication
* Create, Update, Delete Posts
* Comment on Posts
* Like Posts
* GraphQL API (Graphene-Django)
* REST API (Django REST Framework)
* SQLite Database (default)
* Admin Panel

---

## 🛠 Tech Stack

* Python
* Django
* GraphQL (Graphene-Django)
* Django REST Framework
* SQLite (default database)

---

## 📁 Project Structure

```
alx-Social-Media-Feed-Backend/
│
├── config/              # Django project settings
├── feed/                # Main app
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── schema.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│
├── staticfiles/
├── manage.py
├── requirements.txt
├── db.sqlite3
└── README.md
```

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/alx-Social-Media-Feed-Backend.git
cd alx-Social-Media-Feed-Backend
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Apply Migrations

```bash
python manage.py migrate
```

### 5️⃣ Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 6️⃣ Run the Server

```bash
python manage.py runserver
```

---

## 🌐 API Endpoints

### 🔗 REST API

```
http://localhost:8000/api/
```

### 🔗 GraphQL Endpoint

```
http://localhost:8000/graphql/
```

---

## 🧪 Example GraphQL Query

```graphql
query {
  allPosts {
    id
    title
    content
  }
}
```

---

## 🔐 Admin Panel

```
http://localhost:8000/admin/
```

Login using your superuser credentials.

---

## 📄 License

Developed as part of the ALX Backend Program.

---

