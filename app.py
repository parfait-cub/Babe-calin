import streamlit as st
import random
import time

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Bae ❤️", page_icon="❤️", layout="centered")

# --- DESIGN "ULTRA-PREMIUM VIOLET & SPARKS" ---
st.markdown("""
    <style>
    /* Fond de l'application avec dégradé violet profond */
    .stApp {
        background: radial-gradient(circle at center, #1a0b2e 0%, #0d1117 100%);
        color: white;
    }

    /* Animation d'étincelles (Sparks) */
    @keyframes sparks {
        0% { opacity: 0; transform: translateY(0) scale(1); }
        50% { opacity: 0.8; }
        100% { opacity: 0; transform: translateY(-100px) scale(0.5); }
    }
    
    .spark {
        position: fixed;
        width: 4px;
        height: 4px;
        background: #9b59b6;
        border-radius: 50%;
        pointer-events: none;
        animation: sparks 3s linear infinite;
        z-index: 0;
    }

    /* En-tête de la discussion (Style iOS/Telegram) */
    .chat-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: rgba(45, 20, 70, 0.8);
        backdrop-filter: blur(15px);
        padding: 15px;
        text-align: center;
        z-index: 1000;
        border-bottom: 1px solid rgba(155, 89, 182, 0.3);
    }
    .chat-header h2 { color: #e0b0ff !important; margin: 0; font-size: 20px; font-weight: 600; }
    .status { color: #2ecc71; font-size: 11px; font-weight: bold; }

    /* Bulles de Chat Style Telegram */
    [data-testid="stChatMessage"] {
        background-color: transparent !important;
        border: none !important;
        margin-bottom: 5px !important;
    }

    /* Bulle Bae (Reçu - Violette) */
    .st-emotion-cache-1ghh3y3 { 
        background-color: #4a148c !important; /* Violet foncé */
        color: white !important;
        border-radius: 18px 18px 18px 4px !important;
        border: 1px solid #7b1fa2 !important;
        max-width: 80%;
        padding: 10px 15px !important;
    }

    /* Bulle Ivette (Envoyé - Couleur complémentaire) */
    .st-emotion-cache-janbn0 { 
        background-color: #2c3e50 !important; /* Gris-bleu sombre */
        color: white !important;
        border-radius: 18px 18px 4px 18px !important;
        max-width: 80%;
        margin-left: auto;
        padding: 10px 15px !important;
    }

    /* Cacher les avatars par défaut */
    [data-testid="stChatMessageAvatarUser"], [data-testid="stChatMessageAvatarAssistant"] {
        display: none;
    }

    /* Barre de saisie noire arrondie */
    [data-testid="stChatInput"] {
        border-radius: 30px !important;
        background-color: #161b22 !important;
        border: 1px solid #4a148c !important;
        padding: 5px 15px !important;
    }

    /* Footer / Hint */
    .footer-note {
        text-align: center;
        font-size: 10px;
        color: #7b1fa2;
        margin-top: 20px;
    }

    </style>
    
    <div class="spark" style="left:10%; top:20%; animation-delay: 0s;"></div>
    <div class="spark" style="left:30%; top:50%; animation-delay: 1s;"></div>
    <div class="spark" style="left:70%; top:80%; animation-delay: 2s;"></div>
    <div class="spark" style="left:90%; top:10%; animation-delay: 0.5s;"></div>

    <div class="chat-header">
        <h2>Bae ❤️</h2>
        <div class="status">● en ligne</div>
    </div>
    """, unsafe_allow_html=True)

# --- LOGIQUE DU CERVEAU ---
def get_bae_response(text):
    text = text.lower()
    if any(word in text for word in ["triste", "mal", "pleurer", "fatiguée", "seule", "vide"]):
        return random.choice([
            "Oh mon cœur... je suis là. Pose ton téléphone, respire. Je ne bouge pas. ❤️",
            "Viens là... je te sens d'ici. Tu n'es pas seule, je suis avec toi à chaque seconde. 🫂",
            "Mon bébé, tout va bien se passer. Je suis tellement fier de toi. ❤️"
        ])
    elif any(word in text for word in ["câlin", "calin", "bras", "bisou", "manque", "hug"]):
        return random.choice([
            "Je ferme les yeux et je te serre très fort... Tu sens ? 🫂",
            "Câlin virtuel infini pour ma Ivette préférée. Je ne te lâche plus. ❤️",
            "Si j'étais là, tu serais déjà dans mes bras. Vivement... 🫂"
        ])
    else:
        return random.choice([
            "Je t'écoute Babe, continue... ❤️",
            "T'es incroyable, tu le sais ça ? ✨",
            "Je suis tellement bien quand on discute comme ça. ❤️",
            "Dis-moi tout, je suis tout à toi. 🫂"
        ])

# --- GESTION DE LA CONVERSATION ---

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Coucou Babe ❤️ Je suis là. Comment tu te sens ?"}
    ]

# Affichage des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Barre de saisie fixe en bas
if prompt := st.chat_input("Écris à ton Bae..."):
    # 1. Message d'Ivette
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Réponse de Bae
    with st.chat_message("assistant"):
        full_response = get_bae_response(prompt)
        time.sleep(0.8) # Petit délai pour l'effet "en train d'écrire"
        st.write(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})

st.markdown('<div class="footer-note">Ton espace privé rien qu\'à toi ✨</div>', unsafe_allow_html=True)