from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# defining webdriver for chrome
driver = webdriver.Chrome()

# opening the login page
driver.get('https://www.linkedin.com/login')

# waiting for the browser to load the page
time.sleep(2)

# initializing username and password and sending them to the login form
username = driver.find_element(By.ID, "username")
username.send_keys("useremail")

password = driver.find_element(By.ID, "password")
password.send_keys("userpassword")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

# waiting for the browser to load the page
time.sleep(3)

# fetching number of unread messages and notifications from their respective divs
messages = driver.find_element(By.XPATH, "//div[@id='ember13']//span//span")
notifications = driver.find_element(By.XPATH, "//div[@id='ember14']//span//span")



# initializing sender email and password and receiver email
sender_email = "senderemail"
receiver_email = "receiveremail"
password = "senderpassword"

# defining message that will be sent to the receiver via mail
message = MIMEMultipart("alternative")
message["Subject"] = "Unread Messages and Notifications"
message["From"] = sender_email
message["To"] = receiver_email

#creating message body using html
html = """\
<html>
  <body>
    <p>Hi,<br>
       You have """ + messages.text + """ unread messages<br>
       You have """ + notifications.text + """ unread notifications
    </p>
  </body>
</html>
"""

part = MIMEText(html, "html")
message.attach(part)

#sending email using smtp
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )