# Barter Project


## Local project setup

1. Create a virtualenv running on Python 3.8
2. Install PostgreSQL and reate database for the project
3. Clone the project
4. Run the command `pip install -r requirements/local.txt` to install local environment apps
5. Create a copy of `phoenician_api/local_settings.tpl` and rename it to `local_settings.py`
6. Edit `local_settings.py` to match your local environment setup
7. Migrate the database using the command `python manage.py migrate`
8. Create your super user using the command `python manage.py createsuperuser`
9. Run the app using `python manage.py runserver`
