import schedule
import time
from email_sender import enviar_email

def job():
    print("Iniciando o processo de scraping e envio de email...")
    enviar_email()

schedule.every().day.at("08:00").do(job)

print("Agendador iniciado. Aguardando horários agendados...")
while True:
    schedule.run_pending()
    time.sleep(60)
