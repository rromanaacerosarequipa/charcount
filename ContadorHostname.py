import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ---------------------------------------------------
# CONFIG
# ---------------------------------------------------
st.set_page_config(page_title="Contadores", layout="wide")

# ---------------------------------------------------
# ESTILO MODERNO PRO (AZURE)
# ---------------------------------------------------
st.markdown("""
<style>

/* 🌐 Fondo moderno */
body {
    background: radial-gradient(1200px 600px at 10% 10%, #1e3a8a33, transparent),
                radial-gradient(900px 500px at 90% 80%, #06b6d433, transparent),
                linear-gradient(135deg, #0f172a, #1e293b);
}

/* Contenedor */
.block-container {
    padding-top: 2rem;
}

/* 🧊 Card */
.glass {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
}

/* Títulos */
h1 {
    color: #e2e8f0;
    font-weight: 600;
}

/* Inputs */
.stTextInput input {
    background-color: #e2e8f0 !important;
    color: black !important;
    border-radius: 10px !important;
    border: 1px solid #cbd5e1 !important;
}

/* Select */
.stSelectbox div[data-baseweb="select"] {
    background-color: #e2e8f0 !important;
    border-radius: 10px !important;
}

/* Botón */
.stButton > button {
    background: linear-gradient(90deg, #2563eb, #3b82f6) !important;
    color: white !important;
    border-radius: 10px !important;
    padding: 8px 18px !important;
    border: none;
}

.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 8px 20px rgba(37,99,235,.35);
}

/* 🌈 Blob animado */
.blob {
    position: fixed;
    width: 260px;
    height: 260px;
    top: 20%;
    left: -80px;
    background: radial-gradient(circle, #3b82f6, transparent 70%);
    filter: blur(60px);
    opacity: .25;
    animation: blobMove 12s ease-in-out infinite;
}

@keyframes blobMove {
    0% { transform: translateY(0px) }
    50% { transform: translateY(60px) }
    100% { transform: translateY(0px) }
}

/* 🤖 Robot flotante */
.robot-float {
    position: fixed;
    bottom: 24px;
    right: 24px;
    animation: floatPro 6s ease-in-out infinite;
    z-index: 999;
}

@keyframes floatPro {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-12px); }
    100% { transform: translateY(0px); }
}

/* Glow */
.robot-float iframe {
    filter: drop-shadow(0 0 10px rgba(59,130,246,.5));
}

</style>
""", unsafe_allow_html=True)

# 🌈 Blob decorativo
st.markdown('<div class="blob"></div>', unsafe_allow_html=True)

# ---------------------------------------------------
# SESSION STATE
# ---------------------------------------------------
if "hostname" not in st.session_state:
    st.session_state.hostname = ""

if "impresora" not in st.session_state:
    st.session_state.impresora = ""

# ---------------------------------------------------
# FUNCIONES
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
# SIDEBAR
# ---------------------------------------------------
opcion = st.sidebar.selectbox(
    "Seleccione opción",
    ["Contador Hostname", "Contador Impresora"]
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
        st.success("✔ Límite alcanzado")

    if st.button("Validar Hostname"):
        if len(hostname) == 0:
            st.warning("Ingrese un hostname")
        elif len(hostname) <= 15:
            st.success(f"Hostname válido: {hostname}")
        else:
            st.error("Máximo 15 caracteres")

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
        st.success("✔ Límite alcanzado")

    if st.button("Validar"):
        if len(impresora) == 0:
            st.warning("Ingrese nombre de impresora")
        elif len(impresora) <= 25:
            st.success(f"Nombre válido: {impresora}")
        else:
            st.error("Máximo 25 caracteres")

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
