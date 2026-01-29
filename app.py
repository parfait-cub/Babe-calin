import streamlit as st
import random
import time
from datetime import datetime

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Bae ❤️", page_icon="❤️", layout="centered")

# --- DATES IMPORTANTES ---
date_rencontre = datetime(2023, 7, 1)
maintenant = datetime.now()
diff = maintenant - date_rencontre

# Date de la Saint-Valentin 2026
saint_valentin = datetime(2026, 2, 14)
jours_restants_valentin = (saint_valentin - maintenant).days + 1

# --- SURNOMS ---
surnoms = ["Babe", "Ivette", "mon cœur", "ma chérie", "mon amour", "ma princesse", "ma belle"]

def get_surnom():
    return random.choice(surnoms)

# --- LE CERVEAU LOGIQUE ---
def get_manual_brain_response(user_input):
    text = user_input.lower()
    database = {
        "fatigue": {
            "keywords": ["fatigué", "fatigue", "épuisé", "dodo", "sommeil", "naze", "crevé", "dormir", "épuisée"],
            "replies": [{"text": f"Oh {get_surnom()}... pose tout et repose-toi avec moi. ❤️", "emoji": "😴"}]
        },
        "amour_manque": {
            "keywords": ["je t'aime", "t'aime", "love", "manque", "besoin", "voir", "viens", "miss"],
            "replies": [{"text": "Je t'aime encore plus, tu n'as même pas idée... ❤️", "emoji": "💖"}]
        }
    }
    for category in database:
        if any(word in text for word in database[category]["keywords"]):
            return random.choice(database[category]["replies"])
    return {"text": f"Je t'écoute {get_surnom()}... ❤️", "emoji": "🫂"}

# --- CSS (Design Corrigé) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300..700&display=swap');
    body { font-family: 'Quicksand', sans-serif; }
    .stApp { background: linear-gradient(135deg, #1a0b2e 0%, #0d1117 100%) !important; color: white !important; }
    .chat-header { 
        position: fixed; top: 0; left: 0; width: 100%; background: rgba(74, 20, 140, 0.3);
        backdrop-filter: blur(15px); padding: 15px; text-align: center; z-index: 1000;
        border-bottom: 2px solid rgba(224, 176, 255, 0.2);
    }
    .chat-header h2 { color: #e0b0ff !important; margin: 0; }
    .countdown-box { background: rgba(255, 255, 255, 0.08); padding: 15px; border-radius: 15px; border: 2px dashed #e0b0ff; text-align: center; margin-top: 100px; }
    .stButton > button { background: rgba(155, 89, 182, 0.2) !important; border: 2px solid #9b59b6 !important; color: white !important; border-radius: 20px !important; }
</style>
<div class="chat-header">
    <h2>💜 Bae</h2>
    <div style="color: #2ecc71; font-size: 12px;">● en ligne</div>
</div>
""", unsafe_allow_html=True)

# --- ESPACEMENT POUR LE HEADER ---
st.markdown("<br><br><br>", unsafe_allow_html=True)

# --- COMPTE À REBOURS ---
if jours_restants_valentin > 0:
    st.markdown(f'<div class="countdown-box">💝 <b>J-{jours_restants_valentin} jours</b> avant ta surprise ! 🌹</div>', unsafe_allow_html=True)
else:
    st.balloons()
    st.markdown('<div style="background: red; padding: 20px; border-radius: 20px; text-align: center;">❤️ JOYEUSE SAINT-VALENTIN ❤️</div>', unsafe_allow_html=True)

# --- BOUTONS ---
col1, col2 = st.columns(2)
with col1:
    if st.button("✨ Notre coin secret"):
        st.balloons()
        st.video("Souvenir.mp4")
with col2:
    if st.button("💌 Message du jour"):
        st.success("Tu es la plus belle rencontre de ma vie. ✨")

# --- CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": f"Coucou {get_surnom()} ❤️", "emoji": "👋"}]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.write(f"{m.get('emoji', '')} {m['content']}")

if prompt := st.chat_input("Écris à ton Bae..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"): st.write(prompt)
    with st.chat_message("assistant"):
        res = get_manual_brain_response(prompt)
        st.write(f"{res['emoji']} {res['text']}")
    st.session_state.messages.append({"role": "assistant", "content": res["text"], "emoji": res["emoji"]})
