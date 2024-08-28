import random
import smtplib

from email.message import EmailMessage

code = ""
for i in range(6):
        code += str(random.randint(0,9))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
from_mail = 'testeovaldo1@gmail.com'
server.login(from_mail,'pjcp qklj xrah oqpp')
to_mail = input("Enter your best email: ")

msg = EmailMessage()
msg ['Subject'] = "Código de Ativação"
msg ['From']= from_mail
msg ['To'] = to_mail
msg.set_content("Seu código de verificacão é: " + code)

server.send_message(msg)

