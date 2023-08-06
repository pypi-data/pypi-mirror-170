# Notifications

This application sends notifications to the user and emails addresses.
It stores messages into a database, and sends can be delayed through a cron task.

## Installation

```shell
$ pip install django-delayed-notifications
```

Add `django_notifications` to your `INSTALLED_APPS`:
```python
INSTALLED_APPS = (
    ...
    "django_notifications",
    ...
)
```

Apply the migrations:

```shell
$ ./manage.py migrate
```

## Usage
Instead of sending a raw email, with the `send_mail` django function, you can create a Notification object and program the sending.

### Notification creation
```python

from django_notifications.models import Notification
from django.utils.timezone import now
from datetime import timedelta

my_instance = "<A random object in the application>"
notification = Notification.objects.create(
    subject="My beautiful email",
    text_body="My text body",
    html_body="""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="x-apple-disable-message-reformatting">
    <title>My beautiful email</title>
</head>
<body>My HTML bod</body>
</html>
    """,
    from_email = "foo@example.org",  # Optional

)
# It is possible to attach an object to the email (Optional)
notification.related_object = my_instance
# When using FSM, you can provide the states from / to (Optional)
notification.state_from = "active"
notification.state_to = "processing"

# Recipients management
# You can provide users
notification.recipients.set("<User instance>", "<User instance>",...)

# And / Or provides email address, `\n` separated
notification.email_recipients = "\n".join([
    "foo@example.org", "bar@example.org"
])

# You can set the delayed sending date
notification.delayed_sending_at = now() + timedelta(days=1)
# Or you can send the email immediatly
notification.send()
```

### Management command
The application provides a management command to send the emails:

```sh
$ ./manage.py send_notifications
12 notifications sent.
```

### Admin
This application provides an admin interface for notifications.

## Notes

The application is available in English and translated to French.
