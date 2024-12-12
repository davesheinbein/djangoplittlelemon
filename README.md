# Djangop Little Lemon
# https://www.coursera.org/learn/django-web-framework/peer/68wd1/peer-review-rubric-design-and-build-a-simple-django-app

## Restaurant Menu Django App

This code outlines the steps to create a simple menu page for a restaurant website using Django.

### Features

* Model menu items with name and price.
* Admin interface to manage menu items.
* Display menu items on a dedicated page.

### Requirements

* Python 3.x
* Django framework installed

### Setup

1. Create a Django app:

python manage.py startapp restaurant

2. Replace the contents of relevant files (`models.py`, `admin.py`, `views.py`, `menu.html`) with the provided code.

3. Update project-level `urls.py` to include the app's URL patterns (optional, see Step 4).

4. Run migrations:

python manage.py makemigrations restaurant
python manage.py migrate

### Usage

1. Create a superuser:

python manage.py createsuperuser

2. Run the development server:

python manage.py runserver

3. Access the admin interface (http://127.0.0.1:8000/admin) and log in with superuser credentials.

4. Navigate to the "Restaurant" app and add menu items.

5. (Optional) Create a link or URL pattern for the menu view.

6. Access the menu page at the corresponding URL (e.g., http://127.0.0.1:8000/menu/).

### Code Breakdown

* **models.py:** Defines the `Menu` model with `name` and `price` fields.
* **admin.py:** Registers the `Menu` model with the admin interface.
* **views.py:** Creates a `menu` view that retrieves and renders menu items.
* **urls.py (optional):** Defines a URL pattern for the `menu` view.
* **menu.html:** Displays the menu items in a basic format (customizable).

### Customization

* Add more fields to the `Menu` model (e.g., description, category).
* Implement image uploads for menu items.
* Create a visually appealing menu template with CSS or a frontend framework.

