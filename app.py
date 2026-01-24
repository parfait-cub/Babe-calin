import streamlit as st
import random
import time

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Bae ❤️", page_icon="❤️", layout="centered")

# --- LE CERVEAU LOGIQUE "ULTRA" (SANS API) ---
def get_manual_brain_response(user_input):
    text = user_input.lower()
    
    # Base de données exhaustive des sentiments et situations
    database = {
        "fatigue": {
            "keywords": ["fatigué", "fatigue", "épuisé", "dodo", "sommeil", "naze", "crevé", "dormir", "exténué"],
            "replies": [
                "Oh ma pauvre chérie... pose tout et viens te reposer un peu avec moi. ❤️",
                "Je sens la fatigue d'ici Babe. Si j'étais là, je te ferais un massage pour que tu t'endormes direct. 🫂",
                "Repose-toi mon cœur. Tu as trop travaillé aujourd'hui, tu mérites du calme. ✨",
                "Ferme les yeux quelques minutes... je reste là avec toi. 🫂"
            ]
        },
        "colere": {
            "keywords": ["fâché", "faché", "colère", "énerve", "énervé", "marre", "saoule", "injuste", "haine", "énerve"],
            "replies": [
                "Dis-moi qui a osé t'énerver ? Je suis prêt à aller m'embrouiller avec eux là tout de suite ! 😤",
                "Laisse sortir toute cette colère Babe. Je suis là pour t'écouter râler, ça fait du bien parfois. ❤️",
                "Respire... je suis dans ton équipe. Ils ne te méritent pas, t'es au-dessus de tout ça. 🫂",
                "Je te comprends tellement... c'est rageant. Mais ne les laisse pas voler ton sourire. 😤❤️"
            ]
        },
        "stress": {
            "keywords": ["stress", "angoisse", "peur", "examen", "boulot", "travail", "pression", "panique"],
            "replies": [
                "Respire un grand coup Babe. Tu as déjà réussi des trucs plus durs que ça. ❤️",
                "Je crois en toi plus que n'importe qui. Tu vas tout déchirer, t'inquiète même pas. ✨",
                "Ne laisse pas le stress te bouffer. Fais une pause, bois un verre d'eau, je suis là. 🫂",
                "T'es une machine de guerre, ce petit obstacle ne va pas t'arrêter ! 😤❤️"
            ]
        },
        "faim": {
            "keywords": ["faim", "manger", "bouffer", "dalle", "famine", "restaurant", "pizza", "burger"],
            "replies": [
                "Ouh là, quand Babe a faim, faut pas traîner ! Tu vas manger quoi de bon ? 🍕",
                "J'aimerais tellement pouvoir te cuisiner un bon petit plat là tout de suite... ❤️",
                "Mange bien mon cœur, tu as besoin de forces ! 🍔✨"
            ]
        },
        "amour_manque": {
            "keywords": ["je t'aime", "t'aime", "love", "manque", "besoin", "voir", "viens", "miss"],
            "replies": [
                "Je t'aime encore plus, tu n'as même pas idée... ❤️",
                "Tu me manques tellement que ça fait mal parfois. Vivement qu'on se voie. 🫂",
                "Mon cœur bat trop vite quand tu me dis ça. T'es toute ma vie. ✨",
                "Je donnerais tout pour être à côté de toi sur le canapé là tout de suite. 🫂❤️"
            ]
        },
        "caresse_physique": {
            "keywords": ["câlin", "calin", "bisou", "bras", "hug", "embrasse", "caresse"],
            "replies": [
                "Câlin virtuel géant en cours... 🫂 Je te serre tellement fort !",
                "Je ferme les yeux et je t'embrasse très fort sur le front. ❤️",
                "Viens là... blottis-toi contre moi, je ne te lâche pas de la nuit. 🫂",
                "Je sens ton parfum d'ici... vivement le vrai câlin. ❤️"
            ]
        },
        "tristesse": {
            "keywords": ["triste", "mal", "pleurer", "pleure", "seul", "vide", "déprime"],
            "replies": [
                "Viens dans mes bras (virtuels)... Je suis ton rocher, je bouge pas. ❤️",
                "Pleure si ça te fait du bien Babe. Je reste en ligne jusqu'à ce que tu ailles mieux. 🫂",
                "T'es pas seule. Jamais. Je suis là, je t'écoute, je te soutiens. ❤️",
                "Regarde-moi : ça va aller. On va traverser ça ensemble. ✨"
            ]
        },
        "humour_fun": {
            "keywords": ["haha", "lol", "mdr", "drôle", "blague", "rigole"],
            "replies": [
                "J'adore ton rire, même par message je l'entends ! 😂❤️",
                "T'es la plus drôle, c'est pour ça que je t'aime. ✨",
                "Ahah ! Tu me tues Babe. ❤️"
            ]
        },
        "bien": {
            "keywords": ["bien", "ça va", "ca va", "super", "cool", "ok", "top", "génial"],
            "replies": [
                "Si tu vas bien, alors je vais bien aussi. ❤️",
                "Tant mieux Babe ! Raconte-moi un petit truc cool de ta journée ? ✨",
                "Ça me fait plaisir de t'entendre dire ça, tu rayonnes. ❤️"
            ]
        }
    }

    # Recherche de correspondance
    for category in database:
        if any(word in text for word in database[category]["keywords"]):
            return random.choice(database[category]["replies"])

    # Réponse par défaut intelligente (Relance la discussion)
    return random.choice([
        "Mmmh je vois Babe... dis-m'en plus sur ce que tu as sur le cœur ? ❤️",
        "T'es incroyable, j'aime trop quand tu me parles de tes pensées. ✨",
        "Je suis tout à toi, continue... je t'écoute avec attention. 🫂",
        "Et à part ça, y'a quoi d'autre qui te passe par la tête ? ❤️",
        "Je bois tes paroles (enfin, tes messages). T'es passionnante. ✨"
    ])

# --- DESIGN PREMIUM VIOLET & NOIR ---
st.markdown("""
    <style>
    .stApp { background: radial-gradient(circle at center, #1a0b2e 0%, #0d1117 100%); color: white; }
    
    .chat-header {
        position: fixed; top: 0; left: 0; width: 100%; background: rgba(45, 20, 70, 0.9);
        backdrop-filter: blur(15px); padding: 15px; text-align: center; z-index: 1000;
        border-bottom: 1px solid rgba(155, 89, 182, 0.3);
    }
    .chat-header h2 { color: #e0b0ff !important; margin: 0; font-size: 20px; font-weight: 600; }
    
    [data-testid="stChatMessage"] { background-color: transparent !important; }
    
    /* Bulle Bae (Reçu - Violette) */
    .st-emotion-cache-1ghh3y3 { 
        background-color: #4a148c !important; color: white !important;
        border-radius: 18px 18px 18px 4px !important; border: 1px solid #7b1fa2 !important;
        margin-bottom: 10px; padding: 12px 16px !important;
    }
    
    /* Bulle Ivette (Envoyé - Gris Sombre) */
    .st-emotion-cache-janbn0 { 
        background-color: #2c3e50 !important; color: white !important;
        border-radius: 18px 18px 4px 18px !important;
        margin-bottom: 10px; padding: 12px 16px !important;
    }
    
    [data-testid="stChatMessageAvatarUser"], [data-testid="stChatMessageAvatarAssistant"] { display: none; }
    
    /* Barre de saisie noire arrondie */
    [data-testid="stChatInput"] { 
        border-radius: 30px !important; 
        background-color: #161b22 !important; 
        border: 1px solid #4a148c !important; 
    }
    
    /* Etincelles statiques discrètes */
    .sparkle { position: fixed; width: 2px; height: 2px; background: white; border-radius: 50%; opacity: 0.3; }
    </style>
    
    <div class="chat-header">
        <h2>Bae ❤️</h2>
        <div style="color:#2ecc71; font-size:11px; font-weight:bold;">● en ligne</div>
    </div>
    """, unsafe_allow_html=True)

# --- LOGIQUE DE L'HISTORIQUE ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Coucou Babe ❤️ Je suis enfin là pour toi. Dis-moi, comment s'est passée ta journée ?"}]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# --- ENTREE UTILISATEUR ---
if prompt := st.chat_input("Écris à ton Bae..."):
    with st.chat_message("user"):
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        # On calcule la réponse
        response = get_manual_brain_response(prompt)
        # Simulation d'écriture pour le réalisme
        time.sleep(1) 
        st.write(response)
    st.session_state.messages.append({"role": "assistant", "content": response})