# Product Inventory Management
Product Inventory Management is a Django web application that allows users to manage a product inventory. It provides CRUD (Create, Read, Update, Delete) operations for the Product model and includes fields for time created and date created.

# Features
  View a list of products in the inventory.

  Add new products to the inventory.

  Edit existing products in the inventory.

  Delete products from the inventory.

# Requirements
  Python 3.x

  Django 3.x

# Getting Started
# Installation
- Clone the repository:

  $ git clone https://github.com/Dolapur/Product_Inventory_Management.git

  $ cd Product_Inventory_Management

- Set up a virtual environment (optional but recommended):
  $ python3 -m venv env

  $ source env/bin/activate

- Install the dependencies:

  $ pip install -r requirements.txt

- Configuration:

  Configure the database settings in product_inventory/settings.py. By default, the application uses an SQLite database.

- Apply the model changes to the database:

  $ python manage.py migrate

# Usage:

- Start the Django development server:

  $ python manage.py runserver

- Open your web browser and visit http://localhost:8000/ to access the product inventory management app.

- Use the app to perform CRUD operations on the product inventory:

  View the list of products in the inventory.

  Click on "Add Product" to create a new product.

  Edit existing products by clicking on the "Edit" link next to each product.

  Delete products by clicking on the "Delete" button next to each product.

# Testing:

  To run the tests for the application, execute the following command:

  $ python manage.py test

# Project Structure
The project has the following structure:
- product_inventory/: Django project root directory.
- inventory_management/: Django app directory containing the product inventory management functionality.
- migrations/: Directory containing database migration files.
- templates/inventory_management/: Directory containing HTML templates for the app.
- admin.py: Django admin configuration.
- forms.py: Django forms for the app.
- models.py: Django models for the app.
- urls.py: URL configuration for the app.
- views.py: Views and logic for the app.
- product_inventory/: Project settings directory.
- settings.py: Django project settings.
- manage.py: Django project management script.

# Contributing
  Contributions to the Product Inventory Management project are welcome. If you have any ideas, suggestions, or bug reports, please create a new issue or submit a pull request.

# License
  The Product Inventory Management project is licensed under the MIT License.
