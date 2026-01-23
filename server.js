const express = require("express");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json());

const PORT = process.env.PORT || 3000;

// 🌟 Mémoire courte : on garde les 5 derniers messages
let memory = [];

// 🎯 Réponses par contexte (idem ton code)
const responses = {
  // ... toutes tes catégories de réponses ici ...
  neutre: [
    "Je suis là Babe ❤️… parle-moi un peu 🫂",
    "Dis-moi ce que tu ressens Babe ❤️",
    "Je t’écoute Babe ❤️… je suis là",
    "Je suis avec toi 🫂… tu n’es pas seule",
    "Prenons un moment ensemble Babe ❤️"
  ]
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
    calin: ["câlin","embrass","près de toi","serre-moi"],
    compliment: ["belle","adorable","magnifique","canon","sublime"],
    encourage: ["je peux","je vais","je dois","je veux","fais moi confiance"],
    leger: ["haha","lol","mdr","rigole","drôle"],
    fatigue: ["fatigu","épuis","dormi","somnolent"],
    peur: ["peur","angoiss","inquiet","effrayé"],
    doute: ["doute","hésit","incertain","peux pas"],
    surprise: ["surpris","incroyable","inattendu","oh la la"],
    gratitude: ["merci","gentil","touche","adorable"],
    reflexion: ["réfléch","pense","je me demande","question"],
    amour: ["amour","je t’aime","cœur","adorer"],
    curiosite: ["curieux","dis m'en","raconte","explique"],
    reflexion_positive: ["bien","super","génial","bravo","top"],
    leger_humour: ["rigole","haha","mdr","drôle","marrant"]
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

  // Ajouter à la mémoire
  memory.push(message);
  if (memory.length > 5) memory.shift();

  const context = detectContext(message);
  let reply = getResponse(context);

  // Ajouter un rappel de mémoire courte pour humaniser
  if (memory.length > 1) {
    const prev = memory[memory.length - 2];
    reply += ` (je me souviens que tu as dit : "${prev}")`;
  }

  res.json({ reply });
});

// 🫂 Route câlin uniquement
app.post("/hug", (req, res) => {
  console.log("🫂 Demande de câlin");
  const reply = getResponse("calin");
  res.json({ reply });
});

// 🚀 Lancement serveur
app.listen(PORT, () => {
  console.log(`💙 Backend prêt sur http://localhost:${PORT}`);
});
