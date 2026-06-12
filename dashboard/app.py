#streamlit run app.py
#python -m streamlit run app.py
import streamlit as st
import requests
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# Refresh every 2 seconds (2000 ms)
st_autorefresh(interval=2000, key="helium_refresh")

API_URL = "https://criogenia-mri-api-render-db-sqlite.onrender.com"

st.title("MRI Cryogenics Dashboard")

try:

    r = requests.get(f"{API_URL}/helium_level")

    nivel = r.json()["helium_level_MRI"]

    st.metric(
        label="Current Helium Level",
        value=f"{nivel:.1f}%"
    )

except Exception as e:

    st.error(f"API Error: {e}")

#Add the history table

r = requests.get(f"{API_URL}/historico")

dados = r.json()

df = pd.DataFrame(
    dados,
    columns=[
        "ID",
        "Helium Level",
        "Timestamp"
    ]
)

st.subheader("History")

st.dataframe(df)

#Add the chart
st.subheader("Helium Trend")

grafico = df.copy()

grafico = grafico.sort_values("ID")

grafico = grafico.set_index("Timestamp")

st.line_chart(grafico["Helium Level"])


