#pip install requests
import requests
import time

#url = "http://127.0.0.1:8000/update_helium_level"
url="https://criogenia-mri-api-render-db-sqlite.onrender.com/update_helium_level"
file_path = r"helium_level.dat"
#nivel = 80.0

# Abre arquivo
with open(file_path, "r") as f:

    # Lê todas as linhas
    linhas = f.readlines()
    print(file_path)
# Remove espaços/quebras
linhas = [linha.strip() for linha in linhas]
dados = linhas[8:]


x=0

while x<len(dados):
    
    valor_1 = dados[x]
    nivel1 =valor_1[20:]
    nivel=float(nivel1)
    x=x+1
    
    print(nivel)
    print(nivel1)

    dado = {
        "helium_level_MRI": nivel
    }

    r = requests.post(url, json=dado)

    print("Enviado:", nivel)
    print("Resposta:", r.text)

    #nivel -= 1

    time.sleep(2)
  