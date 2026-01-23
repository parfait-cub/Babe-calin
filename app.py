import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Pour toi Babe ❤️", page_icon="❤️", layout="centered")

# --- TA CLÉ API (À REMPLACER) ---
GEMINI_API_KEY = st.secrets["GEMINI_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# --- DESIGN PERSONNALISÉ (CSS) ---
st.markdown("""
    <style>
    /* Fond animé et style global */
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
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.3);
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }

    /* Titres et textes */
    h1, h3 {
        color: #4a4a4a !important;
        text-align: center;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Customisation de l'input */
    .stTextArea textarea {
        border-radius: 15px !important;
        border: 1px solid #ddd !important;
    }

    /* Boutons personnalisés */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        transition: all 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

# --- LOGIQUE DU CERVEAU (PROMPT) ---
def get_ai_response(user_input, special_context=""):
    prompt = f"""
    Tu es le petit ami idéal pour Ivette (Babe ❤️).
    Analyse son émotion : Joie, Colère, Tristesse ou Fatigue.
    
    RÈGLES :
    - Ton humain, chaleureux, spontané.
    - Jamais de mention du passé douloureux.
    - 3 à 5 phrases max.
    - 1 ou 2 emojis max (🫂 ou ❤️).
    
    Contexte : {special_context}
    Message d'Ivette : "{user_input}"
    """
    response = model.generate_content(prompt)
    return response.text

# --- INTERFACE UTILISATEUR ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)
st.title("Comment tu te sens, Babe ? ❤️")

# Champ de texte
user_msg = st.text_area("", placeholder="Raconte-moi, ou vide ton sac...", label_visibility="collapsed")

col1, col2 = st.columns(2)

with col1:
    if st.button("Envoyer 💌", type="primary"):
        if user_msg:
            with st.spinner("Je t'écoute..."):
                reply = get_ai_response(user_msg, "Réponse émotionnelle adaptée")
                st.write("---")
                st.write(reply)
        else:
            st.warning("Dis-moi quelque chose Babe ❤️")

with col2:
    if st.button("Juste un câlin 🫂"):
        with st.spinner("Je suis là..."):
            reply = get_ai_response("Je veux juste un câlin", "Elle a besoin de douceur extrême, pas de questions, juste de l'amour.")
            st.write("---")
            st.write(reply)

st.markdown("""
    <div style="text-align: center; margin-top: 20px; font-size: 0.8em; color: #666;">
        🔒 Ton espace privé. Rien n'est enregistré.
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)