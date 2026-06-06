# mybank — Django REST API

A banking-domain REST API built from scratch with Django REST Framework, JWT authentication, and PostgreSQL. Models real banking workflows including transaction management and teller session operations.

---

## What it does

A fully authenticated REST API for banking operations — users log in with JWT tokens, manage transactions, and track teller sessions.

**Get a token:**
```json
POST /api/token/
{
    "username": "soumya",
    "password": "yourpassword"
}
```

**Use token to fetch transactions:**
```
GET /api/transactions/
Authorization: Bearer <your_token>
```

**Filter transactions:**
```
GET /api/transactions/?transaction_type=credit
GET /api/tasks/?is_completed=false
GET /api/transactions/?search=ATM
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django + Django REST Framework |
| Authentication | JWT (simplejwt) |
| Database | PostgreSQL |
| API Testing | Swagger UI + Postman |

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/token/` | Login — get JWT access + refresh tokens |
| POST | `/api/token/refresh/` | Refresh expired access token |
| GET/POST | `/api/transactions/` | List or create transactions |
| GET/PUT/DELETE | `/api/transactions/{id}/` | Retrieve, update, delete transaction |
| GET/POST | `/api/teller-sessions/` | List or create teller sessions |
| GET/POST | `/api/tasks/` | List or create tasks |
| GET | `/api/tasks/?is_completed=false` | Filter incomplete tasks |
| GET | `/admin/` | Django admin panel |

---

## Models

**Transaction**
- description, amount, transaction_type (credit/debit), created_at

**TellerSession**
- teller_name, cash_drawer_opening_balance, cash_drawer_closing_balance, session_date, is_active

**Task**
- title, description, is_completed, created_at

---

## Running Locally

```bash
git clone https://github.com/soumyabailkeri/mybank.git
cd mybank
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit `http://localhost:8000/api/` for the browsable API.
Visit `http://localhost:8000/admin/` for the admin panel.

---

## Key Concepts Demonstrated

- Django ORM — models to PostgreSQL tables
- DRF serializers — Python objects to JSON
- ViewSets — automatic CRUD endpoints
- JWT authentication — stateless token-based security
- Custom filtering — `get_queryset()` with query params
- Django admin — built-in data management UI

---

## Domain Context

Models reflect real banking operations from 3 years at TCS:
- TellerSession maps to cash drawer management
- Transaction maps to banking transaction workflows
- JWT auth maps to session-based banking login systems

---

## Author

**Soumya Bailkeri**
Backend Software Engineer | Python · Django · DRF · BFSI
[LinkedIn](https://linkedin.com/in/soumyabailkeri) · [GitHub](https://github.com/soumyabailkeri)