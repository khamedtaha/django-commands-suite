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

5. **Set Up Pre-commit Hooks**

   .. code-block:: bash

      pre-commit install

6. **Run Tests**

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

Code Style Guidelines
---------------------

Python Code
^^^^^^^^^^^

We follow **PEP 8** with some modifications:

- Maximum line length: 88 characters (Black formatter)
- Use double quotes for strings
- Use trailing commas in multi-line structures

**Formatting Tools**:

.. code-block:: bash

   # Format code with Black
   black .
   
   # Sort imports with isort
   isort .
   
   # Check style with flake8
   flake8 .

**Type Hints**:

Use type hints for all new code:

.. code-block:: python

   from typing import Dict, List, Optional, Union
   from django.contrib.auth.models import User

   def log_command(
       command_name: str,
       arguments: Dict[str, Any],
       status: str,
       output: str,
       user: Optional[User] = None,
       duration: Optional[float] = None
   ) -> 'CommandLog':
       """Log a command execution."""

Documentation
^^^^^^^^^^^^^

- Use Google-style docstrings
- Document all public functions, classes, and methods
- Include examples in docstrings
- Update relevant .rst files for user-facing changes

.. code-block:: python

   def backup_database(filename: str, compress: bool = False) -> str:
       """Create a database backup.
       
       Args:
           filename: Name of the backup file to create
           compress: Whether to compress the backup file
           
       Returns:
           Path to the created backup file
           
       Raises:
           BackupError: If backup creation fails
           PermissionError: If unable to write to backup directory
           
       Example:
           >>> backup_path = backup_database('daily_backup.sql', compress=True)
           >>> print(f"Backup created: {backup_path}")
       """

Tests
^^^^^

Write comprehensive tests for all new features:

.. code-block:: python

   from django.test import TestCase
   from django_commands_suite.testing import DCSTestCase
   from django_commands_suite.utils import run_command

   class BackupCommandTest(DCSTestCase):
       def test_basic_backup(self):
           """Test basic database backup functionality."""
           result = self.call_command('backup_db', filename='test.sql')
           
           self.assertCommandSuccess(result)
           self.assertIn('Backup completed', result['output'])
           self.assertTrue(os.path.exists('/backups/test.sql'))
       
       def test_compression_option(self):
           """Test backup with compression enabled."""
           result = self.call_command('backup_db', 
               filename='compressed.sql.gz', 
               compress=True
           )
           
           self.assertCommandSuccess(result)
           self.assertIn('compressed', result['output'])

Development Workflow
--------------------

Adding New Commands
^^^^^^^^^^^^^^^^^^^

1. **Create Command File**

   .. code-block:: bash

      # Create new command file
      touch django_commands_suite/management/commands/my_new_command.py

2. **Implement Command Class**

   .. code-block:: python

      from django_commands_suite.management.commands.base import DCSBaseCommand

      class Command(DCSBaseCommand):
          help = 'Description of what this command does'
          
          def add_arguments(self, parser):
              parser.add_argument('--option', help='Command option')
          
          def handle(self, *args, **options):
              try:
                  # Your command logic here
                  self.log_success("Command completed successfully")
              except Exception as e:
                  self.log_error(f"Command failed: {e}")
                  raise

3. **Write Tests**

   .. code-block:: python

      # tests/test_my_new_command.py
      from django_commands_suite.testing import DCSTestCase

      class MyNewCommandTest(DCSTestCase):
          def test_command_execution(self):
              result = self.call_command('my_new_command', option='value')
              self.assertCommandSuccess(result)

4. **Update Documentation**

   Add your command to the appropriate documentation files.

Adding New Features
^^^^^^^^^^^^^^^^^^^

1. **Design Discussion**

   For significant features, create an issue to discuss:
   - Use cases and requirements
   - Implementation approach
   - API design
   - Breaking changes

2. **Implementation**

   - Start with tests (TDD approach)
   - Implement feature incrementally
   - Maintain backward compatibility
   - Consider performance implications

3. **Documentation**

   - Update user documentation
   - Add API documentation
   - Include examples
   - Update changelog

Release Process
---------------

We follow semantic versioning (SemVer):

- **Major** (X.0.0): Breaking changes
- **Minor** (0.X.0): New features, backward compatible  
- **Patch** (0.0.X): Bug fixes

**Release Checklist**:

1. Update version in ``setup.py`` and ``__init__.py``
2. Update ``CHANGELOG.md``
3. Run full test suite
4. Update documentation
5. Create release notes
6. Tag release and push to GitHub
7. Deploy to PyPI

Code Review Process
-------------------

All contributions go through code review:

1. **Automated Checks**
   - Tests must pass
   - Code style checks (Black, flake8, isort)
   - Type checking (mypy)
   - Security scanning

2. **Manual Review**
   - Code quality and maintainability
   - Test coverage and quality
   - Documentation completeness
   - API design consistency

3. **Review Criteria**
   - Follows project conventions
   - Includes appropriate tests
   - Documentation is updated
   - No breaking changes (unless major version)

Communication Channels
----------------------

- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: General questions, ideas
- **Pull Requests**: Code changes, documentation updates
- **Discord**: Real-time chat with maintainers and community

Community Guidelines
--------------------

Please follow our Code of Conduct:

1. **Be Respectful**: Treat all community members with respect
2. **Be Constructive**: Provide helpful feedback and suggestions
3. **Be Patient**: Maintainers are volunteers with limited time
4. **Be Inclusive**: Welcome newcomers and different perspectives

Recognition
-----------

Contributors are recognized in several ways:

- Listed in ``CONTRIBUTORS.md``
- Mentioned in release notes
- GitHub contributor statistics
- Special thanks in major releases

Getting Help
------------

If you need help contributing:

1. Check existing documentation and issues
2. Ask questions in GitHub Discussions
3. Reach out on Discord
4. Contact maintainers directly for sensitive issues

Thank you for contributing to Django Commands Suite! Your efforts help make this project better for everyone.