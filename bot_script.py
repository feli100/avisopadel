import requests
import os

def enviar_mensaje_telegram(mensaje):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    datos = {"chat_id": chat_id, "text": mensaje}
    response = requests.post(url, data=datos)
    print(response.text)  # Para depuración

# Mensaje que deseas enviar
mensaje = "Hola, esto es una alarma para que alquiles la pista del próximo martes."
enviar_mensaje_telegram(mensaje)
