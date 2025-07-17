import streamlit as st
import openai
import pandas as pd

# Cargar el archivo
archivo = st.file_uploader("📁 Sube tu archivo Excel:", type=["xlsx"])

# Procesar si hay archivo
if archivo is not None:
    df = pd.read_excel(archivo)
    st.write("📊 Vista previa del archivo:")
    st.dataframe(df)

    # Input de pregunta
    pregunta = st.text_input("🧠 Escribe tu pregunta:")

    if pregunta:
        # Leer la API key desde los secrets
        openai.api_key = st.secrets.get("OPENAI_API_KEY", "")

        # Crear contexto a partir de las columnas
        contexto = f"Estas son las columnas del archivo: {', '.join(df.columns)}"
        prompt = f"{contexto}\n\nCon base en esto, responde lo siguiente:\n{pregunta}"

        # Llamada a OpenAI
        respuesta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )

        # Mostrar respuesta
        st.markdown("### ✅ Respuesta:")
        st.write(respuesta['choices'][0]['message']['content'])
else:
    st.warning("🔺 Sube un archivo Excel (.xlsx) para comenzar.")
