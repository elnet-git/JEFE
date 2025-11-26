import subprocess
import threading
import webbrowser
import time

# Levantar proxy en segundo plano
def levantar_proxy():
    subprocess.Popen(["python", "proxy_server.py"])

threading.Thread(target=levantar_proxy, daemon=True).start()

# Espera un momento para que Flask inicie
time.sleep(2)

# Abrir el HTML
webbrowser.open("C:/jefe.html")  # Ajusta la ruta completa a tu HTML
