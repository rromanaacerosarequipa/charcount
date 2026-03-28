import streamlit as st 
from streamlit_lottie import st_lottie
import requests
import random
import string

# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="CharCount",
    page_icon="🤖",
    layout="centered"
)

# ---------------------------------------------------
# ESTILO (TAL COMO TU LO TENÍAS)
# ---------------------------------------------------
st.markdown("""
<style>
/* … TU CSS COMPLETO TAL COMO LO ENVIASTE … */
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="blob"></div>', unsafe_allow_html=True)

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------
if "hostname" not in st.session_state:
    st.session_state.hostname = ""

if "impresora" not in st.session_state:
    st.session_state.impresora = ""

# ---------------------------------------------------
# FUNCIONES EXISTENTES
# ---------------------------------------------------
def autocompletar_hostname():
    st.session_state.hostname = {
        "LAPTOP": "PEPILA",
        "PC": "PEPIPC",
    }[st.session_state.tipo]

def autocompletar_impresora():
    st.session_state.impresora = {
        "PISCO": "CAASA-PISCO-",
        "LIMA": "CAASA-LIMA-",
        "CALLAO": "CAASA-CALLAO-",
        "LURIN": "CAASA-LURIN-",
        "AREQUIPA": "CAASA-AREQUIPA-"
    }[st.session_state.sede]

# ---------------------------------------------------
# NUEVAS FUNCIONES GENERADOR CONTRASEÑAS
# ---------------------------------------------------
def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + "$"
    contraseña = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("$")
    ]
    contraseña += random.choices(caracteres, k=longitud - 4)
    random.shuffle(contraseña)
    return ''.join(contraseña)

def generar_contraseñas(cantidad, longitud=12):
    return [generar_contraseña(longitud) for _ in range(cantidad)]

# ---------------------------------------------------
# SIDEBAR + NUEVA OPCIÓN
# ---------------------------------------------------
opcion = st.sidebar.selectbox(
    "Seleccione opción",
    ["Contador Hostname", "Contador Impresora", "Generador de Contraseñas"]
)

# =====================================================
# HOSTNAME
# =====================================================
if opcion == "Contador Hostname":
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.title("Contador Hostname")

    st.selectbox(
        "Tipo de equipo",
        ["LAPTOP", "PC"],
        key="tipo",
        on_change=autocompletar_hostname
    )

    hostname = st.text_input(
        "Hostname (máximo 15 caracteres)",
        key="hostname",
        max_chars=15
    )

    st.write(f"🔹 Caracteres: {len(hostname)}/15")

    if len(hostname) == 15:
        st.success("Límite alcanzado")

    if st.button("Validar"):
        if len(hostname) == 0:
            st.warning("Ingrese un hostname")
        else:
            st.success(f"Hostname válido: {hostname}")

    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# IMPRESORA
# =====================================================
if opcion == "Contador Impresora":

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.title("Contador Impresora")

    st.selectbox(
        "Seleccione la Sede",
        ["PISCO", "LIMA", "CALLAO", "LURIN", "AREQUIPA"],
        key="sede",
        on_change=autocompletar_impresora
    )

    impresora = st.text_input(
        "Nombre de la impresora (máximo 25 caracteres)",
        key="impresora",
        max_chars=25
    )

    st.write(f"🔹 Caracteres: {len(impresora)}/25")

    if len(impresora) == 25:
        st.success("Límite alcanzado")

    if st.button("Validar"):
        if len(impresora) == 0:
            st.warning("Ingrese el nombre de impresora")
        else:
            st.success(f"Nombre válido: {impresora}")

    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# NUEVA OPCIÓN: GENERADOR DE CONTRASEÑAS
# =====================================================
if opcion == "Generador de Contraseña":

    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.title("Generador de Contraseña")

    cantidad = st.number_input(
        "Cantidad de contraseña",
        min_value=1,
        max_value=200,
        value=5
    )

    longitud = st.number_input(
        "Longitud por contraseña",
        min_value=4,
        max_value=50,
        value=12
    )

    if st.button("Generar"):
        contraseñas = generar_contraseñas(cantidad, longitud)

        st.success(f"🔒 {cantidad} Contraseñas generadas:")

        for pwd in contraseñas:
            st.code(pwd)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------------------------------
# 🤖 ROBOT FLOTANTE
# ---------------------------------------------------
def load_lottie(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

robot = load_lottie("https://assets6.lottiefiles.com/packages/lf20_zrqthn6o.json")

st.markdown('<div class="robot-float">', unsafe_allow_html=True)
st_lottie(robot, height=500, key="robot")
st.markdown('</div>', unsafe_allow_html=True)
