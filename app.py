import streamlit as st
import random

st.set_page_config(page_title="Bae ❤️", page_icon="❤️", layout="centered")

# 🌸 Couleurs et style CSS
st.markdown(
    """
    <style>
    body { background-color: #f3f0f8; font-family: system-ui, sans-serif; }
    .bubble { 
        background-color: #9b5de5; 
        color: white; 
        padding: 12px 18px; 
        border-radius: 20px; 
        margin: 8px 0; 
        display: inline-block; 
        max-width: 70%;
        word-wrap: break-word;
        transition: all 0.2s ease-in-out;
    }
    .user { background-color: #c4b5fd; color: black; margin-left: auto; }
    .hug-button { background-color: #7f3fbf; color: white; border:none; padding:8px 12px; border-radius:12px; cursor:pointer; }
    </style>
    """, unsafe_allow_html=True
)

# 🌟 Mémoire courte
if "memory" not in st.session_state:
    st.session_state.memory = []

# 🎯 Réponses par contexte (simplifié, tu peux ajouter plus de phrases)
responses = {
    "triste": [
        "Viens là Babe ❤️… je suis là avec toi.",
        "Je te serre fort dans mes bras 🫂… respire doucement.",
        "Ça va aller… je suis juste là pour toi 🫂",
        "Je t’écoute Babe ❤️… prends ton temps."
    ],
    "stresse": [
        "Respire un peu Babe ❤️… je suis là.",
        "Tout va aller… je suis avec toi 🫂",
        "Doucement… tu n’es pas seule ❤️",
        "Relax Babe ❤️… je veille sur toi."
    ],
    "calin": [
        "Viens là Babe ❤️… juste un câlin",
        "Je te prends dans mes bras 🫂… je reste avec toi",
        "Babe ❤️… je t’entoure de douceur 🫂",
        "Je te serre fort… je suis là pour toi ❤️"
    ],
    "neutre": ["Je suis là Babe ❤️… parle-moi un peu 🫂"]
}

# 🔍 Détection simple du contexte
def detect_context(msg):
    msg = msg.lower()
    if any(w in msg for w in ["triste","mal","pleure"]): return "triste"
    if any(w in msg for w in ["stress","angoisse","nerveux"]): return "stresse"
    if any(w in msg for w in ["câlin","serre-moi"]): return "calin"
    return "neutre"

st.title("💜 Bae ❤️")

# 🌸 Zone d'entrée
user_msg = st.text_input("Bae écrit :")

# 🫂 Bouton câlin
if st.button("Juste un câlin 🫂"):
    st.session_state.memory.append("Câlin demandé")
    reply = random.choice(responses["calin"])
    st.session_state.memory.append(f"Bae : {reply}")
    st.markdown(f'<div class="bubble">{reply}</div>', unsafe_allow_html=True)

# 📨 Envoyer message
if st.button("Envoyer") and user_msg:
    st.session_state.memory.append(f"Bae écrit : {user_msg}")
    context = detect_context(user_msg)
    reply = random.choice(responses.get(context, responses["neutre"]))

    # Ajouter rappel mémoire
    if len(st.session_state.memory) > 1:
        prev = st.session_state.memory[-2]
        reply += f" (je me souviens que tu as dit : '{prev}')"

    st.session_state.memory.append(f"Bae ❤️ : {reply}")

# 🌟 Affichage des messages en bulle
for msg in st.session_state.memory:
    # Ajuster largeur selon longueur du message
    width = min(70 + len(msg)//2, 90)
    st.markdown(f'<div class="bubble" style="max-width:{width}%;">{msg}</div>', unsafe_allow_html=True)
