# Product-catalog
This a test project of product catalog

# Project description
It's include product list with its multiple attributes and multiple prices for different date ranges.

# Tech used
- Python 3.7
- Django
- Django Rest Framework
- Simple JWT authentication
- Faker and Factory boy (for test)

# Project Structure
- It is a monolith structure app has one project name product and containing two apps authentication and product_catalog.
- For virtualenvironment can use pipenv or python3 default environment.
- Its have simple docker file and docker compose file
- You can run in shell command `./runserver`.
- You find your all application log into `application.log` file in project root folder.

# How to run
- Clone this repo in your local.
- Create virtualenvironment using command `python3 -m venv <env_name>` or use `pipenv` library for more flexibility.
- Install dependencies using command `pipenv shell` and `pipenv install` or `pip install -r requirements.txt` after activating the virtualenv.
- Just run `./runserver.sh`
- For runing test run command `python manage.py test`
- For api documentation visit `http://0.0.0.0:8000/doc/` after running the server.

# Runing with docker
- Just run `docker-compose up`. (Make sure you have docker installed in your machine)
