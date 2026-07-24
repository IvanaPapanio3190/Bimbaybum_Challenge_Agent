import os
import glob
import streamlit as st
from google import genai
from google.genai import types
from pypdf import PdfReader

# Configuración de la página
st.set_page_config(
    page_title="BimBam Buy - Asistente RAG",
    page_icon="🛍️",
    layout="centered"
)

st.title("🛍️ BimBam Buy - Asistente Virtual")
st.caption("Consultá sobre catálogos, productos, políticas y envíos en tiempo real.")

# 1. Obtener la API Key desde los secretos de Streamlit
api_key = st.secrets.get("GOOGLE_API_KEY") or os.environ.get("GOOGLE_API_KEY")

if not api_key:
    st.error("⚠️ No se encontró la GOOGLE_API_KEY. Por favor, configúrala en los Secrets de Streamlit.")
    st.stop()

# Inicializar cliente de Gemini
client = genai.Client(api_key=api_key)

# 2. Cargar y extraer texto de todos los PDFs en la carpeta 'Data'
@st.cache_resource
def load_knowledge_base():
    pdf_paths = glob.glob("Data/*.pdf")
    combined_text = ""
    
    if not pdf_paths:
        st.warning("⚠️ No se encontraron archivos PDF dentro de la carpeta 'Data/'.")
        return ""

    for path in pdf_paths:
        try:
            reader = PdfReader(path)
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    combined_text += text + "\n"
        except Exception as e:
            st.error(f"Error al leer {path}: {e}")
            
    return combined_text

# Cargar base de conocimiento
with st.spinner("Cargando catálogo y base de conocimiento..."):
    context_text = load_knowledge_base()

# 3. Inicializar el historial de conversación en Streamlit
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "¡Hola! 👋 Soy el asistente virtual de BimBam Buy. ¿En qué puedo ayudarte hoy?"}
    ]

# Mostrar historial de mensajes previos
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# 4. Input del usuario
if user_input := st.chat_input("Escribí tu consulta aquí..."):
    # Guardar y mostrar mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Definir la instrucción de sistema con el contexto inyectado (RAG)
    system_instruction = f"""
    Sos un asistente de atención al cliente amable, profesional y eficiente para la tienda 'BimBam Buy'.
    Tu objetivo es responder las dudas del usuario basándote EXCLUSIVAMENTE en la siguiente base de conocimientos extraída de los documentos de la empresa:

    --- BASE DE CONOCIMIENTO ---
    {context_text}
    --- FIN BASE DE CONOCIMIENTO ---

    Reglas de respuesta:
    1. Sé cordial, claro y conciso.
    2. Si la información solicitada NO se encuentra en la base de conocimientos, responde amablemente indicando que no dispones de esa información en este momento y ofrece derivar la consulta con un asesor humano.
    3. No inventes precios, stock ni promociones que no estén descritas explícitamente en el texto.
    """

    # Construir el historial formateado para la API de Gemini
    formatted_contents = []
    for m in st.session_state.messages[-10:]:
        role_label = "user" if m["role"] == "user" else "model"
        formatted_contents.append(
            types.Content(
                role=role_label,
                parts=[types.Part.from_text(text=m["content"])]
            )
        )

    # Llamada a Gemini
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            try:
                response = client.models.generate_content(
                    model="gemini-1.5-flash-latest",
                    contents=formatted_contents,
                    config=types.GenerateContentConfig(
                        system_instruction=system_instruction,
                        temperature=0.3
                    )
                )
                bot_reply = response.text
                st.markdown(bot_reply)
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            except Exception as e:
                st.error(f"Ocurrió un error al procesar tu respuesta: {e}")
