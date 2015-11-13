# django_scrubadub

[![Build Status](https://travis-ci.org/datascopeanalytics/django-scrubadub.svg?branch=master)](https://travis-ci.org/datascopeanalytics/django-scrubadub)

This [Django](https://www.djangoproject.com/) package provides a web services
API (via [Django REST Framework](http://www.django-rest-framework.org/)) and
also a training interface for highlighting filth in dirty dirty text, which can
then be used to train [`scrubadub`](http://scrubadub.readthedocs.org/)
classifiers [`scrubadub`](http://scrubadub.readthedocs.org/).

## Usage

To get started using `django_scrubadub` in your Django project:

1. Install `django_scrubadub` into your python environment
   ```sh
   pip install django_scrubadub
   ```

2. Add `django_scrubadub` to your application
   ```python
   # settings.py
   INSTALLED_APPS = (
       ...
       'django_scrubadub',
       ...
   )

   # urls.py
   urlpatterns = +[
       url(r'^scrubadub/', include('django_scrubadub.urls')),
   ]
   ```

3. Migrate your database to add some default filth detection from scrubadub
   into your application
   ```sh
   ./manage.py migrate
   ```

4. Install all of npm packages necessary for the training interface with
   ```sh
   npm install
   ```

5. Start the development server with `./manage.py runserver` and open up
   http://localhost:8000/scrubadub to add some documents for review.


## Contributing

The intent of django-scrubadub is to make it as easy as possible for anyone to
contribute. Please see [the contributing guidelines](CONTRIBUTING.md) for more details.
