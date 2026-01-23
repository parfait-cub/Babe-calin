import streamlit as st
import google.generativeai as genai
import random
import time

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Bae ❤️", page_icon="❤️", layout="centered")

# --- BACKEND : CONFIGURATION IA & SÉCURITÉ ---
if "GEMINI_API_KEY" in st.secrets:
    try:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('gemini-1.5-flash')
        ia_active = True
    except:
        ia_active = False
else:
    ia_active = False

# --- LOGIQUE DE RÉPONSE (HYBRIDE IA + MANUEL) ---
def get_intelligent_response(user_input):
    # 1. Si l'IA est active, on l'utilise avec un prompt ultra-précis
    if ia_active:
        try:
            prompt = f"""
            Tu es le petit ami d'Ivette (Babe ❤️). Tu es calme, protecteur, un peu drôle et très aimant.
            Analyse son message : {user_input}
            
            RÈGLES :
            - Réponds comme si tu étais dans une inbox Telegram (court, 2-4 phrases).
            - Si elle est triste : sois un pilier, très doux.
            - Si elle est en colère : sois solidaire, ne la contredis pas.
            - Si elle est joyeuse : sois son premier fan, très enthousiaste.
            - Utilise 1 seul emoji (❤️, 🫂, ✨, 😤).
            - Ne parle JAMAIS du passé sauf si elle insiste.
            """
            response = model.generate_content(prompt)
            return response.text
        except:
            pass # Si l'IA échoue, on passe au manuel ci-dessous

    # 2. Système de secours (Si l'IA bug)
    text = user_input.lower()
    if any(w in text for w in ["triste", "mal", "pleurer", "fatigue", "seul"]):
        return "Je sens que c'est lourd ce soir... pose tout, je suis là. Respire avec moi Babe ❤️"
    elif any(w in text for w in ["câlin", "calin", "bras", "hug"]):
        return "Viens là... je ferme les yeux et je te serre très fort. Tu sens ? 🫂"
    else:
        return "Je t'écoute mon cœur, dis-moi tout ce que tu as sur le cerveau ❤️"

# --- FRONTEND : DESIGN VIOLET & SPARKS ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #1a0b2e 0%, #0d1117 100%); color: white; }
    
    .chat-header {
        position: fixed; top: 0; left: 0; width: 100%; background: rgba(45, 20, 70, 0.9);
        backdrop-filter: blur(15px); padding: 15px; text-align: center; z-index: 1000;
        border-bottom: 1px solid rgba(155, 89, 182, 0.3);
    }
    .chat-header h2 { color: #e0b0ff !important; margin: 0; font-size: 20px; }
    
    /* Bulles Telegram Custom */
    [data-testid="stChatMessage"] { background-color: transparent !important; }
    
    .st-emotion-cache-1ghh3y3 { 
        background-color: #4a148c !important; color: white !important;
        border-radius: 18px 18px 18px 4px !important; border: 1px solid #7b1fa2 !important;
    }
    .st-emotion-cache-janbn0 { 
        background-color: #2c3e50 !important; color: white !important;
        border-radius: 18px 18px 4px 18px !important;
    }
    [data-testid="stChatMessageAvatarUser"], [data-testid="stChatMessageAvatarAssistant"] { display: none; }

    /* Input fixe en bas */
    [data-testid="stChatInput"] {
        border-radius: 30px !important; background-color: #161b22 !important;
        border: 1px solid #4a148c !important;
    }
    </style>
    <div class="chat-header"><h2>Bae ❤️</h2><div style="color:#2ecc71; font-size:11px;">● en ligne</div></div>
    """, unsafe_allow_html=True)

# --- GESTION DE LA CONVERSATION ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Coucou Babe ❤️ Je suis là. Comment s'est passée ta journée ?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Écris à ton Bae..."):
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        with st.spinner(""):
            full_response = get_intelligent_response(prompt)
            time.sleep(1) # Simulation de frappe
            st.write(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})