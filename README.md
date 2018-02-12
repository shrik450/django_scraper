# Django-Scraper

A django server running celery to scrape market headlines from the Economic Times, the Business Herald, and the Finanical Express. The server scrapes every 15 minutes and stores the headlines in the sqlite database. 

# Setup

This project is written in python 3.6.4 using Django 2.0.2. It's recommended that you create a virtual environment before using this server. Then, simply type;

    pip install -r requirements.txt

To install all python dependencies. You will also need a [RabbitMQ](https://www.rabbitmq.com/) server running on localhost, or you can also use [Redis](https://redis.io/) and change the [celery settings](http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html) in settings.py. First, you need to run the migrations. On a terminal at the scraper folder, run:

    python manage.py makemigrations

Then:
   
    python manage.py migrate

You will also need to create a superuser to get anything out of this, so run:

    python manage.py createsuperuser

Then, while in the scraper folder, run:

    celery -A scraper worker -l info

NOTE: On Windows, running celery like this raises ValueErrors whenever a task is called. If on windows, as a workaround you can run:

    celery -A scraper worker --pool=solo -l info

Then, on another terminal at the scraper folder, run:

    celery -A scraper beat -l info

This is enough for the scraper to run in the background, and update the database as necessary. To check the entries, you need to run:

    python manage.py runserver

Then head over to http://localhost:8000/admin/ (or your server's address) and login with the superuser you've created.