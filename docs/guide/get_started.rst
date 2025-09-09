===============
Getting Started
===============

This guide will help you get up and running with Django Commands Suite quickly.

Quick Overview
--------------

Django Commands Suite provides both command-line and web-based interfaces for executing management commands. All command executions are automatically logged for audit and debugging purposes.

Discover Available Commands
--------------------------

View all available DCS commands:

.. code-block:: bash

   python manage.py dcs_help

This command displays:

- All built-in DCS commands
- Custom commands you've created  
- Brief descriptions of each command
- Usage examples

Basic Command Structure
----------------------

All DCS commands follow Django's standard management command structure but include additional features:

1. **Automatic Logging**: Every command execution is logged with timestamp, user, arguments, and output
2. **Error Handling**: Comprehensive error reporting and logging
3. **Progress Feedback**: Styled output with success, warning, and error indicators
4. **Web Terminal Support**: Commands can be executed via browser interface

Your First Commands
------------------

Let's start with some basic commands:

Create a Quick Superuser
^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python manage.py quick_superuser

This will interactively create a Django superuser with minimal prompts.

Backup Your Database
^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python manage.py backup_db

This creates a backup of your database in the default backup location.

Generate Test Data
^^^^^^^^^^^^^^^^^^

.. code-block:: bash

   python manage.py dummy_data --model auth.User --count 10

This generates 10 test user records with realistic data.

Web Terminal Access
------------------

After configuring URLs (see :doc:`installation`), access the web terminal at:

.. code-block::

   http://your-domain.com/dcs/terminal/

The web terminal provides:

- Interactive command execution
- Real-time output display  


Using the Web Terminal
^^^^^^^^^^^^^^^^^^^^^

1. Navigate to ``/dcs/terminal/`` in your browser
2. Log in with your Django user account
3. Type commands in the terminal interface
4. View real-time output and results

Example commands in web terminal:

.. code-block:: bash

   quick_superuser
   backup_db --db=sqlite
   dummy_data --model blog.Post --count 5

Command Logging
--------------

All command executions are automatically logged. You can view logs in several ways:

Django Admin Interface
^^^^^^^^^^^^^^^^^^^^^

1. Go to Django Admin
2. Navigate to "Django Commands Suite" section  
3. Click "Command logs"
4. Filter by command, date, status

Programmatic Access
^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from django_commands_suite.models import CommandLog
   
   # Error command executions
   recent = CommandLog.objects.filter(
      status="error"
   )
   
   # View command details
   for log in recent:
      print(f"{log.name}: {log.status}")


Rub Command in views
--------------------
Sometimes you may want to execute Django management commands directly from a view 
(for example, creating a backup from the dashboard).  
With ``django-commands-suite``, you can easily achieve this while keeping your views secure.


In this example, we define a decorator to ensure that only superusers can access the view.  
Then, inside the view, we call ``run_command`` to trigger a management command.

.. code-block:: python
   :caption: project/core/decorators.py

   from functools import wraps
   from django.contrib.auth.decorators import login_required
   from django.shortcuts import redirect

   def is_superuser_admin(view_func):
       @wraps(view_func)
       @login_required
       def _wrapped_view(request, *args, **kwargs):
           if request.user.is_superuser:
               return view_func(request, *args, **kwargs)
           return redirect("main")
       return _wrapped_view


.. code-block:: python
   :caption: project/core/views.py

   from django.shortcuts import render
   from django.contrib import messages
   from django_commands_suite.utils import run_command
   from .decorators import is_superuser_admin


   @is_superuser_admin
   def backup_db_view(request):
       if request.method == "POST":
           type_db = request.POST.get("type_db")
           output = run_command("backup_db", db=type_db)
           messages.success(request, f"Backup completed: {output}")

       return render(request, "core/Dash/backup.html")

* Example form in ``backup.html`` could look like:
.. code-block:: html

   <form method="post">
       {% csrf_token %}
       <select name="type_db">
           <option value="sqlite">SQLite</option>
           <option value="postgres">Postgres</option>
       </select>
       <button type="submit">Run Backup</button>
   </form>
