#python -m uvicorn main:app --reload
from fastapi import FastAPI

app = FastAPI()

ultimo_nivel = 0.0


@app.get("/")
def home():
    return {"status": "online"}


@app.post("/update_helium_level")
def update_helium_level(dados: dict):

    global ultimo_nivel

    ultimo_nivel = dados["helium_level_MRI"]

    print("Recebido:", ultimo_nivel)

    return {
        "status": "ok",
        "nivel": ultimo_nivel
    }


@app.get("/helium_level")
def read_helium_level():

    return {
        "helium_level_MRI": ultimo_nivel
    }