Status: published
Date: 2020-07-19 15:47:42
Author: Benjamin Du
Slug: send-emails-in-python
Title: Send Emails in Python
Category: Computer Science
Tags: programming, Python, email, web, knockknock, yagmail, notifiers

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**

## Use Standard Libraries smtplib and email

Below is a function for sending email leveraging standard libraries smtplib and email.

    :::python
    import smtplib
    from email.mime.text import MIMEText


    def send_email(recipient,
                subject,
                body="",
                sender="_sender_no_reply@domain.com",
                server="smtp.server.domain.com"):
        """Send email.
        """
        mail = MIMEText(body, "html", "utf-8")
        mail["Subject"] = subject
        mail["To"] = join(recipient, sep=";")
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
    def send_email(
        to: Union[str, List[str]],
        subject: str,
        msg: str,
        from_: str = "_dsm_no_reply@ebay.com",
        host: str = "mx.vip.ebay.com"
    ) -> None:
        """Send email in eBay's production environment.

        :param recipient: A (list of) email address(es) to send the email to.
        :param subject: The subject of the meail.
        :param msg: The body message of the meail.
        :param sender: The sender email address.
        :param host: The address of the STMP server.
        :return: A boolean value indicating whether the email is sent successfully.
        """
        if not to:
            return
        notifiers.get_notifier("email").notify(
            from_=from_,
            to=to,
            subject=subject,
            message=msg,
            host=host,
            username="",
            password="",
        )


## [yagmail](https://github.com/kootenpv/yagmail)

https://blog.mailtrap.io/yagmail-tutorial/