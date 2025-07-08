import mysql.connector as mysql
from datetime import datetime
from dotenv import load_dotenv
import os

load_dotenv()

def sauvegarder_echange(prompt, reponse, date, statut):
        # Connexion à la base de données
        connexion = mysql.connect(
            host='localhost',
            user='root',       # à adapter
            password='example',  # à adapter
            database='cgvbot',
            port=3306          # à adapter si nécessaire
        )

        curseur = connexion.cursor()
        requete = """
                INSERT INTO echanges (n_conversation, prompt, reponse, date, statut)
                VALUES (1, %s, %s, %s, %s)
            """
        valeurs = (prompt, reponse, date, statut)
        curseur.execute(requete, valeurs)
        connexion.commit()
    
        curseur.close()
        connexion.close()


sauvegarder_echange(
    prompt="Quels sont les CGV applicables aux prestations ?",
    reponse="Les CGV applicables sont celles en vigueur à la date de signature.",
    date=datetime.now(),
    statut=1
)
