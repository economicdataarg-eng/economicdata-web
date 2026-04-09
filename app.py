import streamlit as st

# Configuración de la página
st.set_page_config(page_title="EconomicData.ARG", page_icon="📈")
# logo de economic data
import streamlit as st
from PIL import Image

# Cargar la imagen
foto = Image.open('mi_logo.png')

# Simplemente borramos el parámetro caption
st.image(foto, use_container_width=True)

def fondo_pagina():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://i.postimg.cc/Qdds5hf3/Gemini-Generated-Image-j94299j94299j942.png");
             background-attachment: fixed;
             background-size: cover;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

fondo_pagina()


# --- CABECERA ---
st.title("EconomicData.arg")
st.subheader("Análisis macro, microeconómico y datos financieros")
st.write("Nos dedicamos a la divulgación económica y el análisis de historia del pensamiento.")

# --- SECCIÓN: REDES SOCIALES ---
st.markdown("### 📱 Redes Sociales")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.link_button("Tiktok", "https://www.tiktok.com/@economicdata.arg")
with col2:
    st.link_button("YouTube", "https://www.youtube.com/@EconomicData.Argentina")
with col3:
    st.link_button("Instagram", "https://www.instagram.com/economicdata.arg/")
with col4:
    st.link_button("Spotify", "https://open.spotify.com/show/0mwKgRFyg926y22O2863tn")

st.divider()

# --- SECCIÓN: ESTUDIOS Y PUBLICACIONES ---
st.markdown("### 📚 Estudios de Economía")
st.info("Haz clic en los enlaces para leer mis investigaciones y análisis detallados.")

# Ejemplo de lista de estudios
estudios = {
    "Teoría de Adam Smith: Un análisis moderno": "https://www.youtube.com/watch?v=IkecNZnUGJQ&t=71s",
    "Keynes: Vida, teoria y legado": "https://www.youtube.com/watch?v=knb69ZuYf9o&t=1s",
    "Karl Marx Fundamentos de la historia, la economia y el poder": "https://www.youtube.com/watch?v=zlxB9UGkl6Q&t=55s"
}

for titulo, link in estudios.items():
    st.write(f"🔗 [{titulo}]({link})")

st.divider()

# --- SECCIÓN: CONTACTO ---
st.markdown("### ✉️ Contacto")
st.write("Si te interesa una colaboración nuestro alias es: Economicdata.arg o consultoría, escríbeme:")
st.write("📧 economicdata.arg@gmail.com")

# Formulario de contacto simple (simulado)
with st.form("contacto"):
    nombre = st.text_input("Nombre")
    mensaje = st.text_area("Tu consulta")
    submit = st.form_submit_button("Enviar")
    if submit:
        st.success(f"Gracias {nombre}, mensaje recibido, nos estaremos comunicando con usted.")

with st.sidebar:
    st.image(foto, width=150)
    st.write("Bienvenido a mi central de datos económicos.")
    st.divider()
    st.write("📧 contacto@economicdata.arg")

    st.markdown("### 📚 Estudios Recientes")
    col_e1, col_e2 = st.columns(2)

    with col_e1:
        st.markdown("""
            <div style="border: 1px solid #4CAF50; padding: 20px; border-radius: 15px;">
                <h4>Teoría de Kalecki</h4>
                <p>Análisis sobre la determinación de la inversión y ciclos económicos.</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Leer estudio", "https://drive.google.com/file/d/10raTTe9RnvrJb_SV_QwX7Mm2NxQxSocw/view?usp=sharing")

    with col_e2:
        st.markdown("""
            <div style="border: 1px solid #4CAF50; padding: 20px; border-radius: 15px;">
                <h4> Milton Friedman</h4>
                <p>Guía académica sobre Milton Friedman</p>
            </div>
        """, unsafe_allow_html=True)
        st.link_button("Ver datos", "https://drive.google.com/file/d/1prgMKDC_LzVDmbo9CQGOelH5O-bAZ9t3/view?usp=sharing")

import streamlit as st
import requests

# Título de la sección
st.divider()
st.markdown("### 💱 Conversor de Divisas Real-Time")


# Función para obtener datos
def obtener_cambio(base="USD"):
    url = f"https://open.er-api.com/v6/latest/{base}"
    data = requests.get(url).json()
    return data


datos = obtener_cambio("USD")

if datos["result"] == "success":
    tasas = datos["rates"]

    col_conv1, col_conv2 = st.columns(2)

    with col_conv1:
        cantidad = st.number_input("Cantidad en Dólares (USD)", min_value=0.0, value=1.0)

    with col_conv2:
        # Aquí puedes agregar las monedas que quieras del mundo
        moneda_destino = st.selectbox("Convertir a:", ["ARS", "BRL", "CLP", "UYU", "EUR", "MXN"])

    # Cálculo
    resultado = cantidad * tasas[moneda_destino]

    # Mostrar resultado con diseño llamativo
    st.metric(label=f"Total en {moneda_destino}", value=f"{resultado:,.2f}")
    st.caption(f"Última actualización: {datos['time_last_update_utc'][:16]}")
else:
    st.error("No se pudo conectar con el servidor de divisas.")

    import streamlit as st
    import requests

    st.divider()
    st.markdown("### ₿ Mercado de Criptomonedas (USD)")


    # Función para obtener precios de criptos
    def obtener_precios_cripto():
        # Consultamos Bitcoin, Ethereum, Solana y Tether
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,tether&vs_currencies=usd&include_24hr_change=true"
        try:
            respuesta = requests.get(url)
            return respuesta.json()
        except:
            return None

 