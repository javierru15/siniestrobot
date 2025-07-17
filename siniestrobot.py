import streamlit as st
import pandas as pd
import openai
import plotly.express as px

# Configura la clave API (se toma desde Secrets en Streamlit)
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Carga de archivo
df = pd.read_excel("Info Siniestros.xlsx")

# Interfaz
st.title("SiniestroBot 📊🚛")
st.write("Pregúntame lo que quieras sobre los siniestros")

mostrar_datos = st.checkbox("Mostrar datos")
if mostrar_datos:
    st.dataframe(df)

pregunta = st.text_input("Escribe tu pregunta:")

if pregunta:
    # Crear contexto como texto plano para el prompt
    contexto = df.head(50).to_string(index=False)

    # Llamada a la API sin stream
    respuesta = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un analista amable de siniestros en Traxión. Sé claro y directo."},
            {"role": "user", "content": f"Toma esta tabla:\n{contexto}\n\nRespóndeme esto:\n{pregunta}"}
        ],
        temperature=0.3
    )

    # Muestra la respuesta
    st.success(respuesta.choices[0].message.content)
