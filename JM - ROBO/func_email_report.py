import os
import smtplib
from email.message import EmailMessage

#configurar email e senha


def email_report(email, senha, email_destino, assunto, mensagem):
    try:
        EMAIL_ADDRESS = email
        EMAIL_PASSWORD = senha


        #cria email
        msg = EmailMessage()
        msg['Subject'] = assunto
        msg['From'] = email
        msg['To'] = email_destino
        msg.set_content(mensagem)

        #Enviar um e-mail
        with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            return True
    except:
        return False
