1. Introduction

Ce backend utilise Flask pour gérer les fonctionnalités d’une application de messagerie, avec une base de données SQLite pour stocker les utilisateurs et les messages. Les routes couvrent l’authentification, la messagerie et la gestion en temps réel via Socket.IO.

2. Structure du Projet

Voici les principaux fichiers et leurs rôles :
	•	app.py : Point d’entrée de l’application. Configure les extensions (Socket.IO, SQLAlchemy) et démarre le serveur.
	•	extensions.py : Initialise les extensions comme SQLAlchemy pour la base de données et Bcrypt pour le hachage des mots de passe.
	•	models.py : Définit les modèles de la base de données pour les utilisateurs et les messages.
	•	routes.py : Contient les routes principales, y compris les fonctionnalités de messagerie, d’authentification et de gestion des utilisateurs.
	•	socketio_instance.py : Configure une instance Socket.IO.
	•	server.tls et client.tls : Contiennent les certificats nécessaires pour les connexions sécurisées.
	•	requirements.txt : Liste des dépendances Python nécessaires.

3. Fonctionnalités Principales

A. Authentification
	•	Inscription : Vérifie les doublons et hache les mots de passe avant de les stocker.
	•	Connexion : Valide les identifiants et démarre une session utilisateur.
	•	Déconnexion : Efface la session utilisateur.

B. Messagerie
	•	Envoyer et recevoir des messages entre utilisateurs.
	•	Stockage des messages dans une base de données.
	•	Récupération des messages pour l’historique des discussions.

C. Socket.IO (en option pour temps réel)
	•	Gère l’envoi et la réception des messages via des “rooms”.
	•	Permet une communication en temps réel entre les utilisateurs connectés.

D. Gestion des Utilisateurs
	•	Liste des utilisateurs connectés.
	•	Filtrage des utilisateurs pour exclure l’utilisateur connecté.

4. Installation et Lancement

Prérequis
	•	Python 3.9+.
	•	Pipenv ou virtualenv (pour gérer les dépendances).

Étapes
	1.	Cloner le projet :

git clone <URL_DU_REPO>
cd backend


	2.	Créer un environnement virtuel :

python3 -m venv env
source env/bin/activate  # Sur Windows : env\Scripts\activate


	3.	Installer les dépendances :

pip install -r requirements.txt


	4.	Configurer la base de données :
	•	Assurez-vous que db.sqlite3 existe dans le répertoire du projet, ou utilisez Flask-Migrate :

flask db init
flask db migrate -m "Initial migration"
flask db upgrade


	5.	Lancer le serveur :

python app.py

Le serveur sera accessible sur http://127.0.0.1:80.

5. Routes Disponibles

A. Authentification
	•	/register (POST) : Inscription des utilisateurs.
	•	/login (POST) : Connexion des utilisateurs.
	•	/logout (GET) : Déconnexion de l’utilisateur.

B. Messagerie
	•	/send-message (POST) : Envoie un message et l’enregistre dans la base de données.
	•	/get-messages (GET) : Récupère tous les messages entre deux utilisateurs.

C. Gestion des Utilisateurs
	•	/get-users (GET) : Récupère tous les utilisateurs sauf l’utilisateur connecté.

D. Pages Web
	•	/login-page : Affiche la page de connexion.
	•	/register-page : Affiche la page d’inscription.
	•	/chat : Affiche la discussion avec un autre utilisateur.

6. Modèles de la Base de Données

A. User

Champ	Type	Description
id	Integer	Identifiant unique de l’utilisateur.
username	String(80)	Nom d’utilisateur.
email	String(120)	Adresse email unique.
password	String(200)	Mot de passe haché.

B. Message

Champ	Type	Description
id	Integer	Identifiant unique du message.
sender_id	Integer	ID de l’expéditeur (clé étrangère).
receiver_id	Integer	ID du destinataire (clé étrangère).
room	String(100)	Identifiant de la “room” de discussion.
content	Text	Contenu du message.
timestamp	DateTime	Date et heure d’envoi.

7. Notes et Améliorations
	•	L’intégration de Socket.IO pour des messages en temps réel est partiellement implémentée.
	•	Des tests unitaires sont recommandés pour garantir la robustesse.
