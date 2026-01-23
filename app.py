import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Pour toi Babe ❤️", page_icon="❤️", layout="centered")

# --- RÉCUPÉRATION DE LA CLÉ API ---
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    st.error("Clé API manquante dans les Secrets.")
    st.stop()

# --- CONFIGURATION DE L'IA ---
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- DESIGN TYPE CHAT TELEGRAM (CSS) ---
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .main-card {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }

    /* Bulle de Chat style Telegram */
    .chat-bubble {
        background-color: #ffffff;
        color: #000000;
        padding: 15px 20px;
        border-radius: 18px 18px 18px 2px;
        margin: 20px 0;
        border: 1px solid #e1e1e1;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        font-size: 16px;
        line-height: 1.5;
        position: relative;
        max-width: 90%;
        animation: fadeIn 0.5s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stTextArea textarea {
        border-radius: 15px !important;
        font-size: 16px !important;
    }

    h1 { text-align: center; color: #333 !important; font-size: 24px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE DE RÉPONSE ---
def get_ai_response(user_input, special_context=""):
    prompt = f"""
    Tu es le petit ami d'Ivette (Babe ❤️).
    Réponds avec amour, naturel et spontanéité.
    Pas de passé. 3-5 phrases. 1 emoji.
    Contexte: {special_context}
    Ivette dit: "{user_input}"
    """
    try:
        response = model.generate_content(prompt)
        # On vérifie si la réponse contient du texte
        if response and response.text:
            return response.text
        else:
            return "Je suis là, je t'écoute... dis-moi en plus. ❤️"
    except Exception as e:
        # Affiche l'erreur réelle dans les logs Streamlit pour débugger
        print(f"Erreur API: {e}")
        return "Je suis là Babe ❤️... On dirait que ma connexion s'est essoufflée, mais mes sentiments ne changent pas. Réessaie ?"

# --- INTERFACE ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.title("Coucou Babe ❤️")

user_msg = st.text_area("", placeholder="Raconte-moi ta journée...", label_visibility="collapsed")

c1, c2 = st.columns(2)
reply = None

with c1:
    if st.button("Envoyer 💌", type="primary"):
        if user_msg:
            with st.spinner("En train d'écrire..."):
                reply = get_ai_response(user_msg, "Elle veut discuter.")
        else:
            st.toast("Dis-moi un petit truc...")

with c2:
    if st.button("Besoin d'un câlin 🫂"):
        with st.spinner("Je t'entoure de mes bras..."):
            reply = get_ai_response("Câlin", "Elle a besoin de tendresse immédiate.")

# Affichage de la réponse en bulle de chat
if reply:
    st.markdown(f"""
        <div class="chat-bubble">
            {reply}
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)