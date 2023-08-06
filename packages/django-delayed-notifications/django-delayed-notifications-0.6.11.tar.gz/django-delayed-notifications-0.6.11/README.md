# Notifications

This application sends notifications to the user and emails addresses.
It stores messages into a database, and sends can be delayed through a cron task.

## Installation

```shell
$ pip istall django-notifications
```

Add `django_notifications` to your `INSTALLED_APPS`:
```python
INSTALLED_APPS = (
    ...
    'django_notifications',
    ...
)
```

Apply the migrations:

```shell
$ ./manage.py migrate
```

## Notes

The application is available in English and translated to French.
