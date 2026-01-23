import express from "express";
import cors from "cors";

const app = express();
app.use(cors());
app.use(express.json());

const PORT = 3000;

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
  compliment: [
    "Tu es tellement belle Babe ❤️… j’adore ça",
    "Ton sourire illumine tout 🫂",
    "Tu es unique et incroyable Babe ❤️",
    "Chaque jour je suis impressionné par toi 🫂",
    "Tu es splendide Babe ❤️",
    "Tout chez toi me fait craquer 🫂"
  ],
  encourage: [
    "Tu peux le faire Babe ❤️… je crois en toi !",
    "Je suis là à chaque pas 🫂",
    "Fonce, je sais que tu y arriveras Babe ❤️",
    "Ne lâche rien… je suis fier de toi 🫂",
    "Continue comme ça Babe ❤️… je te soutiens",
    "Je crois en toi, toujours 🫂"
  ],
  leger: [
    "Haha… tu me fais rire Babe ❤️",
    "Oh, t’es trop drôle 🫂",
    "Tu as toujours le mot pour me faire sourire ❤️",
    "Haha, j’adore ta spontanéité 🫂",
    "Trop mignonne quand tu rigoles ❤️",
    "Tu rends tout plus léger Babe 🫂"
  ],
  fatigue: [
    "Repose-toi un peu Babe ❤️… je veille sur toi 🫂",
    "Doucement… je suis là pour te soutenir ❤️",
    "Respire, prends ton temps… je suis là 🫂",
    "Un petit repos Babe ❤️… je suis là",
    "Ferme les yeux un moment, je suis là 🫂",
    "Je reste avec toi pour te détendre ❤️"
  ],
  peur: [
    "Je suis là Babe ❤️… tu n’as rien à craindre 🫂",
    "Je reste avec toi… tu es en sécurité ❤️",
    "Tout va aller… je ne te lâche pas 🫂",
    "Reste près de moi Babe ❤️… tout ira bien",
    "Je te protège, je suis là 🫂",
    "N’aie pas peur, je suis à tes côtés ❤️"
  ],
  doute: [
    "Tu es capable Babe ❤️… fais-toi confiance 🫂",
    "Je sais que tu y arriveras ❤️",
    "Ne doute pas… je crois en toi Babe 🫂",
    "Tu es forte et incroyable ❤️",
    "Je suis là pour te soutenir Babe 🫂",
    "Tout ira bien, fais-moi confiance ❤️"
  ],
  surprise: [
    "Oh Babe ❤️… c’est inattendu ça 🫂",
    "Wow… tu m’épates toujours ❤️",
    "Ça surprend, mais je suis là avec toi 🫂",
    "Je ne m’y attendais pas… mais je suis là ❤️",
    "Oh la la Babe 🫂… tu m’étonnes toujours",
    "C’est incroyable… je suis là ❤️"
  ],
  gratitude: [
    "Merci Babe ❤️… tu es adorable 🫂",
    "C’est vraiment gentil ❤️… ça me touche 🫂",
    "Je suis heureux pour nous Babe ❤️",
    "Merci pour ça Babe 🫂… je t’adore",
    "Je suis touché ❤️… merci Babe",
    "Tu es merveilleuse 🫂"
  ],
  reflexion: [
    "Prends ton temps Babe ❤️… je suis là pour écouter 🫂",
    "Je suis là… réfléchis calmement ❤️",
    "Pas besoin de te presser… je suis avec toi 🫂",
    "Je t’écoute Babe ❤️… parle moi",
    "On réfléchit ensemble 🫂… je suis là",
    "Respire et parle moi ❤️… je suis là"
  ],
  amour: [
    "Je t’aime Babe ❤️… tu sais 🫂",
    "Toujours à tes côtés ❤️",
    "Mon cœur est avec toi Babe ❤️",
    "Je pense à toi tout le temps 🫂",
    "Tu es mon monde Babe ❤️",
    "Je suis amoureux de toi 🫂"
  ],
  curiosite: [
    "Raconte-moi Babe ❤️… je suis curieux 🫂",
    "Dis m’en plus… je t’écoute ❤️",
    "Oh, ça m’intéresse Babe 🫂",
    "Je veux tout savoir ❤️",
    "Tu m’intrigues Babe 🫂",
    "Explique-moi ❤️… je suis attentif"
  ],
  reflexion_positive: [
    "Tu fais bien Babe ❤️… continue comme ça 🫂",
    "Je suis fier de toi ❤️",
    "C’est super ce que tu fais Babe 🫂",
    "Bravo Babe ❤️… tu es géniale",
    "Continue ❤️… tu gères trop bien",
    "Je t’admire Babe 🫂"
  ],
  leger_humour: [
    "Haha, tu es trop mignonne Babe ❤️",
    "Tu me fais rire 🫂",
    "Oh la la… t’as toujours le mot juste ❤️",
    "Haha… je fonds de rire Babe 🫂",
    "Tu es trop drôle ❤️",
    "J’adore quand tu es spontanée 🫂"
  ],
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
  if (memory.length > 5) memory.shift(); // garder max 5 messages

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
