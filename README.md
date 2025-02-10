# 🛒 BigCorp E-commerce Platform

## 📌 Overview
BigCorp is a modern e-commerce platform with integrated payment solutions, a REST API, and a background task system using Celery and Redis.

## 🚀 Features
- 🔐 **User Authentication** (registration, login, password reset)
- 🏷 **Product Management** (discounts, recommendations, and admin panel)
- 🛍 **Shopping Cart & Checkout** (with Stripe and YooKassa integration)
- 📦 **Order Processing** (including PDF invoices and CSV export)
- 🌍 **REST API** (built with Django REST Framework, Swagger, and Redoc)
- ⚡ **Background Tasks** (Celery + Redis for async operations)
- 🎭 **HTMX for Dynamic UI Updates**
- 🤖 **GitHub Actions CI/CD with Telegram Notifications**
- 🐳 **Dockerized Environment** (PostgreSQL, Redis, Celery, Web App)

## 🛠 Installation
### 📌 Prerequisites
- 🐳 Docker & Docker Compose
- 💳 Stripe CLI

### 📥 Clone the repository
```sh
git https://github.com/talyx/bigcorp
cd bigcorp
```

### ⚙️ Environment Setup
1. Copy the example environment file:
   ```sh
   cp .env.example .env
   ```
2. Fill in required values (e.g., database credentials, Stripe keys, etc.)

### 🐳 Run with Docker
```sh
docker-compose up --build -d
```

### 💳 Start Stripe Webhook Listener
```sh
stripe listen --forward-to localhost:8000/payment/webhook/
```

### 🔑 Create Superuser
```sh
docker-compose exec bigcorp-app python manage.py createsuperuser
```
*Superuser is required to create categories in the admin panel before running the faker.*

### 🏗 Create Categories & Generate Fake Products
1. Log in to the admin panel and create product categories.
2. Run the following command to generate fake products:
   ```sh
   docker exec -it bigcorp-app python manage.py fakeproducts
   ```

### 🌐 Access the Application
- Open `http://localhost:8000/` in a browser.

## 📖 API Documentation
API docs are available at:
- 📜 Swagger UI: `http://localhost:8000/api/v1/swagger/`
- 📕 Redoc: `http://localhost:8000/api/v1/redoc/`

## 🧪 Running Tests
```sh
docker-compose exec bigcorp-app test
```

## 🚀 Deployment
### 🤖 GitHub Actions & CI/CD
- **Automated deployment** runs on every push to `main`.
- **Telegram notifications** are sent upon successful deployment.

ℹ️ Educational Project

This project is written for educational purposes only.
