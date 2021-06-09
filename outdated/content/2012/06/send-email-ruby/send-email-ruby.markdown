Status: published
Date: 2020-04-06 11:28:52
Author: Ben Chuanlong Du
Title: Send Email in Ruby
Slug: send-email-ruby
Category: Computer Science
Tags: smtp, programming, Verizon, PDF, Ruby, email

<img src="http://dclong.github.io/media/ruby/ruby.png" height="200" width="240" align="right"/>

A few days ago, I started writing my first Ruby program which read my Verizon
family plan statements, calculate bills for each member and send emails to
notify them. The part of reading PDF document and calculating bill is easy. I
stuck at the sending email part. There are many Ruby libraries for sending
emails, but I want one that allows me to use my Gmail account. For security
reasons, I use a backup Gmail for sending emails. So I want a Ruby library which
allows me to set the "Reply-to" header, the "From" header and can send emails to
multiple recipients at a time. I tried a few options, such as "net/smtp",
"mikell/mail", "pony" and finally I was recommended the library "actionmailer".
Among all these libraries, "actionmailer" meets my requirement well and has good
documentation. The following the function I wrote to send email to members in my
family plan.

    def email_bills(subject,body)
        require 'action_mailer'
        ActionMailer::Base.raise_delivery_errors = true
        ActionMailer::Base.delivery_method = :smtp
        member_emails = "dclong@iastate.edu,lisa19850925@gmail.com,lynnyu2009@gmail.com,klins@iastate.edu"
        # member_emails = 'duchuanlong@gmail.com'
        # read in password for 'firedragon.du@gmail.com'
        password = read_password
        ActionMailer::Base.smtp_settings = {
            :address   => "smtp.gmail.com",
            :port      => 587,
            :domain    => "gmail.com",
            :authentication => :plain,
            :user_name      => "firedragon.du@gmail.com",
            :password       => password,
            :enable_starttls_auto => true
        }
        mail = ActionMailer::Base.mail(:to=>member_emails)
        mail.from = "duchuanlong@gmail.com"
        mail.reply_to = "duchuanlong@gmail.com"
        mail.subject = subject
        mail.body = body
        mail.deliver
    end
    def read_password()
        require 'highline/import'
        return ask('Please enter the password for "firedragon.du@gmail.com":' + "\n"){
            |q|
            q.echo = "*"
        }
    end

