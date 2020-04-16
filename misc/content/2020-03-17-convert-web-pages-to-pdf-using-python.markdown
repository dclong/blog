Status: published
Date: 2020-03-17 21:22:04
Author: Benjamin Du
Slug: convert-web-pages-to-pdf-using-python
Title: Convert Web Pages to PDF Using Python
Category: Computer Science
Tags: Computer Science

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!
**


## [python-pdfkit](https://github.com/JazzCore/python-pdfkit)
Python wrapper for wkhtmltopdf utility to convert HTML to PDF using Webkit.

pip install pdfkit
sudo apt-get install wkhtmltopdf
import pdfkit 
pdfkit.from_url('https://www.google.co.in/', 'shaurya.pdf') 


## [WeasyPrint](https://weasyprint.org/)

pip3 install weasyprint

pdf = weasyprint.HTML('http://www.google.com').write_pdf()
file('google.pdf', 'wb').write(pdf)


## Selenium

https://stackoverflow.com/questions/31136581/automate-print-save-web-page-as-pdf-in-chrome-python-2-7

DesiredCapabilities cap = DesiredCapabilities.chrome();
cap.setCapability("download.default_directory","C:");
cap.setCapability("download.prompt_for_download","false");
cap.setCapability("directory_upgrade","true");
cap.setCapability("plugins.plugins_disabled","Chrome PDF Viewer");

WebDriver driver = new ChromeDriver(cap);
Or you can add the options.AddArgument("---printing"); to automatically click the print button.

https://stackoverflow.com/questions/30452395/selenium-pdf-automatic-download-not-working

## Sikuli

## PyAutoGUI + WebBrowser

## Other Solutions

[Automate Web Page To PDF](https://stevepython.wordpress.com/2019/03/13/automate-web-page-to-pdf/)
introduces a way of using PyAutoGUI to automate the convertion of web pages to PDF.


## References

https://www.tutorialspoint.com/how-to-convert-html-to-pdf-using-python

https://stackoverflow.com/questions/23359083/how-to-convert-webpage-into-pdf-by-using-python

[WebBrowser](https://docs.python.org/3.8/library/webbrowser.html)
