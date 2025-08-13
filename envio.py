import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText


# conexão com as variaveis de ambiente
load_dotenv()
# pega os emails 
meu_email = os.getenv("EMAIL_USER")
senha_app = os.getenv("SENHA_APP")
destinatario = "weslleybarbosa662@gmail.com"
assunto = "Primeiro email enviado com smtplib"
corpo = "Olá, bem vindo ao meu mundo"

# preparação para a mensagem
mensagem = MIMEText(corpo,"plain","utf-8")
mensagem["Subject"] = assunto
mensagem["From"] = meu_email
mensagem["To"] = destinatario



with smtplib.SMTP("smtp.gmail.com",587) as servidor:
    servidor.starttls()
    servidor.login(meu_email,senha_app)
    servidor.sendmail(meu_email,destinatario,mensagem)


print("EMAIL ENVIADO COM SUCESSO!!!")