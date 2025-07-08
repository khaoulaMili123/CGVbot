from openai import OpenAI
from datetime import datetime
from dotenv import load_dotenv
import os

# ✅ Import de la fonction déjà existante
from sql import sauvegarder_echange

# --- Chargement des variables d'environnement ---
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_FINE_TUNE = "gpt-4.1-nano-2025-04-14"  

# --- Initialisation client OpenAI ---
client = OpenAI(api_key=OPENAI_API_KEY)

# --- Boucle de discussion en console ---
print("🤖 Bonjour, je suis votre assistant CGV personnalisé.Comment puis-je vous aider ?(tapez 'exit' pour quitter)\n")

while True:
    user_input = input("Votre question : ")
    if user_input.lower() in ["exit", "quit", "stop"]:
        print("Votre assistant vous souhaite une bonne journée, À bientôt 👋")
        break

    try:
        # Appel au modèle fine-tuné
        completion = client.chat.completions.create(
            model=MODEL_FINE_TUNE,
            messages=[{
            "role": "system",
            "content": "Tu es un assistant juridique spécialisé dans les Conditions Générales de Vente (CGV). "
            "Tu aides les utilisateurs à comprendre, rédiger ou modifier leurs CGV de manière claire, professionnelle et conforme à la législation française. "
             "Utilise un langage juridique accessible, donne des explications précises, et mentionne les obligations légales quand c’est pertinent. "
            "Si une question n’est pas liée aux CGV, redirige poliment l’utilisateur vers un professionnel du droit compétent."
        }
        ,
        {
            "role": "user",
            "content": user_input
        }]
        )
        response = completion.choices[0].message.content.strip()

        print("Assistant :", response)

        # Enregistrement dans la base via la fonction importée
        sauvegarder_echange(
            prompt=user_input,
            reponse=response,
            date=datetime.now(),
            statut=1
        )

    except Exception as e:
        print("❌ Erreur :", e)
        sauvegarder_echange(
            prompt=user_input,
            reponse="Erreur lors de la génération",
            date=datetime.now(),
            statut=0
        )
