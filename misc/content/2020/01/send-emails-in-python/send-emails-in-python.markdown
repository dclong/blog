Status: published
Date: 2020-01-29 22:18:53
Author: Benjamin Du
Slug: send-emails-in-python
Title: Send Emails in Python
Category: Computer Science
Tags: programming, Python, email, web, knockknock, yagmail, notifiers
Modified: 2020-08-29 22:18:53

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Use Standard Libraries smtplib and email

Below is a function for sending email leveraging standard libraries smtplib and email.

    :::python
    import smtplib
    from email.mime.text import MIMEText


    def send_email(recipient: Union[str, List[str]],
                subject: str,
                body: str = "",
                sender: str = "_sender_no_reply@domain.com",
                server: str = "smtp.server.domain.com"):
        """Send email.
        """
        mail = MIMEText(body, "html", "utf-8")
        mail["Subject"] = subject
        if isinstance(recipient, list):
            recipient = ";".join(recipient)
        mail["To"] = recipient
        mail["From"] = sender
        smtp = smtplib.SMTP()
        try:
            smtp.connect(server)
            smtp.send_message(mail)
            smtp.close()
            logger.info("The following message was sent: \n{}", mail.as_string())
            return True
        except:
            logger.info(
                "The following message was constructed but failed to sent: {}",
                mail.as_string())
            return False


## [knockknock](https://github.com/huggingface/knockknock)

## notifiers

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


## [yagmail](https://github.com/kootenpv/yagmail)

https://blog.mailtrap.io/yagmail-tutorial/

## References 

https://notifiers.readthedocs.io/en/latest/_modules/notifiers/providers/email.html?highlight=attachments