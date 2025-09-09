Installation
============

This section covers how to install and set up Django Commands Suite in your Django project.

Requirements
-----------

- Django 3.2 or higher
- Python 3.8 or higher

Step 1: Install the Package
---------------------------

Install Django Commands Suite using pip:

.. code-block:: bash

   pip install django-commands-suite

Step 2: Configure Django Settings
---------------------------------

Add ``django_commands_suite`` to your ``INSTALLED_APPS`` in your Django project's ``settings.py``:

.. code-block:: python

   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       
       # Your apps
       'your_app',
       
       # Django Commands Suite
       'django_commands_suite',
   ]

Step 3: Database Setup
---------------------

Create and apply the necessary database migrations:

.. code-block:: bash

   python manage.py makemigrations django_commands_suite
   python manage.py migrate

This will create the necessary database tables for command logging and tracking.

Step 4: URL Configuration (Optional)
------------------------------------

To enable the Web Terminal feature, add the following to your main ``urls.py``:

.. code-block:: python

   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('dcs/', include('django_commands_suite.urls')),
       # Your other URL patterns
   ]

After this setup, the web terminal will be available at ``/dcs/terminal/``.

Verification
-----------

To verify that Django Commands Suite is properly installed, run:

.. code-block:: bash

   python manage.py dcs_help

You should see a list of available DCS commands.