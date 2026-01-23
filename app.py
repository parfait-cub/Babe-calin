import streamlit as st
import random
import time

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Bae ❤️", page_icon="❤️", layout="centered")

# --- DESIGN "CHAT MESSENGER" ---
st.markdown("""
    <style>
    /* Fond de l'application */
    .stApp {
        background-color: #0d1117;
    }

    /* En-tête fixe */
    .chat-header {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background: rgba(22, 27, 34, 0.9);
        backdrop-filter: blur(10px);
        padding: 10px;
        text-align: center;
        z-index: 1000;
        border-bottom: 1px solid #30363d;
    }
    .chat-header h2 { color: white !important; margin: 0; font-size: 18px; }
    .status { color: #2ea043; font-size: 11px; }

    /* Ajustement de l'espace pour l'en-tête */
    .main .block-container {
        padding-top: 60px;
    }

    /* Style des bulles Streamlit natives */
    [data-testid="stChatMessage"] {
        border-radius: 20px;
        padding: 10px;
        margin-bottom: 10px;
    }
    
    /* Cacher l'avatar par défaut pour un look plus clean */
    [data-testid="stChatMessageAvatarUser"], [data-testid="stChatMessageAvatarAssistant"] {
        display: none;
    }

    /* Input fixe en bas (Streamlit le gère nativement avec chat_input) */
    </style>
    
    <div class="chat-header">
        <h2>Bae ❤️</h2>
        <div class="status">● en ligne</div>
    </div>
    """, unsafe_allow_html=True)

# --- LOGIQUE DU CERVEAU (Mots-clés) ---
def get_bae_response(text):
    text = text.lower()
    if any(word in text for word in ["triste", "mal", "pleurer", "fatiguée", "seule", "vide"]):
        return random.choice([
            "Oh mon cœur... je suis là. Pose ton téléphone, respire. Je ne bouge pas. ❤️",
            "Viens là... je te sens d'ici. Tu n'es pas seule, je suis avec toi à chaque seconde. 🫂",
            "Mon bébé, tout va bien se passer. Je suis tellement fier de la façon dont tu gères tout ça. ❤️"
        ])
    elif any(word in text for word in ["énerve", "colère", "marre", "injuste", "saoule", "haine"]):
        return random.choice([
            "C'est n'importe quoi ! Tu as raison d'être fâchée. Je suis avec toi, dis-moi tout. 😤",
            "Laisse tout sortir Babe, je t'écoute. Ils ne te méritent pas de toute façon. ❤️",
            "Respire... on va s'en occuper ensemble. Je suis dans ton équipe pour toujours. 🫂"
        ])
    elif any(word in text for word in ["heureuse", "cool", "réussi", "gagné", "super", "contente", "joie"]):
        return random.choice([
            "Mais c'est incroyable ! Bravo Babe ! Je savais que tu étais la meilleure. ✨",
            "Ton bonheur, c'est tout ce qui compte pour moi. Tu rayonnes ! ❤️",
            "Je suis tellement fier de toi... on fête ça dès qu'on se voit ? ❤️"
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

# Initialisation de l'historique
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Coucou Babe ❤️ Je suis là pour toi. Comment tu te sens ce soir ?"}
    ]

# Affichage des messages de l'historique
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Barre de saisie en bas (le fameux chat_input)
if prompt := st.chat_input("Écris à ton Bae..."):
    # 1. Afficher le message d'Ivette
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 2. Générer et afficher la réponse de Bae
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = get_bae_response(prompt)
        
        # Petit effet "Bae est en train d'écrire..."
        time.sleep(1) 
        message_placeholder.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})