Contributing
============

We welcome contributions to Django Commands Suite! This guide will help you get started with contributing to the project.

Getting Started
---------------

Development Setup
^^^^^^^^^^^^^^^^^

1. **Fork the Repository**

   Fork the Django Commands Suite repository on GitHub to your account.

2. **Clone Your Fork**

   .. code-block:: bash

      git clone https://github.com/yourusername/django-commands-suite.git
      cd django-commands-suite

3. **Create a Virtual Environment**

   .. code-block:: bash

      python -m venv venv
      source venv/bin/activate  # On Windows: venv\\Scripts\\activate

4. **Install Development Dependencies**

   .. code-block:: bash

      pip install -e .[dev]
      pip install -r requirements-dev.txt


5. **Run Tests**

   .. code-block:: bash

      python manage.py test
      # Or use pytest
      pytest

Project Structure
^^^^^^^^^^^^^^^^^^

.. code-block::

   django_commands_suite/
   ├── management/
   │   └── commands/          # Built-in commands
   ├── models.py              # CommandLog and other models
   ├── utils.py               # Utility functions
   ├── views.py               # Web terminal views
   ├── urls.py                # URL configuration
   ├── admin.py               # Django admin configuration
   ├── apps.py                # App configuration
   ├── signals.py             # Django signals
   ├── exceptions.py          # Custom exceptions
   ├── serializers.py         # DRF serializers
   ├── templates/             # HTML templates
   ├── static/                # CSS, JS, images
   └── tests/                 # Test suite

How to Contribute
-----------------

Reporting Issues
^^^^^^^^^^^^^^^^

Before creating an issue, please:

1. Search existing issues to avoid duplicates
2. Use the appropriate issue template
3. Provide detailed information:
   - Django version
   - Python version
   - DCS version
   - Steps to reproduce
   - Expected vs actual behavior
   - Error messages and stack traces

**Issue Templates**:

- Bug Report
- Feature Request  
- Documentation Improvement
- Performance Issue

Submitting Pull Requests
^^^^^^^^^^^^^^^^^^^^^^^^

1. **Create a Branch**

   Create a descriptive branch name:

   .. code-block:: bash

      git checkout -b feature/add-new-command
      git checkout -b fix/backup-compression-bug
      git checkout -b docs/improve-installation-guide

2. **Make Your Changes**

   - Follow the coding style guidelines
   - Write or update tests
   - Update documentation if needed
   - Add entries to the changelog

3. **Test Your Changes**

   .. code-block:: bash

      # Run the test suite
      python manage.py test
      
      # Run specific test
      python manage.py test tests.test_commands.TestBackupCommand
      
      # Check code coverage
      coverage run --source='.' manage.py test
      coverage report

4. **Commit Your Changes**

   Write clear, descriptive commit messages:

   .. code-block:: bash

      git add .
      git commit -m "Add database compression support to backup_db command
      
      - Add --compress flag to backup_db command
      - Support gzip and bzip2 compression formats
      - Add tests for compression functionality
      - Update documentation with new options"

5. **Push and Create Pull Request**

   .. code-block:: bash

      git push origin feature/add-new-command

   Then create a pull request on GitHub with:
   - Clear title and description
   - Link to related issues
   - Screenshots if relevant
   - Testing instructions



Release Process
---------------

We follow semantic versioning (SemVer):

- **Major** (X.0.0): Breaking changes
- **Minor** (0.X.0): New features, backward compatible  
- **Patch** (0.0.X): Bug fixes

Communication Channels
----------------------

- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: General questions, ideas
- **Pull Requests**: Code changes, documentation updates
- **Discord**: Real-time chat with maintainers and community


Getting Help
------------

If you need help contributing:

1. Check existing documentation and issues
2. Ask questions in GitHub Discussions
3. Reach out on Discord
4. Contact maintainers directly for sensitive issues

Thank you for contributing to Django Commands Suite! Your efforts help make this project better for everyone.