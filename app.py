import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Pour toi Babe ❤️", page_icon="❤️", layout="centered")

# --- RÉCUPÉRATION DE LA CLÉ API ---
# Assure-toi que dans tes Secrets Streamlit, le nom est bien GEMINI_API_KEY
if "GEMINI_API_KEY" in st.secrets:
    API_KEY = st.secrets["GEMINI_API_KEY"]
else:
    st.error("Erreur : La clé 'GEMINI_API_KEY' n'est pas configurée dans les Secrets.")
    st.stop()

# --- CONFIGURATION DE L'IA ---
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- DESIGN PERSONNALISÉ (CSS) ---
st.markdown("""
    <style>
    /* Fond animé global */
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

    /* Style du conteneur principal */
    .main-card {
        background: rgba(255, 255, 255, 0.88);
        backdrop-filter: blur(12px);
        padding: 30px;
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.4);
        box-shadow: 0 12px 40px rgba(0,0,0,0.15);
        margin-top: 20px;
    }

    /* Titres */
    h1 {
        color: #4a4a4a !important;
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
        font-weight: 700;
        margin-bottom: 25px;
    }

    /* Champ de texte */
    .stTextArea textarea {
        border-radius: 16px !important;
        border: 1px solid #eee !important;
        background-color: rgba(255, 255, 255, 0.5) !important;
        font-size: 16px !important;
    }

    /* Boutons */
    .stButton>button {
        width: 100%;
        border-radius: 14px;
        height: 3.2em;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE DE RÉPONSE ---
def get_ai_response(user_input, special_context=""):
    prompt = f"""
    Tu es le petit ami idéal pour Ivette (tu l'appelles "Babe ❤️").
    Analyse son émotion : Joie, Colère, Tristesse ou Fatigue.
    
    TON STYLE :
    - Très humain, chaleureux, spontané.
    - Jamais de mention du passé douloureux (interdit).
    - Entre 3 et 5 phrases max.
    - Utilise 1 seul emoji (❤️ ou 🫂).
    
    CONTEXTE : {special_context}
    MESSAGE D'IVETTE : "{user_input}"
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return "Je suis là Babe ❤️... j'ai juste un petit souci technique, mais je ne bouge pas."

# --- INTERFACE UTILISATEUR ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.title("Comment tu te sens, Babe ? ❤️")

user_msg = st.text_area("", placeholder="Dis-moi tout, je t'écoute...", label_visibility="collapsed")

col1, col2 = st.columns(2)

with col1:
    if st.button("Envoyer 💌", type="primary"):
        if user_msg.strip():
            with st.spinner("Je réfléchis..."):
                reply = get_ai_response(user_msg, "Réponse adaptée à son émotion actuelle.")
                st.info(reply)
        else:
            st.toast("Écris-moi un petit mot Babe ❤️")

with col2:
    if st.button("Juste un câlin 🫂"):
        with st.spinner("Je me rapproche..."):
            reply = get_ai_response("Je ne veux pas parler, juste un câlin.", "Elle a besoin d'un moment de silence et de tendresse pure.")
            st.success(reply)

st.markdown("""
    <div style="text-align: center; margin-top: 25px; font-size: 0.85em; color: #777;">
        🔒 Ton espace privé à toi.
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)