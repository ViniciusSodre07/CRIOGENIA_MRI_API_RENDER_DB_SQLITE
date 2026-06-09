#pip install requests
import requests
import time

url = "http://127.0.0.1:8000/update_helium_level"

nivel = 80.0

while True:

    dados = {
        "helium_level_MRI": nivel
    }

    r = requests.post(url, json=dados)

    print("Enviado:", nivel)
    print("Resposta:", r.text)

    nivel -= 0.1

    time.sleep(2)