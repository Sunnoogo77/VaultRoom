## README Principal (Mise à jour)  

# VaultRoom : Une Solution Sécurisée pour Échanges et Partages 🔐  

## 🛠️ Objectif du Projet  
**VaultRoom** est une plateforme de communication et de partage sécurisée, conçue pour garantir la confidentialité des échanges entre utilisateurs. Ce projet met en œuvre des concepts fondamentaux de cybersécurité pour offrir une solution pratique et robuste, en combinant une interface moderne et un backend sécurisé.  

---

## ✨ Fonctionnalités Clés  

1. **Communication Sécurisée**  
   - Messages stockés en base de données avec chiffrement TLS pour protéger la confidentialité.  
   - Possibilité de discussion privée entre utilisateurs.  
2. **Authentification des Utilisateurs**  
   - Inscription et connexion avec validation sécurisée.  
3. **Interface Moderne et Intuitive**  
   - Chat simplifié et responsive avec des fonctionnalités interactives.  
4. **Gestion des Utilisateurs**  
   - Liste des utilisateurs connectés disponible sur le panneau latéral pour faciliter les interactions.  
5. **Extension et Évolutivité**  
   - Structure prête à intégrer des fonctionnalités en temps réel et des modules complémentaires.  

---

## 🌟 Technologies Utilisées  

- **Python (Flask)** : Backend pour les fonctionnalités et les API.  
- **HTML, CSS, JavaScript** : Construction de l'interface utilisateur (frontend).  
- **SQLite** : Base de données légère pour la gestion des utilisateurs et des messages.  
- **Socket.IO** *(option à venir)* : Préparé pour des communications en temps réel.  
- **TLS/SSL** : Pour sécuriser toutes les communications.  

---

## 📂 Organisation du Dépôt  

```plaintext
VaultRoom/
├── Backend/                    # Serveur principal
│   ├── app.py                  # Point d'entrée de l'application
│   ├── extensions.py           # Extensions Flask (DB, Bcrypt, etc.)
│   ├── models.py               # Modèles de données
│   ├── routes.py               # Routes Flask pour les fonctionnalités backend
│   ├── README.md               # Documentation backend
│   └── static/                 # Certificats TLS/SSL (optionnels)
│
├── Frontend/                   # Interface utilisateur
│   ├── templates/              # Fichiers HTML
│   │   ├── base.html           # Template de base
│   │   ├── home.html           # Page d'accueil
│   │   ├── login.html          # Page de connexion
│   │   ├── register.html       # Page d'inscription
│   │   ├── chat.html           # Interface de discussion
│   │   └── dashboard.html      # Tableau de bord
│   ├── static/                 # Fichiers CSS et JS
│   │   ├── css/
│   │   │   └── styles.css      # Styles globaux
│   │   └── js/
│   │       └── app.js          # Scripts interactifs
│   ├── README.md               # Documentation frontend
│
└── README.md                   # Documentation principale
```  

---

## 🚀 Pourquoi ce Projet ?  

VaultRoom a été conçu pour :  
- Explorer des concepts clés en cybersécurité tels que le chiffrement TLS/SSL.  
- Proposer une plateforme simple, moderne et extensible pour la communication privée.  
- Mettre en œuvre de bonnes pratiques pour le développement web sécurisé.  

---

## 📋 Étapes pour Démarrer  

1. **Pré-requis** :  
   - Python 3.8+  
   - Flask  
   - SQLite  

2. **Installation** :  
   ```bash
   git clone https://github.com/username/vaultroom.git
   cd vaultroom
   python -m venv env
   source env/bin/activate  # Sur Windows, utilisez env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Exécution** :  
   ```bash
   python app.py
   ```

4. **Accéder à l'application** :  
   Ouvrez un navigateur et rendez-vous sur `https://IP_DU_SERVER:80`.
   Pour un port pareil vous serez amener à l'éxécuter en tant qu'admin. POur éviter cela, vous pouvez changer le numéro du port. 8443 par exemple (https://IP_DU_SERVER:8443)  

