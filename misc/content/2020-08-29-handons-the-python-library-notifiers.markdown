Status: published
Date: 2020-08-29 22:38:46
Author: Benjamin Du
Slug: handons-the-python-library-notifiers
Title: Handons the Python Library Notifiers
Category: Computer Science
Tags: Computer Science, python, notifiers, notification, email, web, internet

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Email

The function below is an example of sending email using the Python library notifiers.

    :::python
    import notifiers
    notifiers.get_notifier("email").notify(
        from_="sender@domain.com",
        to=["recipient1@domain.com", "recipient2@domain.com"],
        subject="Example of Sending Email Using notifiers",
        message="This is a testing email.",
        host="smtp.domain.com",
        username="user_name_if_needed",
        password="password_if_needed",
        attachements=["/path/to/file1", "/path/to/file2"]
    )

Notice that notifiers supports email attachements via the `attachments` option
which accepts an iterable of valid file paths.