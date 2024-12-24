# Guide du Backend pour l'Application de Messagerie

## 1. Introduction  

Ce backend repose sur **Flask**, un micro-framework Python léger et puissant, pour orchestrer les fonctionnalités d'une application de messagerie. Il utilise **SQLite** comme base de données pour gérer les utilisateurs et les messages, et **Socket.IO** pour une communication en temps réel. Grâce à une architecture claire et modulable, ce projet est à la fois simple à comprendre et prêt à évoluer.

---

## 2. Structure du Projet  

Le projet est organisé de manière à favoriser la lisibilité et la maintenabilité :  

- **`app.py`** : Point d’entrée principal de l’application. Configure les extensions (Socket.IO, SQLAlchemy) et démarre le serveur.  
- **`extensions.py`** : Initialise les outils nécessaires comme SQLAlchemy pour les bases de données et Bcrypt pour le hachage des mots de passe.  
- **`models.py`** : Définit les structures des tables de la base de données, y compris les utilisateurs et les messages.  
- **`routes.py`** : Regroupe les routes pour l'authentification, la messagerie et la gestion des utilisateurs.  
- **`socketio_instance.py`** : Configure l’instance Socket.IO pour la communication en temps réel.  
- **`server.tls` et `client.tls`** : Certificats pour les connexions sécurisées (HTTPS).  
- **`requirements.txt`** : Liste les bibliothèques Python nécessaires au fonctionnement.  

---

## 3. Fonctionnalités Principales  

### A. Authentification  
- **Inscription** : Vérifie l’unicité des utilisateurs et hache les mots de passe avant de les sauvegarder.  
- **Connexion** : Valide les identifiants et démarre une session utilisateur sécurisée.  
- **Déconnexion** : Efface les informations de session pour protéger la vie privée.  

### B. Messagerie  
- **Messages privés** : Envoi et réception de messages entre utilisateurs.  
- **Historique** : Stockage des messages dans la base de données et récupération pour consultation.  

### C. Communication en temps réel (via Socket.IO)  
- Gestion des messages en temps réel dans des “rooms”.  
- Synchronisation instantanée entre utilisateurs connectés.  

### D. Gestion des Utilisateurs  
- **Liste des utilisateurs connectés** : Visualisez en temps réel les utilisateurs actifs.  
- **Exclusion automatique** : Filtrage pour ne pas afficher l'utilisateur connecté dans les listes.  

---

## 4. Installation et Lancement  

### Prérequis  
- Python **3.9+**.  
- Gestionnaire de dépendances comme **Pipenv** ou **virtualenv**.  

### Étapes d’installation  

1. **Cloner le projet** :  
   ```bash
   git clone https://github.com/Sunnoogo77/VaultRoom/
   cd backend
   ```

2. **Créer un environnement virtuel** :  
   ```bash
   python3 -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   ```

3. **Installer les dépendances** :  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la base de données** :  
   - Vérifiez la présence de `db.sqlite3`, ou initialisez-la avec Flask-Migrate :  
     ```bash
     flask db init
     flask db migrate -m "Initial migration"
     flask db upgrade
     ```

5. **Lancer le serveur** :  
   ```bash
   python app.py
   ```  
   Le serveur sera accessible à l’adresse [http://127.0.0.1:80](http://127.0.0.1:80).

---

## 5. Routes Disponibles  

### A. Authentification  
- **`POST /register`** : Enregistrement d’un nouvel utilisateur.  
- **`POST /login`** : Connexion d’un utilisateur existant.  
- **`GET /logout`** : Déconnexion de la session utilisateur.  

### B. Messagerie  
- **`POST /send-message`** : Envoi d’un message privé (avec stockage en base).  
- **`GET /get-messages`** : Récupération des messages pour afficher l’historique.  

### C. Gestion des Utilisateurs  
- **`GET /get-users`** : Liste des utilisateurs (sauf l’utilisateur connecté).  

### D. Pages Web  
- **`GET /login-page`** : Page de connexion.  
- **`GET /register-page`** : Page d’inscription.  
- **`GET /chat`** : Interface pour discuter avec un autre utilisateur.  

---

## 6. Modèles de la Base de Données  

### **A. Utilisateur (`User`)**  

| Champ         | Type         | Description                          |  
|---------------|--------------|--------------------------------------|  
| `id`          | Integer      | Identifiant unique.                 |  
| `username`    | String(80)   | Nom d’utilisateur.                  |  
| `email`       | String(120)  | Adresse email (unique).             |  
| `password`    | String(200)  | Mot de passe (haché).               |  

### **B. Message (`Message`)**  

| Champ         | Type         | Description                          |  
|---------------|--------------|--------------------------------------|  
| `id`          | Integer      | Identifiant unique.                 |  
| `sender_id`   | Integer      | ID de l’expéditeur (clé étrangère). |  
| `receiver_id` | Integer      | ID du destinataire (clé étrangère). |  
| `room`        | String(100)  | Identifiant unique de la “room”.    |  
| `content`     | Text         | Contenu du message.                 |  
| `timestamp`   | DateTime     | Date et heure d’envoi.              |  

---


En adoptant cette architecture, vous obtenez un backend robuste, modulable, et prêt à supporter une expérience utilisateur fluide et sécurisée. 🚀
