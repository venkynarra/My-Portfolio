import  smtplib
import ssl

from Tools.demo.mcast import receiver

from pages.Contact_Us import message

host = "smtp.gmail.com"
port = 465
username = "venkateshnarra368@gmail.com"
password = "qkuh gtes tbyz vvcu"

receiver = "venkateshnarra368@gmail.com"

context = ssl.create_default_context()
message = """\
Subject = Hi!
Hi, How are you
Bye!
"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)