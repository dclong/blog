Status: published
Date: 2020-03-17 21:22:04
Author: Benjamin Du
Slug: tips-on-selenium
Title: Tips on Selenium
Category: Computer Science
Tags: programming, Selenium, web automation

**
Things on this page are fragmentary and immature notes/thoughts of the author.
Please read with your own judgement!


https://stackoverflow.com/questions/30452395/selenium-pdf-automatic-download-not-working
**
https://stackoverflow.com/questions/31136581/automate-print-save-web-page-as-pdf-in-chrome-python-2-7

DesiredCapabilities cap = DesiredCapabilities.chrome();
cap.setCapability("download.default_directory","C:");
cap.setCapability("download.prompt_for_download","false");
cap.setCapability("directory_upgrade","true");
cap.setCapability("plugins.plugins_disabled","Chrome PDF Viewer");

WebDriver driver = new ChromeDriver(cap);
Or you can add the options.AddArgument("---printing"); to automatically click the print button.

https://stackoverflow.com/questions/30452395/selenium-pdf-automatic-download-not-working

## Docker Images

https://hub.docker.com/u/selenium

https://github.com/dclong/docker-jupyterhub-selenium-chrome

https://github.com/dclong/docker-jupyterhub-selenium-firefox

https://github.com/dclong/docker-selenium
