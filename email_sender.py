import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from scraper import coletar_noticias
from dotenv import load_dotenv

load_dotenv()
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT'))
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
DESTINATARIOS = os.getenv('DESTINATARIOS').split(',')

def enviar_email():
    noticias = coletar_noticias()
    if not noticias:
        print("Nenhuma notícia coletada")
        return

    msg = MIMEMultipart()
    msg['From'] = EMAIL_USER
    msg['To'] = ', '.join(DESTINATARIOS)
    msg['Subject'] = 'Notícias Atualizadas'
    corpo_email = '<h1>Notícias Recentes</h1><ul>'
    for noticia in noticias:
        corpo_email += f"<li><a href='{noticia['link']}'>{noticia['titulo']}</a></li>"
    corpo_email += '</ul>'
    msg.attach(MIMEText(corpo_email, 'html'))
    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, DESTINATARIOS, msg.as_string())
    
    print("Email enviado com sucesso!")
