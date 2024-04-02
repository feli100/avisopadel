import requests
import schedule
import time
from datetime import datetime
import os

def enviar_mensaje_telegram(mensaje):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    datos = {"chat_id": chat_id, "text": mensaje}
    response = requests.post(url, data=datos)
    print(response.text)  # Para depuración

def comprobar_y_enviar():
    now = datetime.now()
    # Asegúrate de ajustar esta condición para tu zona horaria específica, si es necesario
    if now.weekday() == 1 and now.hour == 12 and now.minute == 1:  # 1 = Martes
        enviar_mensaje_telegram("Hola, esto es una alarma de tu bot de Telegram.")

# Programa la función para que se ejecute cada minuto
schedule.every().minute.at(":00").do(comprobar_y_enviar)

while True:
    schedule.run_pending()
    time.sleep(1)
