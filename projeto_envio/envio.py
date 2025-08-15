import smtplib
from dotenv import load_dotenv
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import make_msgid
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders

cid = make_msgid()[1:-1]
# conexão com as variaveis de ambiente
load_dotenv()
# pega os emails 
meu_email = os.getenv("EMAIL_USER")
senha_app = os.getenv("SENHA_APP")
destinatario = "weslleybarbosa662@gmail.com"
assunto = "Email enviado com a biblioteca smtplib"


corpo = f"""
<div style="width:350px; height:320px; background: #e6e6e6; border-radius:10px;">
    <div style="background:#8a2019; border-top-right-radius: 10px; border-top-left-radius: 10px; padding:10px;">
        <h1 style="color:white" text-align:center;>Produtos</h1>
    </div>

    <div>
        <img src="cid:{cid}" style="max-width: 350px ;  text-aling:center; border-bottom-right-radius: 10px; border-bottom-left-radius: 10px;">
    </div>
    
</div>
"""

# preparação para a mensagem
mensagem = MIMEMultipart("related")
mensagem["Subject"] = assunto
mensagem["From"] = meu_email
mensagem["To"] = destinatario
alt = MIMEMultipart("alternative")
alt.attach(MIMEText(corpo,"html","utf-8"))
mensagem.attach(alt)


with open ("../documentos/grafico.png","rb") as imagem:
    img = MIMEImage(imagem.read(), _subtype="png")
img.add_header("Content-ID",f"<{cid}>")
img.add_header("Content-Disposition","inline")
mensagem.attach(img)


caminho_documento = "../documentos/relatorio.pdf"
with open(caminho_documento, "rb") as anexo:
    parte = MIMEBase("application","octet-stream")
    parte.set_payload(anexo.read())

encoders.encode_base64(parte)
parte.add_header("Content-Disposition",f"attchment; filename=relatorio.pdf")


mensagem.attach(parte)

with smtplib.SMTP("smtp.gmail.com",587) as servidor:
    servidor.starttls()
    servidor.login(meu_email,senha_app)
    servidor.sendmail(meu_email,destinatario,mensagem.as_string())


print("EMAIL ENVIADO COM SUCESSO!!!")