import express from "express";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

// ⚡ Port dynamique pour Render ou fallback local
const PORT = process.env.PORT || 3000;

// 🌟 Mémoire courte : on garde les 5 derniers messages
let memory = [];

// 🎯 Réponses par contexte (30+ contextes)
const responses = {
  triste: [
    "Viens là Babe ❤️… je suis là avec toi.",
    "Je te serre fort dans mes bras 🫂… respire doucement.",
    "Je suis là Babe ❤️… même si les mots ne suffisent pas.",
    "Ça va aller… je suis juste là pour toi 🫂",
    "Je t’écoute Babe ❤️… prends ton temps.",
    "Même si c’est dur, je suis là pour toi 🫂"
  ],
  stresse: [
    "Respire un peu Babe ❤️… je suis là.",
    "Tout va aller… je suis avec toi 🫂",
    "Doucement… tu n’es pas seule ❤️",
    "Je t’accompagne Babe ❤️… prends ton temps",
    "Tu es forte, je suis là avec toi 🫂",
    "Relax Babe ❤️… je veille sur toi."
  ],
  joyeuse: [
    "Wow Babe ❤️… tu rayonnes aujourd’hui !",
    "Je suis super content de te voir heureuse 🫂",
    "Tu as un sourire magnifique Babe ❤️",
    "Ça fait plaisir de te voir comme ça 🫂",
    "Je suis fier de toi ❤️… toujours adorable",
    "Tellement heureux de te voir sourire 🫂"
  ],
  calin: [
    "Viens là Babe ❤️… juste un câlin",
    "Je te prends dans mes bras 🫂… je reste avec toi",
    "Câlin doux pour toi Babe ❤️… respire un peu",
    "Un petit câlin tendre pour toi 🫂",
    "Babe ❤️… je t’entoure de douceur 🫂",
    "Je te serre fort… je suis là pour toi ❤️"
  ],
  neutre: [
    "Je suis là Babe ❤️… parle-moi un peu 🫂",
    "Dis-moi ce que tu ressens Babe ❤️",
    "Je t’écoute Babe ❤️… je suis là",
    "Je suis avec toi 🫂… tu n’es pas seule",
    "Prenons un moment ensemble Babe ❤️"
  ]
  // 🟢 Ajoute les autres contextes ici…
};

// 🎲 Fonction pour choisir une phrase aléatoire selon contexte
function getResponse(context) {
  const phrases = responses[context] || responses["neutre"];
  const randomIndex = Math.floor(Math.random() * phrases.length);
  return phrases[randomIndex];
}

// 🔍 Détection simple du contexte
function detectContext(message) {
  const msg = message.toLowerCase();
  if (!msg) return "neutre";

  const map = {
    triste: ["triste","déprim","mal","pleure","pleurer"],
    stresse: ["stress","angoisse","pressé","nerveux","tendu"],
    joyeuse: ["content","heureux","génial","super","top"],
    calin: ["câlin","embrass","près de toi","serre-moi"]
    // 🟢 Ajouter tous les autres mots-clés ici
  };

  for (const [key, words] of Object.entries(map)) {
    if (words.some(w => msg.includes(w))) return key;
  }
  return "neutre";
}

// 🌐 Route principale
app.post("/message", (req, res) => {
  const { message } = req.body;
  console.log("📩 Message reçu :", message);

  if (!message) return res.json({ reply: "Oops… tu n'as rien écrit 😅" });

  // Ajouter à la mémoire
  memory.push(message);
  if (memory.length > 5) memory.shift(); // garder max 5 messages

  const context = detectContext(message);
  let reply = getResponse(context);

  // Ajouter un rappel de mémoire courte pour humaniser
  if (memory.length > 1) {
    const prev = memory[memory.length - 2];
    reply += ` (je me souviens que tu as dit : "${prev}")`;
  }

  // Renvoyer aussi la longueur du message pour le frontend
  const bubbleSize = Math.min(Math.max(message.length * 2, 50), 300); // 50px min, 300px max

  res.json({ reply, bubbleSize });
});

// 🫂 Route câlin uniquement
app.post("/hug", (req, res) => {
  console.log("🫂 Demande de câlin");
  const reply = getResponse("calin");
  const bubbleSize = Math.min(Math.max(reply.length * 2, 50), 300);
  res.json({ reply, bubbleSize });
});

// 🚀 Lancement serveur
app.listen(PORT, () => {
  console.log(`💙 Backend prêt sur http://localhost:${PORT}`);
});
