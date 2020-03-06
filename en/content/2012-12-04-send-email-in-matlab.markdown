UUID: 21443057-903b-44ae-b806-756ae32eeafc
Status: published
Title: Sending Email in MATLAB
Date: 2012-12-04 00:00:00
Tags: MATLAB, programming, email
Category: Computer Science
Slug: send-email-in-MATLAB
Author: Ben Chuanlong Du


It is very easy to send emails in MATLAB. 
To do this, you can just call `sendmail`. 
However, 
usually you need to set preference for sending emails using `setpref` first. 
Here is one example:

    %%
    % Define these variables appropriately:
    mail = 'username@gmail.com'; %Your GMail email address
    password = 'password'; %Your GMail password
    %%
    % Then this code will set up the preferences properly:
    setpref('Internet','E_mail',mail);
    setpref('Internet','SMTP_Server','smtp.gmail.com');
    setpref('Internet','SMTP_Username',mail);
    setpref('Internet','SMTP_Password',password);
    props = java.lang.System.getProperties;
    props.setProperty('mail.smtp.auth','true');
    props.setProperty('mail.smtp.socketFactory.class', 'javax.net.ssl.SSLSocketFactory');
    props.setProperty('mail.smtp.socketFactory.port','465');
    %%
    % Send email. The first argument is recipient.
    sendmail('receiver@gmail.com','Test from MATLAB','Hello! This is a test from MATLAB!')
            
