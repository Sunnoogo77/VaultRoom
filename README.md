# VaultRoom : Une Solution Sécurisée pour Échanges et Partages 🔐  

## 🛠️ Objectif du Projet  
**VaultRoom** est une plateforme de communication et de partage sécurisée, conçue pour garantir la confidentialité des échanges entre utilisateurs. Ce projet met en œuvre des concepts fondamentaux de cybersécurité pour offrir une solution pratique et robuste.  

---


## ✨ Fonctionnalités Clés  

1. **Communication Sécurisée**  
   - Messages chiffrés avec TLS/SSL pour protéger la confidentialité.  
2. **Authentification des Utilisateurs**  
   - Connexions sécurisées avec gestion des utilisateurs.  
3. **Interface Intuitive**  
   - Un chat simple et fonctionnel pour les utilisateurs.  
4. **Journalisation des Activités**  
   - Suivi des événements pour plus de transparence et un audit facile.  

---

## 🌟 Technologies Utilisées  

- **Python** : Langage principal pour le backend (serveur et sockets).  
- **React** : Framework JS pour l’interface utilisateur (frontend).  
- **SQLite** : Base de données légère pour gérer les utilisateurs et les journaux.  
- **Bind9, isc-dhcp-server** : Pour la configuration DNS/DHCP (optionnel).  
- **TLS/SSL** : Pour sécuriser les communications.  

---

## 🚀 Pourquoi ce Projet ?  

VaultRoom a été conçu pour explorer des concepts clés en cybersécurité, notamment :  
- La sécurisation des communications via des protocoles modernes (TLS/SSL).  
- L’authentification et la gestion des utilisateurs dans un environnement protégé.  
- L’intégration d’un réseau local sécurisé avec DNS et DHCP.  
- La sensibilisation aux bonnes pratiques en matière de sécurité.  

---

## 📂 Organisation du Dépôt  

```plaintext
VaultRoom/
├── Preparations/               # Préparations techniques optionnelles
│   ├── DNS_Config/             # Configuration DNS pour vaultroom.local
│   ├── DHCP_Config/            # Configuration DHCP pour le réseau local
│   ├── Firewall_Rules/         # Règles de pare-feu
│   ├── TLS_Security/           # Certificats TLS/SSL
│   └── README.md               # Explications des préparations
├── Backend/                    # Serveur principal
│   ├── server.py               # Serveur socket principal
│   └── README.md
├── Frontend/                   # Interface utilisateur
│   ├── index.html              # Page principale
│   ├── styles.css              # Fichiers CSS
│   └── app.js                  # Logiciel frontend
└── README.md                   # Documentation principale
