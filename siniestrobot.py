import streamlit as st
import pandas as pd
import openai
import plotly.express as px

# Configuración de la clave API (guárdala de forma segura en prod)
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("SiniestroBot 📊🚛")
st.write("Pregúntame lo que quieras sobre los siniestros")

# Cargar el archivo Excel
df = pd.read_excel("Info Siniestros.xlsx")

# Mostrar preview
if st.checkbox("Mostrar datos"):
    st.dataframe(df)

# Entrada de usuario
pregunta = st.text_input("Escribe tu pregunta:")

if pregunta:
    with st.spinner("Pensando..."):
        contexto = df.to_string(index=False)
        respuesta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Eres un analista amable de siniestros en Traxión. Sé claro y directo."},
                {"role": "user", "content": f"Toma esta tabla:\n{contexto}\n\nY respóndeme esto:\n{pregunta}"}
            ],
            temperature=0.3
        )
        st.success(respuesta["choices"][0]["message"]["content"])
