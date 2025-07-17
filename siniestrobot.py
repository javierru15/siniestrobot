import streamlit as st
import pandas as pd
from openai import OpenAI

# Ruta directa al archivo en GitHub
archivo_url = "https://raw.githubusercontent.com/javierru15/siniestrobot/main/Info%20Siniestros.xlsx"

# Cargar el archivo
df = pd.read_excel(archivo_url)

# Título
st.title("🤖 SiniestroBot – Analiza tus datos con IA")

# Vista previa
st.subheader("👁️ Vista previa de datos")
st.dataframe(df)

# Pregunta del usuario
pregunta = st.text_input("❓ Escribe tu pregunta:")

if pregunta:
    # Crear cliente OpenAI
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    # Contexto para el modelo
    columnas = ", ".join(df.columns)
    contexto = f"Estas son las columnas del archivo: {columnas}"
    prompt = f"{contexto}\n\nCon base en esto, responde lo siguiente:\n{pregunta}"

    # Llamada a OpenAI con cliente nuevo
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )

    # Mostrar respuesta
    st.markdown("### ✅ Respuesta:")
    st.write(response.choices[0].message.content)
