# E-commerce-website-django


---

# 🛍️ E-commerce Website (Django)

A simple **E-commerce web application** built with **Django**, featuring product listings, shopping cart, checkout functionality, and user authentication.

---

## 🚀 Features

* Browse products with categories and descriptions
* Add/remove products from the shopping cart
* Checkout page with customer details
* User authentication (login/register)
* Order management with total calculation
* Responsive Bootstrap-based UI

---

## ⚙️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS (Bootstrap), JavaScript
* **Database:** SQLite (default, can be changed to PostgreSQL/MySQL)
* **Other:** Django ORM, LocalStorage (for cart preview)

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/himangiagrawal15/E-commerce-website-django.git
cd E-commerce-website-django/ecomsite
```

### 2️⃣ Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

* **Windows (PowerShell):**

  ```bash
  venv\Scripts\activate
  ```
* **Linux / Mac:**

  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install dependencies

```bash
pip install django
```

*(Optional: add more packages later, e.g. Pillow for image handling)*

### 4️⃣ Apply migrations

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

### 5️⃣ Create a superuser (admin)

```bash
python manage.py createsuperuser
```

Follow prompts to set up admin login.

### 6️⃣ Run the development server

```bash
python manage.py runserver
```

Your app will be live at:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🧪 Usage

* Visit `/admin/` to log into Django admin and manage products/orders.
* Browse products on the homepage.
* Add items to cart, then proceed to checkout.

---

## 📂 Project Structure

```
ecomsite/
│── manage.py
│── ecomsite/         # Project settings & URLs
│── vecom/            # Main app (products, cart, orders, views, templates)
│── templates/        # HTML templates
│── static/           # CSS/JS/Images
```

---

## 📌 Future Improvements

* Payment integration (Razorpay/Stripe/PayPal)
* Product search and filtering
* Order history for users
* REST API for mobile apps

---

## 👩‍💻 Author

**Himangi Agrawal**
🔗 [GitHub](https://github.com/himangiagrawal15)

---



