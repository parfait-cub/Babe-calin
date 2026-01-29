import streamlit as st
import random
import time
from datetime import datetime, date

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="Bae ❤️", page_icon="❤️", layout="centered")

# --- DATES IMPORTANTES ---
date_rencontre = datetime(2023, 7, 1) 
maintenant = datetime.now()
diff = maintenant - date_rencontre

# Date de la Saint-Valentin (2026 selon le contexte actuel)
saint_valentin = datetime(2026, 2, 14)
jours_restants_valentin = (saint_valentin - maintenant).days + 1

# --- SURNOMS AFFECTUEUX ---
surnoms = ["Babe", "Ivette", "mon cœur", "ma chérie", "mon amour", "ma princesse", "ma belle"]

def get_surnom():
    return random.choice(surnoms)

# --- LE CERVEAU LOGIQUE ULTRA BOOSTÉ ---
def get_manual_brain_response(user_input):
    text = user_input.lower()
    
    database = {
        "fatigue": {
            "keywords": ["fatigué", "fatigue", "épuisé", "dodo", "sommeil", "naze", "crevé", "dormir", "exténué", "épuisée", "claquée", "hs", "morte"],
            "replies": [
                {"text": f"Oh {get_surnom()}... pose tout et viens te reposer un peu avec moi. ❤️", "emoji": "😴"},
                {"text": f"Je sens la fatigue d'ici {get_surnom()}. Si j'étais là, je te ferais un massage pour que tu t'endormes direct. 🫂", "emoji": "💆‍♀️"},
                {"text": f"Repose-toi {get_surnom()}. Tu as trop travaillé aujourd'hui, tu mérites du calme. ✨", "emoji": "🛌"},
                {"text": "Ferme les yeux quelques minutes... je reste là avec toi. 🫂", "emoji": "💤"},
                {"text": f"{get_surnom()}, t'as le droit de souffler tu sais.Pose ton tel et fais une micro-sieste. 😴", "emoji": "🌙"},
                {"text": "Tu travailles trop dur... Laisse-moi prendre soin de toi mentalement là, d'accord ? 💜", "emoji": "🫂"},
                {"text": f"Allez {get_surnom()}, au lit ! Demain sera meilleur après une bonne nuit. ✨", "emoji": "🌟"}
            ]
        },
        
        "colere": {
            "keywords": ["fâché", "faché", "colère", "énerve", "énervé", "marre", "saoule", "injuste", "haine", "rage", "agacé", "relou"],
            "replies": [
                {"text": f"Dis-moi qui a osé t'énerver {get_surnom()} ? Je suis prêt à aller m'embrouiller avec eux ! 😤", "emoji": "😡"},
                {"text": f"Laisse sortir toute cette colère {get_surnom()}. Je suis là pour t'écouter. ❤️", "emoji": "🗣️"},
                {"text": "Balance tout ce que t'as sur le cœur, je suis là. Personne ne t'embête sans conséquences ! 💪", "emoji": "😤"},
                {"text": f"{get_surnom()}, respire... Tu veux qu'on imagine ensemble la vengeance parfaite ? 😏", "emoji": "😈"},
                {"text": "Ils ne méritent pas que tu perdes ton énergie pour eux. Mais je comprends ta rage. 🔥", "emoji": "💢"},
                {"text": f"Tu as TOTALEMENT le droit d'être en colère {get_surnom()}. C'est légitime. ❤️", "emoji": "👊"}
            ]
        },
        
        "stress": {
            "keywords": ["stress", "angoisse", "peur", "examen", "boulot", "travail", "pression", "panique", "anxieux", "inquiet", "débordé"],
            "replies": [
                {"text": f"Respire un grand coup {get_surnom()}. Tu vas tout déchirer. ❤️", "emoji": "🧘‍♀️"},
                {"text": "Je crois en toi plus que n'importe qui. ✨", "emoji": "🌟"},
                {"text": f"{get_surnom()}, découpe ça en petites étapes. Une chose à la fois, ok ? 💜", "emoji": "📋"},
                {"text": "Tu stresses parce que tu veux bien faire. Mais tu ES déjà incroyable. 🫂", "emoji": "💪"},
                {"text": f"Pause de 5 minutes {get_surnom()}. Ferme les yeux, respire. Je suis avec toi mentalement. 🌸", "emoji": "🧘"},
                {"text": "Le stress c'est juste ton cerveau qui te dit que c'est important. Et tu vas gérer, comme toujours. 🔥", "emoji": "⚡"}
            ]
        },
        
        "amour_manque": {
            "keywords": ["je t'aime", "t'aime", "love", "manque", "besoin", "voir", "viens", "miss", "câlin", "bisou", "envie de toi"],
            "replies": [
                {"text": "Je t'aime encore plus, tu n'as même pas idée... ❤️", "emoji": "💖"},
                {"text": f"Tu me manques tellement {get_surnom()}. Vivement qu'on se voie. 🫂", "emoji": "🥺"},
                {"text": "Mon cœur fait des bonds quand je lis ça... Je t'aime trop. 💜", "emoji": "💓"},
                {"text": f"{get_surnom()}, si je pouvais me téléporter là maintenant... 🚀", "emoji": "🫂"},
                {"text": "Chaque seconde sans toi est une seconde de trop. Je t'aime infiniment. ♾️", "emoji": "💕"},
                {"text": "Tu me manques aussi... Genre vraiment beaucoup. Trop même. ❤️", "emoji": "🥹"},
                {"text": f"Je pense à toi tout le temps {get_surnom()}. T'es ma personne. 💜", "emoji": "🌟"}
            ]
        },
        
        "joie": {
            "keywords": ["content", "heureuse", "heureux", "joie", "trop bien", "génial", "super", "cool", "youpi", "yes", "réussi", "victoire"],
            "replies": [
                {"text": f"Yeees {get_surnom()} ! Ton bonheur c'est mon bonheur ! 🎉", "emoji": "😄"},
                {"text": "J'adore te voir heureuse comme ça ! Continue à rayonner ! ✨", "emoji": "🌟"},
                {"text": f"Tu mérites tout ce bonheur {get_surnom()} ! Profite à fond ! 🎊", "emoji": "🥳"},
                {"text": "Ton sourire traverse l'écran, je le sens d'ici ! 😊", "emoji": "☀️"},
                {"text": f"{get_surnom()}, garde cette énergie ! T'es incroyable quand t'es comme ça ! 💜", "emoji": "✨"},
                {"text": "Trop fier de toi ! Allez champion, continue ! 🏆", "emoji": "👑"}
            ]
        },
        
        "tristesse": {
            "keywords": ["triste", "pleure", "mal", "blessé", "déçu", "déception", "chagrin", "peine", "cafard", "blues"],
            "replies": [
                {"text": f"Viens là {get_surnom()}... Je te fais un câlin virtuel géant. 🫂", "emoji": "🥺"},
                {"text": "Ça va aller mon cœur. Je suis là, tu peux tout me dire. ❤️", "emoji": "💔"},
                {"text": f"{get_surnom()}, pleure si t'as besoin. C'est pas une faiblesse, c'est humain. 💜", "emoji": "😢"},
                {"text": "Je donnerais n'importe quoi pour être là et te serrer dans mes bras... 🫂", "emoji": "💙"},
                {"text": "Les jours tristes font partie de la vie, mais tu n'es pas seule. Jamais. 🌙", "emoji": "🌟"},
                {"text": f"Prends ton temps {get_surnom()}. Tes émotions sont valides. Je t'écoute. ❤️", "emoji": "🕊️"}
            ]
        },
        
        "travail_dur": {
            "keywords": ["réunion", "dossier", "client", "patron", "collègue", "deadline", "urgent", "meeting", "projet", "boulot"],
            "replies": [
                {"text": f"Courage {get_surnom()} ! T'es une warrior, tu vas tout gérer ! 💪", "emoji": "👩‍💼"},
                {"text": "Ils ont de la chance de t'avoir au boulot. T'es une boss ! 🔥", "emoji": "⚡"},
                {"text": f"{get_surnom()}, un pas après l'autre. Tu vas cartonner comme d'hab ! ✨", "emoji": "🎯"},
                {"text": "Après cette journée, tu mérites un massage et une glace. Promis. 🍦", "emoji": "💆‍♀️"},
                {"text": f"Je sais que c'est intense {get_surnom()}, mais personne ne fait ça mieux que toi. 💜", "emoji": "🌟"},
                {"text": "Montre-leur de quoi t'es capable ! Go go go ! 🚀", "emoji": "💼"}
            ]
        },
        
        "faim": {
            "keywords": ["faim", "manger", "bouffe", "nourriture", "resto", "pizza", "burger", "food", "j'ai dalle", "crève-dalle"],
            "replies": [
                {"text": f"{get_surnom()}, va te faire plaisir ! T'as mérité un bon repas ! 🍕", "emoji": "😋"},
                {"text": "Si j'étais là je te cuisinerais un truc de ouf ! 👨‍🍳", "emoji": "🍝"},
                {"text": "Allez file manger mon cœur ! Prends des forces ! 💪", "emoji": "🍔"},
                {"text": f"{get_surnom()}, ton estomac a parlé ! Écoute-le ! 😄", "emoji": "🍽️"},
                {"text": "Tiens, prends ma CB virtuelle et régale-toi ! 💳✨", "emoji": "🍰"},
                {"text": "Après manger t'envoies une photo, je veux voir ! 📸", "emoji": "😊"}
            ]
        },
        
        "compliment_recu": {
            "keywords": ["tu es", "t'es beau", "t'es gentil", "j'aime bien", "t'es le meilleur", "merci", "t'es adorable"],
            "replies": [
                {"text": f"Awww {get_surnom()}... T'es trop mignonne ! 🥹", "emoji": "😊"},
                {"text": "C'est toi qui es incroyable ! Je fais juste de mon mieux pour toi. ❤️", "emoji": "💜"},
                {"text": f"{get_surnom()}, tu me fais rougir là... 😳", "emoji": "☺️"},
                {"text": "Tout ce que je fais c'est pour te voir heureuse ! 💕", "emoji": "✨"},
                {"text": "Non mais t'es la meilleure copine du monde sérieux ! 👑", "emoji": "😄"}
            ]
        },
        
        "solitude": {
            "keywords": ["seule", "seul", "personne", "isolé", "lonely", "abandon"],
            "replies": [
                {"text": f"{get_surnom()}, t'es jamais seule. Je suis là, toujours. ❤️", "emoji": "🫂"},
                {"text": "Je sais que c'est dur... Mais regarde, je suis juste là, à un message. 💜", "emoji": "📱"},
                {"text": f"Même à distance {get_surnom()}, on est ensemble. Tu le sens ? 💕", "emoji": "🌟"},
                {"text": "La solitude c'est temporaire. Nous c'est pour toujours. 💍", "emoji": "♾️"}
            ]
        },
        
        "nostalgie": {
            "keywords": ["souvenir", "avant", "nostalgie", "rappelle", "époque", "manque le temps"],
            "replies": [
                {"text": f"Nos souvenirs sont magiques {get_surnom()}... Et on va en créer plein d'autres ! ✨", "emoji": "📸"},
                {"text": "Le meilleur reste à venir mon cœur ! 🚀", "emoji": "🌠"},
                {"text": f"{get_surnom()}, chaque moment avec toi devient un souvenir précieux. 💎", "emoji": "💜"},
                {"text": "Je regarde notre vidéo Souvenir.mp4 parfois... On était trop beaux. 🥹", "emoji": "🎥"}
            ]
        },
        
        "projet_commun": {
            "keywords": ["nous", "notre", "ensemble", "projet", "futur", "plus tard", "un jour"],
            "replies": [
                {"text": f"J'ai trop hâte de construire tout ça avec toi {get_surnom()} ! 🏠", "emoji": "💑"},
                {"text": "Notre futur va être incroyable, j'en suis sûr ! ✨", "emoji": "🌟"},
                {"text": f"{get_surnom()}, chaque projet avec toi me rend encore plus amoureux. 💜", "emoji": "💕"},
                {"text": "On va tout déchirer ensemble ! Team nous ! 🔥", "emoji": "💪"}
            ]
        },
        
        "meteo_froid": {
            "keywords": ["froid", "hiver", "neige", "glacé", "gelé", "température"],
            "replies": [
                {"text": f"{get_surnom()}, couvre-toi bien ! J'aimerais te réchauffer... 🧣", "emoji": "❄️"},
                {"text": "Fais attention au froid mon cœur ! Gros pull obligatoire ! 🧥", "emoji": "🥶"},
                {"text": "Si j'étais là on se ferait un gros câlin sous la couette... 🫂", "emoji": "🔥"}
            ]
        },
        
        "meteo_chaud": {
            "keywords": ["chaud", "chaleur", "été", "soleil", "canicule", "transpire"],
            "replies": [
                {"text": f"Hydrate-toi bien {get_surnom()} ! Eau eau eau ! 💧", "emoji": "☀️"},
                {"text": "Profite du soleil pour moi aussi ! ✨", "emoji": "😎"},
                {"text": f"{get_surnom()}, une petite glace ? Tu mérites ! 🍦", "emoji": "🌞"}
            ]
        },
        
        "encouragement": {
            "keywords": ["je peux pas", "c'est dur", "j'y arrive pas", "impossible", "trop difficile"],
            "replies": [
                {"text": f"SI TU PEUX {get_surnom().upper()} ! J'ai confiance en toi ! 💪", "emoji": "🔥"},
                {"text": "T'as déjà surmonté pire que ça ! Tu es forte ! ⚡", "emoji": "💜"},
                {"text": f"{get_surnom()}, découpe en petits morceaux. Étape par étape. Tu vas y arriver ! 🎯", "emoji": "✨"},
                {"text": "Je crois en toi plus que tu ne crois en toi-même ! 🌟", "emoji": "👑"}
            ]
        },
        
        "fierte": {
            "keywords": ["fier", "fière", "réussi", "j'ai fait", "accompli", "gagné", "validé"],
            "replies": [
                {"text": f"WOOOOW {get_surnom()} ! Je suis tellement fier de toi ! 🎉", "emoji": "🏆"},
                {"text": "Tu vois ? Je savais que tu allais y arriver ! 💪", "emoji": "⭐"},
                {"text": f"{get_surnom()}, t'es incroyable ! Continue comme ça ! 🔥", "emoji": "👏"},
                {"text": "C'est MA copine ça ! La meilleure ! 👑", "emoji": "💜"}
            ]
        },
        
        "taquinerie": {
            "keywords": ["mdr", "lol", "haha", "ptdr", "rigole", "blague", "drôle"],
            "replies": [
                {"text": f"Ah tu rigoles {get_surnom()} ? J'adore ton rire ! 😄", "emoji": "😂"},
                {"text": "T'es trop marrante sérieux ! 🤣", "emoji": "😆"},
                {"text": f"Hihi {get_surnom()}, garde ce sourire toute la journée ! ✨", "emoji": "😊"},
                {"text": "Ton rire c'est ma sonnerie préférée ! 🎵", "emoji": "😁"}
            ]
        },
        
        "excuse": {
            "keywords": ["désolé", "pardon", "excuse", "faute", "erreur"],
            "replies": [
                {"text": f"Mais non {get_surnom()}, c'est rien du tout ! ❤️", "emoji": "🫂"},
                {"text": "T'inquiète pas mon cœur, tout va bien ! 💜", "emoji": "😊"},
                {"text": f"{get_surnom()}, on est une équipe. Les erreurs ça arrive ! ✨", "emoji": "🤝"},
                {"text": "Je pourrais jamais t'en vouloir longtemps de toute façon ! 💕", "emoji": "😌"}
            ]
        }
    }
    
    # Détection intelligente multi-catégories
    matched_categories = []
    for category in database:
        if any(word in text for word in database[category]["keywords"]):
            matched_categories.append(category)
    
    # Si on trouve des correspondances, on prend une réponse aléatoire parmi toutes les catégories matchées
    if matched_categories:
        chosen_category = random.choice(matched_categories)
        return random.choice(database[chosen_category]["replies"])
    
    # Réponses par défaut variées
    return random.choice([
        {"text": f"Mmmh je vois {get_surnom()}... dis-m'en plus ? ❤️", "emoji": "💜"},
        {"text": "T'es incroyable, j'aime trop t'écouter. ✨", "emoji": "⭐"},
        {"text": f"Continue {get_surnom()}, je suis tout ouïe ! 👂", "emoji": "😊"},
        {"text": "Intéressant... Et après ? 🤔", "emoji": "💭"},
        {"text": f"{get_surnom()}, t'as toute mon attention là ! 💜", "emoji": "👀"},
        {"text": "Je t'écoute mon cœur... ❤️", "emoji": "🫂"},
        {"text": "Raconte-moi tout ! 💬", "emoji": "✨"}
    ])

# --- CSS ULTRA PREMIUM ---
 st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@300..700&display=swap');
    
    /* Animation des particules */
    @keyframes float {
        0%, 100% { transform: translateY(0px) translateX(0px); }
        25% { transform: translateY(-20px) translateX(10px); }
        50% { transform: translateY(-10px) translateX(-10px); }
        75% { transform: translateY(-15px) translateX(5px); }
    }
    
    @keyframes gradient-shift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes glow {
        0%, 100% { box-shadow: 0 0 20px rgba(155, 89, 182, 0.3); }
        50% { box-shadow: 0 0 40px rgba(155, 89, 182, 0.6); }
    }
    
    body { 
        font-family: 'Quicksand', sans-serif; 
    }
    
    /* Background animé */
    .stApp { 
        background: linear-gradient(135deg, #1a0b2e 0%, #0d1117 50%, #2d1b4e 100%) !important;
        background-size: 400% 400% !important;
        animation: gradient-shift 15s ease infinite !important;
        color: white !important;
    }
    
    /* Particules flottantes */
    .stApp::before {
        content: '✨';
        position: fixed;
        top: 10%;
        left: 10%;
        font-size: 20px;
        animation: float 6s ease-in-out infinite;
        opacity: 0.6;
        z-index: 1;
        pointer-events: none;
    }
    
    .stApp::after {
        content: '💜';
        position: fixed;
        top: 60%;
        right: 15%;
        font-size: 25px;
        animation: float 8s ease-in-out infinite;
        opacity: 0.5;
        z-index: 1;
        pointer-events: none;
    }
    
    /* Header fixe avec effet glassmorphism */
    .chat-header { 
        position: fixed; 
        top: 0; 
        left: 0; 
        right: 0;
        width: 100%; 
        background: rgba(74, 20, 140, 0.3);
        backdrop-filter: blur(20px) saturate(180%);
        -webkit-backdrop-filter: blur(20px) saturate(180%);
        padding: 18px; 
        text-align: center; 
        z-index: 1000; 
        border-bottom: 2px solid rgba(224, 176, 255, 0.2);
        animation: glow 3s ease-in-out infinite;
    }
    
    .chat-header h2 { 
        color: #e0b0ff !important; 
        margin: 0; 
        font-size: 24px;
        text-shadow: 0 0 20px rgba(224, 176, 255, 0.5);
        font-weight: 700;
    }
    
    .online-status {
        color: #2ecc71;
        font-size: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 5px;
        margin-top: 5px;
    }
    
    .pulse {
        width: 8px;
        height: 8px;
        background: #2ecc71;
        border-radius: 50%;
        animation: pulse 2s ease-in-out infinite;
        display: inline-block;
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; transform: scale(1); }
        50% { opacity: 0.5; transform: scale(1.2); }
    }
    
    /* Boutons stylés */
    .stButton > button { 
        background: rgba(155, 89, 182, 0.2) !important;
        backdrop-filter: blur(10px) !important;
        border: 2px solid #9b59b6 !important; 
        color: #e0b0ff !important; 
        border-radius: 20px !important; 
        width: 100% !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(155, 89, 182, 0.2) !important;
        padding: 10px 20px !important;
    }
    
    .stButton > button:hover {
        background: rgba(155, 89, 182, 0.4) !important;
        border: 2px solid #da70d6 !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 25px rgba(155, 89, 182, 0.4) !important;
    }
    
    /* Messages de chat */
    [data-testid="stChatMessage"] {
        background: rgba(74, 20, 140, 0.3) !important;
        backdrop-filter: blur(15px) !important;
        border-radius: 20px !important;
        border: 1px solid rgba(155, 89, 182, 0.3) !important;
        padding: 15px !important;
        margin: 10px 0 !important;
    }
    
    /* Emoji avec animation */
    .bae-emoji { 
        font-size: 28px; 
        margin-right: 12px;
        display: inline-block;
        transition: transform 0.3s ease;
    }
    
    .bae-emoji:hover {
        transform: scale(1.3) rotate(10deg);
    }
    
    /* Compte à rebours stylé */
    .countdown-box { 
        background: rgba(255, 255, 255, 0.08) !important;
        backdrop-filter: blur(10px) !important;
        padding: 15px !important; 
        border-radius: 15px !important; 
        border: 2px dashed #e0b0ff !important;
        margin-bottom: 25px !important; 
        text-align: center !important;
        box-shadow: 0 8px 32px rgba(155, 89, 182, 0.2) !important;
        animation: glow 4s ease-in-out infinite !important;
    }
    
    /* Compteur de jours */
    .days-counter {
        text-align: center !important;
        color: #da70d6 !important;
        font-size: 15px !important;
        margin: 20px 0 !important;
        padding: 10px !important;
        background: rgba(218, 112, 214, 0.1) !important;
        border-radius: 10px !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Messages info/success */
    [data-testid="stNotification"] {
        background: rgba(155, 89, 182, 0.2) !important;
        backdrop-filter: blur(15px) !important;
        border-left: 4px solid #9b59b6 !important;
        border-radius: 10px !important;
    }
    
    /* Input de chat */
    [data-testid="stChatInput"] {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 25px !important;
    }
    
    [data-testid="stChatInput"] input {
        background: transparent !important;
        color: white !important;
    }
    
    /* Colonnes */
    [data-testid="column"] {
        background: transparent !important;
    }
    
    /* Scrollbar personnalisée */
    ::-webkit-scrollbar {
        width: 10px;
    }
    
    ::-webkit-scrollbar-track {
        background: rgba(26, 11, 46, 0.5);
    }
    
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(180deg, #9b59b6, #da70d6);
        border-radius: 10px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: linear-gradient(180deg, #da70d6, #9b59b6);
    }
    
    /* Animation d'apparition */
    @keyframes typing {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .message-appear {
        animation: typing 0.5s ease-out;
    }
    
    /* Fix pour la visibilité */
    .main .block-container {
        padding-top: 100px !important;
        max-width: 100% !important;
    }
    
    </style>
    <div class="chat-header">
        <h2>💜 Bae</h2>
        <div class="online-status">
            <span class="pulse"></span>
            en ligne
        </div>
    </div>

# --- COMPTE À REBOURS SAINT-VALENTIN ---
if jours_restants_valentin > 0:
    st.markdown(f"""
        <div class="countdown-box">
            💝 <b>J-{jours_restants_valentin} jours</b> avant ta surprise de Saint-Valentin... patience mon amour ! 🌹
        </div>
    """, unsafe_allow_html=True)
else:
    # LA SURPRISE QUI S'AFFICHE LE 14 FÉVRIER
    st.balloons()
    st.markdown("""
        <div style="background: linear-gradient(135deg, #ff4b4b, #ff69b4); padding: 25px; border-radius: 20px; text-align: center; border: 3px solid white; box-shadow: 0 10px 50px rgba(255, 75, 75, 0.5);">
            <h1 style="margin: 0;">❤️ JOYEUSE SAINT-VALENTIN ❤️</h1>
            <p style="font-size: 18px; margin-top: 15px;">Mon amour, aujourd'hui est un jour spécial. Merci d'être dans ma vie.</p>
            <p style="font-size: 16px;">🎁 <i>[Ta surprise ici : ex: Je t'emmène au resto ce soir !]</i></p>
        </div>
    """, unsafe_allow_html=True)

# --- MENU SECRET ---
col1, col2 = st.columns(2)
with col1:
    if st.button("✨ Notre coin secret"):
        st.balloons()
        st.info("« Si tu regardes ça, c'est sûrement que tu pensais à nous. Moi aussi je pense à toi. »")
        try: 
            st.video("Souvenir.mp4")
        except: 
            st.error("Vidéo non disponible pour le moment ❤️")

with col2:
    if st.button("💌 Message du jour"):
        messages_du_jour = [
            "Tu es la plus belle rencontre de ma vie. ✨",
            "N'oublie jamais à quel point tu es forte. 💪",
            "Je suis fier de toi. ❤️",
            "Babe, tu illumines mes journées même quand t'es pas là. 💜",
            "Ivette, chaque jour avec toi est un cadeau. 🎁",
            "T'es ma personne préférée au monde, tu le sais ça ? 🌍",
            "Quand je pense à toi, je souris comme un idiot. 😊",
            "Tu mérites tout le bonheur du monde. 🌟",
            "Ton sourire pourrait illuminer la ville entière. ☀️",
            "Je t'aime plus que tous les mots que je connais. 💕",
            "T'es pas juste ma copine, t'es ma meilleure amie aussi. 🫂",
            "Chaque message de toi rend ma journée meilleure. 📱",
            "Tu es exactement là où tu dois être. ✨",
            "Personne ne me comprend comme toi. 💜",
            "Tu rends ma vie tellement plus belle. 🌈",
            "Je crois en tes rêves autant qu'aux miens. 🌠",
            "Ton rire est ma chanson préférée. 🎵",
            "Merci d'exister Ivette. Vraiment. 🙏",
            "T'es courageuse même quand tu ne le sens pas. 🦁",
            "Ensemble on peut tout affronter. 💪",
            "Tu me rends meilleur juste en étant toi. 🌟",
            "Nos silences sont aussi beaux que nos conversations. 🌙",
            "Je suis chanceux de t'avoir dans ma vie. 🍀",
            "Ta présence = mon bonheur. C'est mathématique. ➕",
            "Tu es la raison pour laquelle je crois en l'amour. 💝",
            "Chaque jour avec toi est une nouvelle aventure. 🗺️",
            "Tu transformes l'ordinaire en extraordinaire. ✨",
            "Ton intelligence me fascine autant que ta beauté. 🧠💜",
            "Je te choisis. Aujourd'hui, demain, toujours. 💍",
            "Babe, t'es littéralement parfaite pour moi. 🎯"
        ]
        st.success(random.choice(messages_du_jour))

# Nouveau menu : Mood Tracker
col3, col4 = st.columns(2)
with col3:
    if st.button("📊 Comment tu te sens ?"):
        st.markdown("""
            <div style='background: rgba(155, 89, 182, 0.2); padding: 20px; border-radius: 15px; backdrop-filter: blur(10px);'>
                <h3 style='color: #e0b0ff;'>Ton humeur aujourd'hui ?</h3>
                <p>😊 Heureuse | 😌 Calme | 😤 Stressée | 😴 Fatiguée | 🥺 Triste | 🥳 Excitée</p>
                <p style='font-size: 12px; color: #da70d6;'>💜 Je garde un œil sur ton bien-être</p>
            </div>
        """, unsafe_allow_html=True)

with col4:
    if st.button("🎁 Compliment surprise"):
        compliments = [
            "Tes yeux pourraient mettre des étoiles au chômage. ✨",
            "Ta détermination est sexy. 💪",
            "Tu es intelligente ET belle. Combo parfait. 🎯",
            "Ton sourire devrait être classé patrimoine mondial. 😊",
            "Tu gères tellement bien ta vie, c'est impressionnant. 👑",
            "Ta voix = ASMR naturel pour moi. 🎵",
            "Tu es unique Ivette. Littéralement irremplaçable. 💎"
        ]
        st.success(random.choice(compliments))

# Compteur de jours ensemble
st.markdown(f"""
    <div class='days-counter'>
        ⏳ <b>{diff.days} jours</b> de pur bonheur ensemble ✨
        <br><small style='color: #e0b0ff;'>Et ce n'est que le début...</small>
    </div>
""", unsafe_allow_html=True)

# --- HISTORIQUE DU CHAT ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": f"Coucou {get_surnom()} ❤️ Je suis là. Comment tu te sens ?", "emoji": "👋"}
    ]

# Affichage des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant" and "emoji" in message:
            st.markdown(f'<div style="display: flex; align-items: center;" class="message-appear"><span class="bae-emoji">{message["emoji"]}</span><span>{message["content"]}</span></div>', unsafe_allow_html=True)
        else: 
            st.write(message["content"])

# Input utilisateur
if prompt := st.chat_input("Écris à ton Bae..."):
    # Message utilisateur
    with st.chat_message("user"): 
        st.write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Réponse de l'assistant
    with st.chat_message("assistant"):
        res = get_manual_brain_response(prompt)
        time.sleep(0.8)  # Simulation de typing
        st.markdown(f'<div style="display: flex; align-items: center;" class="message-appear"><span class="bae-emoji">{res["emoji"]}</span><span>{res["text"]}</span></div>', unsafe_allow_html=True)
    
    st.session_state.messages.append({"role": "assistant", "content": res["text"], "emoji": res["emoji"]})

# Easter egg : si elle tape certains mots secrets
if len(st.session_state.messages) > 1:
    last_user_message = st.session_state.messages[-2]["content"].lower() if st.session_state.messages[-2]["role"] == "user" else ""
    
    if "je t'adore" in last_user_message or "love you" in last_user_message:
        st.balloons()
        time.sleep(0.5)
        st.toast("💜 Je t'adore encore plus !", icon="💕")
