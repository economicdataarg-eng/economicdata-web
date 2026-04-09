import streamlit as st
import requests
from PIL import Image
import base64

# 1. CONFIGURACIÓN DE PÁGINA (Debe ser lo primero)
st.set_page_config(page_title="EconomicData.ARG", page_icon="📈")


# 2. FONDO DE PANTALLA
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

# 3. LOGO PRINCIPAL
try:
    foto = Image.open('mi_logo.png')
    st.image(foto, use_container_width=True)
except:
    st.warning("No se encontró el archivo 'mi_logo.png'. Asegúrate de subirlo a GitHub.")

# 4. CABECERA
st.title("EconomicData.arg")
st.subheader("Análisis macro, microeconómico y datos financieros")
st.write("Nos dedicamos a la divulgación económica y el análisis de historia del pensamiento.")

# 5. REDES SOCIALES
st.markdown("### 📱 Redes Sociales")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.link_button("Tiktok", "https://www.tiktok.com/@economicdata.arg")
with col2:
    st.link_button("YouTube", "https://www.youtube.com/@EconomicData.Argentina")
with col3:
    st.link_button("Instagram", "https://www.instagram.com/economicdata.arg/")
with col4:
    st.link_button("Spotify", "https://spotify.com")  # Link corregido

st.divider()

# 6. ESTUDIOS Y PUBLICACIONES
st.markdown("### 📚 Estudios de Economía")
st.info("Haz clic en los enlaces para leer mis investigaciones y análisis detallados.")

estudios = {
    "Teoría de Adam Smith: Un análisis moderno": "https://www.youtube.com/watch?v=IkecNZnUGJQ&t=71s",
    "Keynes: Vida, teoria y legado": "https://www.youtube.com/watch?v=knb69ZuYf9o&t=1s",
    "Karl Marx: Fundamentos de la historia": "https://www.youtube.com/watch?v=zlxB9UGkl6Q&t=55s"
}

for titulo, link in estudios.items():
    st.write(f"🔗 [{titulo}]({link})")

st.divider()

# 7. CONVERSOR DE DIVISAS
st.markdown("### 💱 Conversor de Divisas Real-Time")


@st.cache_data(ttl=3600)  # Para no saturar la API
def obtener_cambio(base="USD"):
    url = f"https://open.er-api.com/v6/latest/{base}"
    return requests.get(url).json()


datos_divisas = obtener_cambio("USD")

if datos_divisas["result"] == "success":
    tasas = datos_divisas["rates"]
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        cantidad = st.number_input("Cantidad en USD", min_value=0.0, value=1.0)
    with col_c2:
        moneda = st.selectbox("Convertir a:", ["ARS", "BRL", "CLP", "UYU", "EUR", "MXN"])

    resultado = cantidad * tasas[moneda]
    st.metric(label=f"Total en {moneda}", value=f"{resultado:,.2f}")
else:
    st.error("Error al cargar divisas.")

# 8. MERCADO CRIPTO
st.divider()
st.markdown("### ₿ Mercado de Criptomonedas (USD)")


def obtener_precios_cripto():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana,tether&vs_currencies=usd&include_24hr_change=true"
    try:
        return requests.get(url).json()
    except:
        return None


datos_crypto = obtener_precios_cripto()

if datos_crypto:
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Bitcoin", f"${datos_crypto['bitcoin']['usd']:,}", f"{datos_crypto['bitcoin']['usd_24h_change']:.2f}%")
    c2.metric("Ethereum", f"${datos_crypto['ethereum']['usd']:,}", f"{datos_crypto['ethereum']['usd_24h_change']:.2f}%")
    c3.metric("Solana", f"${datos_crypto['solana']['usd']:,}", f"{datos_crypto['solana']['usd_24h_change']:.2f}%")
    c4.metric("Tether", f"${datos_crypto['tether']['usd']:.2f}")

st.divider()

# 9. CONTACTO REAL (FormSubmit)
st.markdown("### ✉️ Contacto Directo")
mi_correo = "economicdata.arg@gmail.com"

# IMPORTANTE: Solo un formulario con la clave 'contacto_real'
with st.form(key="contacto_real"):
    nombre = st.text_input("Nombre completo")
    email_usuario = st.text_input("Tu correo")
    mensaje = st.text_area("Tu consulta")
    submit_button = st.form_submit_button("Enviar Mensaje")

    if submit_button:
        if nombre and email_usuario and mensaje:
            payload = {"name": nombre, "email": email_usuario, "message": mensaje}
            res = requests.post(f"https://formsubmit.co/ajax/{mi_correo}", data=payload)
            if res.status_code == 200:
                st.success("¡Mensaje enviado! Revisa tu mail para confirmar la conexión la primera vez.")
            else:
                st.error("Error al enviar.")
        else:
            st.warning("Completa todos los campos.")

# 10. SIDEBAR
with st.sidebar:
    st.image(foto, width=150)
    st.write("Bienvenido a mi central de datos.")
    st.divider()
    st.markdown("#### 📚 Estudios Destacados")
    st.link_button("Teoría de Kalecki",
                   "https://drive.google.com/file/d/10raTTe9RnvrJb_SV_QwX7Mm2NxQxSocw/view?usp=sharing")
    st.link_button("Milton Friedman",
                   "https://drive.google.com/file/d/1prgMKDC_LzVDmbo9CQGOelH5O-bAZ9t3/view?usp=sharing")