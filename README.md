# CGVbot
Un chatbot en ligne de commande capable de répondre automatiquement aux questions liées aux Conditions Générales de Vente (CGV)
Fonctionnalités :
Envoie de questions via la console

Génération de réponses via un modèle OpenAI fin-tunning

Enregistrement des échanges dans une base MySQL (via Docker)

Possibilité d’accéder à la BDD avec Adminer

Pré-prompt métier intégré dans les données d'entraînement

Technologies utilisées :
Python 3.10+

OpenAI API

MySQL 8 + Adminer

Docker / Docker Compose

python-dotenv, mysql-connector-python

Installation
1. Cloner le projet
git clone https://github.com/<ton-pseudo>/chatbot-cgv-moneshop.git
cd chatbot-cgv-moneshop
2. Créer un fichier .env
À la racine du projet, crée un fichier .env :

env
OPENAI_API_KEY=...
Ne partage jamais cette clé sur GitHub – le fichier .env est ignoré automatiquement.

3. Installer les dépendances Python
Active ton environnement virtuel puis :

pip install -r requirements.txt
4. Lancer la base de données avec Docker
docker-compose up -d
Accès à Adminer : http://localhost:8080

Identifiants :

Serveur : db

Utilisateur :...

Mot de passe : ...

Base : cgvbot

5. Créer la base et la table (dans Adminer ou en SQL)
Structure du projet
bash
Copier
Modifier
chatbot_cgv/
├── chatbot_console.py     # Interface console
├── sql.py                 # Fonction pour enregistrer les échanges
├── train/train.jsonl      # Fichier d'entraînement
├── docker-compose.yml     # MySQL + Adminer
├── requirements.txt       # Dépendances Python
├── .env                   # Clé API OpenAI (non commitée)
├── .gitignore             # Fichiers à ne pas versionner
└── README.md              # Ce fichier
