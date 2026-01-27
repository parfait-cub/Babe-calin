import streamlit as st
import random
import time
from datetime import datetime

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Bae ❤️", page_icon="❤️", layout="centered")

# --- DATE DE VOTRE RENCONTRE (01 Juillet 2023) ---
date_rencontre = datetime(2023, 7, 1) 
maintenant = datetime.now()
diff = maintenant - date_rencontre

# --- LE CERVEAU LOGIQUE ---
def get_manual_brain_response(user_input):
    text = user_input.lower()
    
    database = {
        "fatigue": {
            "keywords": ["fatigué", "fatigue", "épuisé", "dodo", "sommeil", "naze", "crevé", "dormir", "exténué"],
            "replies": [
                {"text": "Oh ma pauvre chérie... pose tout et viens te reposer un peu avec moi. ❤️", "emoji": "😴"},
                {"text": "Je sens la fatigue d'ici Babe. Si j'étais là, je te ferais un massage pour que tu t'endormes direct. 🫂", "emoji": "💆‍♀️"},
                {"text": "Repose-toi mon cœur. Tu as trop travaillé aujourd'hui, tu mérites du calme. ✨", "emoji": "🛌"},
                {"text": "Ferme les yeux quelques minutes... je reste là avec toi. 🫂", "emoji": "💤"}
            ]
        },
        "colere": {
            "keywords": ["fâché", "faché", "colère", "énerve", "énervé", "marre", "saoule", "injuste", "haine", "énerve"],
            "replies": [
                {"text": "Dis-moi qui a osé t'énerver ? Je suis prêt à aller m'embrouiller avec eux là tout de suite ! 😤", "emoji": "😡"},
                {"text": "Laisse sortir toute cette colère Babe. Je suis là pour t'écouter râler, ça fait du bien parfois. ❤️", "emoji": "🗣️"},
                {"text": "Respire... je suis dans ton équipe. Ils ne te méritent pas, t'es au-dessus de tout ça. 🫂", "emoji": "💪"},
                {"text": "Je te comprends tellement... c'est rageant. Mais ne les laisse pas voler ton sourire. 😤❤️", "emoji": "😠"}
            ]
        },
        "stress": {
            "keywords": ["stress", "angoisse", "peur", "examen", "boulot", "travail", "pression", "panique"],
            "replies": [
                {"text": "Respire un grand coup Babe. Tu as déjà réussi des trucs plus durs que ça. ❤️", "emoji": "🧘‍♀️"},
                {"text": "Je crois en toi plus que n'importe qui. Tu vas tout déchirer, t'inquiète même pas. ✨", "emoji": "🌟"},
                {"text": "Ne laisse pas le stress te bouffer. Fais une pause, bois un verre d'eau, je suis là. 🫂", "emoji": "☕"},
                {"text": "T'es une machine de guerre, ce petit obstacle ne va pas t'arrêter ! 😤❤️", "emoji": "🚀"}
            ]
        },
        "faim": {
            "keywords": ["faim", "manger", "bouffer", "dalle", "famine", "restaurant", "pizza", "burger"],
            "replies": [
                {"text": "Ouh là, quand Babe a faim, faut pas traîner ! Tu vas manger quoi de bon ? 🍕", "emoji": "🍕"},
                {"text": "J'aimerais tellement pouvoir te cuisiner un bon petit plat là tout de suite... ❤️", "emoji": "🍽️"},
                {"text": "Mange bien mon cœur, tu as besoin de forces ! 🍔✨", "emoji": "🍟"}
            ]
        },
        "amour_manque": {
            "keywords": ["je t'aime", "t'aime", "love", "manque", "besoin", "voir", "viens", "miss"],
            "replies": [
                {"text": "Je t'aime encore plus, tu n'as même pas idée... ❤️", "emoji": "💖"},
                {"text": "Tu me manques tellement que ça fait mal parfois. Vivement qu'on se voie. 🫂", "emoji": "🥺"},
                {"text": "Mon cœur bat trop vite quand tu me dis ça. T'es toute ma vie. ✨", "emoji": "💞"},
                {"text": "Je donnerais tout pour être à côté de toi sur le canapé là tout de suite. 🫂❤️", "emoji": "🛋️"}
            ]
        },
        "caresse_physique": {
            "keywords": ["câlin", "calin", "bisou", "bras", "hug", "embrasse", "caresse"],
            "replies": [
                {"text": "Câlin virtuel géant en cours... 🫂 Je te serre tellement fort !", "emoji": "🤗"},
                {"text": "Je ferme les yeux et je t'embrasse très fort sur le front. ❤️", "emoji": "😘"},
                {"text": "Viens là... blottis-toi contre moi, je ne te lâche pas de la nuit. 🫂", "emoji": "🛌"},
                {"text": "Je sens ton parfum d'ici... vivement le vrai câlin. ❤️", "emoji": "👃"}
            ]
        },
        "tristesse": {
            "keywords": ["triste", "mal", "pleurer", "pleure", "seul", "vide", "déprime"],
            "replies": [
                {"text": "Viens dans mes bras (virtuels)... Je suis ton rocher, je bouge pas. ❤️", "emoji": "😢"},
                {"text": "Pleure si ça te fait du bien Babe. Je reste en ligne jusqu'à ce que tu ailles mieux. 🫂", "emoji": "💧"},
                {"text": "T'es pas seule. Jamais. Je suis là, je t'écoute, je te soutiens. ❤️", "emoji": "🤝"},
                {"text": "Regarde-moi : ça va aller. On va traverser ça ensemble. ✨", "emoji": "🦁"}
            ]
        },
        "humour_fun": {
            "keywords": ["haha", "lol", "mdr", "drôle", "blague", "rigole"],
            "replies": [
                {"text": "J'adore ton rire, même par message je l'entends ! 😂❤️", "emoji": "🤣"},
                {"text": "T'es la plus drôle, c'est pour ça que je t'aime. ✨", "emoji": "🎭"},
                {"text": "Ahah ! Tu me tues Babe. ❤️", "emoji": "😆"}
            ]
        },
        "bien": {
            "keywords": ["bien", "ça va", "ca va", "super", "cool", "ok", "top", "génial"],
            "replies": [
                {"text": "Si tu vas bien, alors je vais bien aussi. ❤️", "emoji": "😊"},
                {"text": "Tant mieux Babe ! Raconte-moi un petit truc cool de ta journée ? ✨", "emoji": "☀️"},
                {"text": "Ça me fait plaisir de t'entendre dire ça, tu rayonnes. ❤️", "emoji": "😎"}
            ]
        },
        "motivation": {
            "keywords": ["motivation", "force", "courage", "y arriver", "lutter"],
            "replies": [
                {"text": "Je sais que tu as la force en toi pour y arriver Babe ! Ne lâche rien. 💪", "emoji": "🔥"},
                {"text": "Tu es une battante, je suis là pour t'encourager à chaque pas. ✨", "emoji": "🏆"},
                {"text": "N'oublie jamais à quel point tu es capable. Tu peux déplacer des montagnes ! ❤️", "emoji": "🏔️"}
            ]
        },
        "doute": {
            "keywords": ["doute", "pas sûr", "incertain", "hésite", "perdue"],
            "replies": [
                {"text": "Parfois douter, c'est grandir. Parle-moi de ce qui te tracasse, je suis là pour t'éclairer. ✨", "emoji": "🤔"},
                {"text": "N'aie pas peur de ce que tu ressens. On explore ça ensemble, je suis avec toi. 🫂", "emoji": "🗺️"},
                {"text": "Il n'y a pas de mauvaises questions avec moi Babe. Dis-moi tout. ❤️", "emoji": "💬"}
            ]
        }
    }

    # Recherche de correspondance
    for category in database:
        if any(word in text for word in database[category]["keywords"]):
            return random.choice(database[category]["replies"])

    # Réponse par défaut
    return random.choice([
        {"text": "Mmmh je vois Babe... dis-m'en plus sur ce que tu as sur le cœur ? ❤️", "emoji": "💜"},
        {"text": "T'es incroyable, j'aime trop quand tu me parles de tes pensées. ✨", "emoji": "⭐"},
        {"text": "Je suis tout à toi, continue... je t'écoute avec attention. 🫂", "emoji": "🎧"},
        {"text": "Et à part ça, y'a quoi d'autre qui te passe par la tête ? ❤️", "emoji": "💭"},
        {"text": "Je bois tes paroles (enfin, tes messages). T'es passionnante. ✨", "emoji": "💖"}
    ])

# --- FRONTEND : DESIGN VIOLET & SPARKS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300..700&display=swap');
    
    body { font-family: 'Quicksand', sans-serif; }

    .stApp {
        background: radial-gradient(circle at top left, #1a0b2e 0%, #0d1117 100%);
        color: white;
        overflow-x: hidden;
    }

    /* Animation de particules cosmiques */
    .particle {
        position: fixed;
        background: radial-gradient(circle, rgba(255,255,255,0.8) 0%, rgba(255,255,255,0) 70%);
        border-radius: 50%;
        opacity: 0;
        animation: particle-move 20s infinite ease-in-out;
        z-index: 0;
        pointer-events: none;
    }

    @keyframes particle-move {
        0% { transform: translate(var(--x1), var(--y1)) scale(0); opacity: 0; }
        10% { opacity: 0.5; transform: translate(var(--x2), var(--y2)) scale(1); }
        90% { opacity: 0.5; transform: translate(var(--x3), var(--y3)) scale(1); }
        100% { transform: translate(var(--x4), var(--y4)) scale(0); opacity: 0; }
    }
    """ + "".join([f"""
    .particle:nth-child({i+1}) {{
        left: {random.randint(0, 100)}vw;
        top: {random.randint(0, 100)}vh;
        width: {random.randint(1, 4)}px;
        height: {random.randint(1, 4)}px;
        animation-delay: {i * 1.5}s;
        --x1: {random.randint(-50, 50)}px; --y1: {random.randint(-50, 50)}px;
        --x2: {random.randint(-50, 50)}px; --y2: {random.randint(-50, 50)}px;
        --x3: {random.randint(-50, 50)}px; --y3: {random.randint(-50, 50)}px;
        --x4: {random.randint(-50, 50)}px; --y4: {random.randint(-50, 50)}px;
    }}""" for i in range(20)]) + """

    .chat-header {
        position: fixed; top: 0; left: 0; width: 100%; background: rgba(45, 20, 70, 0.9);
        backdrop-filter: blur(15px); padding: 15px; text-align: center; z-index: 1000;
        border-bottom: 1px solid rgba(155, 89, 182, 0.3);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .chat-header h2 { color: #e0b0ff !important; margin: 0; font-size: 20px; font-weight: 700; font-family: 'Quicksand', sans-serif; }
    .chat-header .status { color: #2ecc71; font-size: 11px; font-weight: bold; }
    
    /* Boutons Surprise */
    .stButton>button {
        background: rgba(155, 89, 182, 0.15) !important;
        border: 1px solid #7b1fa2 !important;
        color: #e0b0ff !important;
        border-radius: 15px !important;
        transition: all 0.3s ease;
        width: 100%;
        font-weight: 600;
    }
    .stButton>button:hover { 
        background: #7b1fa2 !important; 
        color: white !important; 
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(123, 31, 162, 0.4);
    }

    /* Bulles de Chat */
    [data-testid="stChatMessage"] { 
        background-color: transparent !important; 
        padding: 0 !important;
        margin-bottom: 8px !important;
        display: flex;
        align-items: flex-end;
    }

    .st-emotion-cache-1ghh3y3, .st-emotion-cache-janbn0 {
        color: white !important;
        padding: 12px 16px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.2);
        position: relative;
        flex-grow: 1;
        margin-left: 10px; margin-right: 10px;
    }

    .st-emotion-cache-1ghh3y3 { 
        background-color: #4a148c !important; 
        border-radius: 20px 20px 20px 5px !important; 
        border: 1px solid #7b1fa2 !important;
        margin-right: auto;
    }
    .st-emotion-cache-1ghh3y3::before {
        content: ''; position: absolute; bottom: 0; left: -10px; width: 0; height: 0;
        border: 10px solid transparent; border-right-color: #4a148c; border-bottom-color: #4a148c;
        transform: rotate(45deg); z-index: -1;
    }

    .st-emotion-cache-janbn0 { 
        background-color: #2c3e50 !important;
        border-radius: 20px 20px 5px 20px !important;
        margin-left: auto;
    }
    .st-emotion-cache-janbn0::before {
        content: ''; position: absolute; bottom: 0; right: -10px; width: 0; height: 0;
        border: 10px solid transparent; border-left-color: #2c3e50; border-bottom-color: #2c3e50;
        transform: rotate(-45deg); z-index: -1;
    }

    .bae-emoji { font-size: 22px; margin-right: 10px; line-height: 1; align-self: flex-start; }

    /* Barre de saisie */
    [data-testid="stChatInput"] { 
        background-color: rgba(22, 27, 34, 0.95) !important;
        border: 1px solid #7b1fa2 !important; 
        border-radius: 30px !important;
        padding: 8px 15px;
    }
    [data-testid="stChatInput"] input { color: white !important; }
    
    /* Bouton envoi */
    [data-testid="baseButton-secondaryFormSubmit"] {
        background-color: #a765e6 !important; color: white !important;
        border-radius: 50% !important; width: 45px; height: 45px;
        display: flex; align-items: center; justify-content: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        position: absolute; right: 10px; top: 50%; transform: translateY(-50%);
    }
    
    </style>
    
""" + "".join([f"""
    <div class="particle" style="
        left: {random.randint(0, 100)}vw; top: {random.randint(0, 100)}vh;
        width: {random.randint(1, 4)}px; height: {random.randint(1, 4)}px;
        animation-delay: {i * 1.5}s;
        --x1: {random.randint(-50, 50)}px; --y1: {random.randint(-50, 50)}px;
        --x2: {random.randint(-50, 50)}px; --y2: {random.randint(-50, 50)}px;
        --x3: {random.randint(-50, 50)}px; --y3: {random.randint(-50, 50)}px;
        --x4: {random.randint(-50, 50)}px; --y4: {random.randint(-50, 50)}px;
    }}"></div>""" for i in range(20)]) + """

    <div class="chat-header">
        <h2>Bae ❤️</h2>
        <div class="status">● en ligne</div>
    </div>
    <div style="margin-top: 75px;"></div>
    """, unsafe_allow_html=True)

# --- MENU SECRET (BOUTONS) ---
col1, col2 = st.columns(2)

with col1:
    if st.button("Notre coin secret ✨"):
        st.balloons()
        st.info("“Si tu regardes ça, c’est sûrement que tu pensais à nous. Moi aussi je pense à toi.”")
        try:
            st.video("Souvenir.mp4") # C'est ici que ta vidéo va se lancer !
        except:
            st.error("Je n'arrive pas à charger la vidéo... mais sache que je t'aime ❤️")

with col2:
    if st.button("Message du jour 💌"):
        messages = [
            "Tu es la plus belle chose qui me soit arrivée. ✨",
            "N'oublie jamais à quel point tu es forte. 💪",
            "Je suis fier de toi, chaque jour un peu plus. ❤️",
            "Ton sourire est ma drogue préférée. 😍",
            "Même loin, je suis tout près de ton cœur. 🫂"
        ]
        st.success(random.choice(messages))

st.markdown(f"""
    <div style='text-align:center; color:#a765e6; font-size:13px; margin-top:10px; margin-bottom:20px; font-weight:600;'>
        ⏳ Nous deux, ça fait déjà <b>{diff.days}</b> jours de bonheur ✨
    </div>
    """, unsafe_allow_html=True)

# --- HISTORIQUE ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Coucou Babe ❤️ Je suis là. Comment tu te sens ?", "emoji": "👋"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant" and "emoji" in message:
            st.markdown(f'<div style="display: flex; align-items: flex-start;"><span class="bae-emoji">{message["emoji"]}</span> <span>{message["content"]}</span></div>', unsafe_allow_html=True)
        else:
            st.write(message["content"])

# --- INPUT ---
if prompt := st.chat_input("Écris à ton Bae..."):
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        response_data = get_manual_brain_response(prompt)
        time.sleep(1)
        st.markdown(f'<div style="display: flex; align-items: flex-start;"><span class="bae-emoji">{response_data["emoji"]}</span> <span>{response_data["text"]}</span></div>', unsafe_allow_html=True)
        
    st.session_state.messages.append({"role": "assistant", "content": response_data["text"], "emoji": response_data["emoji"]})
