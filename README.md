# SocialBooster – Django REST API Demo

This project is a Django REST Framework–based backend application built as part of a technical assignment.  
It demonstrates CRUD REST APIs, PostgreSQL integration using Supabase, external API usage, and live deployment.

---

## 🚀 Live Deployment
https://socialbooster-django-api.onrender.com

> Note: This is an API-first backend project.  
> The root URL (`/`) may show "Not Found". Please use the API endpoints listed below.

---

## 📂 GitHub Repository
https://github.com/amolkore-1998/socialbooster-django-demo

---

## ⚙️ Tech Stack
- Python
- Django
- Django REST Framework
- PostgreSQL (Supabase)
- Gunicorn
- Render (Deployment)

---

## ✨ Features
- RESTful CRUD APIs
- PostgreSQL database using Supabase
- External API integration example
- Environment variable–based configuration
- Production deployment on Render

---

## 📌 API Endpoints

### Leads CRUD API
- `GET /api/leads/` – List all leads
- `POST /api/leads/` – Create a new lead
- `GET /api/leads/<id>/` – Retrieve a lead
- `PUT /api/leads/<id>/` – Update a lead
- `DELETE /api/leads/<id>/` – Delete a lead

---

## 🔗 External API Integration
The application integrates with a third-party REST API using Python `requests` to demonstrate external API consumption and data handling.

---

## 📊 Data Visualization / Reporting
A simple dashboard/reporting view is included to demonstrate how database records can be visualized or summarized.

---

## 🛠 Local Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/amolkore-1998/socialbooster-django-demo.git
cd socialbooster-django-demo


#Virtual Environment
python -m venv venv
venv\Scripts\activate 

#Install Dependencies
pip install -r requirements.txt

python manage.py migrate   #MIgrate

python manage.py runserver   #Run Server

 


