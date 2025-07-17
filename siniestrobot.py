import streamlit as st
import pandas as pd
import plotly.express as px
from openai import OpenAI

# Configuración de la clave API (usa secrets de Streamlit Cloud)
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("SiniestroBot 📊🚛")
st.write("Pregúntame lo que quieras sobre los siniestros")

# Cargar el archivo Excel
df = pd.read_excel("Info Siniestros.xlsx")

# Mostrar preview si el usuario lo pide
if st.checkbox("Mostrar datos"):
    st.dataframe(df)

# Entrada del usuario
pregunta = st.text_input("Escribe tu pregunta:")

if pregunta:
    with st.spinner("Pensando..."):
        contexto = df.to_string(index=False)
        respuesta = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un analista amable de siniestros en Traxión. Sé claro y directo."},
                {"role": "user", "content": f"Toma esta tabla:\n{contexto}\n\nRespóndeme esto:\n{pregunta}"}
            ],
            temperature=0.3
        )
        st.success(respuesta.choices[0].message.content)
