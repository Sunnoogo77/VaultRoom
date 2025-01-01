# README Principal  

## **VaultRoom : Une Solution Sécurisée pour Échanges et Partages** 🔐  

### 🛠️ **Objectif du Projet**  

VaultRoom est une plateforme conçue pour offrir une **communication sécurisée** et un **partage confidentiel** entre utilisateurs. Intégrant des principes fondamentaux de la cybersécurité, le projet associe une interface utilisateur moderne à un backend robuste, garantissant une expérience fiable et évolutive.  

---

### ✨ **Fonctionnalités Clés**  

1. **Communication Sécurisée**  
   - Messages stockés dans une base de données protégée, avec chiffrement **TLS** pour garantir leur confidentialité.  
   - Discussions privées sécurisées entre utilisateurs.  

2. **Authentification des Utilisateurs**  
   - Inscription et connexion sécurisées, avec validation stricte des informations.  

3. **Interface Moderne et Intuitive**  
   - Un chat responsive avec une navigation simplifiée et des fonctionnalités interactives.  

4. **Gestion des Utilisateurs**  
   - Vue des utilisateurs connectés pour initier des discussions rapidement.  

5. **Évolutivité**  
   - Architecture prête pour des fonctionnalités en temps réel via **Socket.IO** et d’autres extensions.  

---

### 🌟 **Technologies Utilisées**  

- **Python (Flask)** : Backend principal et API.  
- **HTML, CSS, JavaScript** : Création d'une interface utilisateur réactive.  
- **SQLite** : Base de données légère pour gérer utilisateurs et messages.  
- **Socket.IO (à venir)** : Pour une communication en temps réel.  
- **TLS/SSL** : Sécurisation des communications avec des certificats.  

---

### 📂 **Organisation du Dépôt**  

```plaintext
VaultRoom/
├── Backend/                    # Serveur principal
│   ├── app.py                  # Point d'entrée de l'application
│   ├── extensions.py           # Extensions Flask (DB, Bcrypt, etc.)
│   ├── models.py               # Modèles de données
│   ├── routes.py               # Routes backend
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
│   ├── static/                 # CSS et JS
│   │   ├── css/
│   │   │   └── styles.css      # Feuille de style globale
│   │   └── js/
│   │       └── app.js          # Scripts interactifs
│   ├── README.md               # Documentation frontend
│
└── README.md                   # Documentation principale
```

---

### 🚀 **Pourquoi ce Projet ?**  

VaultRoom a été créé pour :  
- Explorer des concepts de cybersécurité comme le chiffrement TLS/SSL.  
- Fournir une plateforme de communication simple, extensible et sécurisée.  
- Adopter de bonnes pratiques de développement web pour garantir sécurité et efficacité.  

---

### 📋 **Étapes pour Démarrer**  

1. **Pré-requis** :  
   - Python **3.8+**  
   - Flask  
   - SQLite  

2. **Installation** :  
   ```bash
   git clone https://github.com/username/vaultroom.git
   cd vaultroom
   python -m venv env
   source env/bin/activate  # Sous Windows : env\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Exécution** :  
   ```bash
   python3 app.py
   ``` 
