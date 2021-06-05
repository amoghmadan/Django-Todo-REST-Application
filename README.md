# Django-Todo-REST-Application
Todo Application Backend

## How to set up?

- Clone this project
- Create a virtual environment
- pip install -r requirements.txt


## Run in development?

- cd src
- python manage.py runserver


## Run in production?

- Change specified variables in the settings file
```python
"""
<Original State>
DEBUG = True
"""
DEBUG = False

"""
<Original State>
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}
"""
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ],
}
```
- Run gunicorn for production after changing the settings
```bash
gunicorn tracker.wsgi:application -b 127.0.0.1:8000 -w 4 -t 2
```
