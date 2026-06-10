#python -m uvicorn main:app --reload
import sqlite3
import os
from fastapi import FastAPI

app = FastAPI()
###################Cria o banco de dados############
os.makedirs("db", exist_ok=True)
conn = sqlite3.connect("db/helium.db", check_same_thread=False)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS helium_levels (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    helium_level REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

#######################################

ultimo_nivel = 0.0


@app.get("/")
def home():
    return {"status": "online"}


@app.post("/update_helium_level")
def update_helium_level(dados: dict):

    global ultimo_nivel

    ultimo_nivel = dados["helium_level_MRI"]

    cursor.execute(
    """
    INSERT INTO helium_levels (helium_level)
    VALUES (?)
    """,
    (ultimo_nivel,)
    )

    conn.commit()

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

@app.get("/historico")
def historico():

    cursor.execute("""
        SELECT *
        FROM helium_levels
        ORDER BY id DESC
        LIMIT 20
    """)

    dados = cursor.fetchall()

    return dados