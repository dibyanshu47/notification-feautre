from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com/login')

time.sleep(2)

username = driver.find_element(By.ID, "username")
username.send_keys("useremail")

password = driver.find_element(By.ID, "password")
password.send_keys("userpassword")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(3)

messages = driver.find_element(By.XPATH, "//div[@id='ember13']//span//span")
notifications = driver.find_element(By.XPATH, "//div[@id='ember14']//span//span")



sender_email = "senderemail"
receiver_email = "receiveremail"
password = "senderpassword"

message = MIMEMultipart("alternative")
message["Subject"] = "Unread Messages and Notifications"
message["From"] = sender_email
message["To"] = receiver_email

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

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )