# README pour le Dossier `templates`  

## Introduction  

Le dossier `templates` regroupe tous les fichiers **HTML** qui définissent l’interface utilisateur de **VaultRoom**, une application de messagerie dynamique. Ces fichiers sont rendus par **Flask**, ce qui permet de générer du contenu adapté aux données du backend, offrant une expérience utilisateur fluide et interactive.  

---

## Structure des Fichiers  

### 1. **`base.html`**  
#### Rôle  
Template principal sur lequel toutes les autres pages se basent. Grâce à `{% extends 'base.html' %}`, les fichiers enfants héritent de sa structure et de ses styles.  

#### Composants principaux  
- **Barre de navigation** :  
  - Lien vers la page d’accueil (`/home`).  
  - Bouton de déconnexion (`/logout`).  
- **Bloc de contenu dynamique** : `{% block content %}` où chaque page injecte son contenu spécifique.  

#### Particularités  
- Référence le fichier CSS principal : `../static/css/styles.css`.  
- Intègre **Socket.IO** pour gérer les événements en temps réel.  

---

### 2. **`home.html`**  
#### Rôle  
Page d’accueil de l’application, présentant un aperçu des fonctionnalités principales.  

#### Contenu  
- Message de bienvenue personnalisé.  
- Trois boutons pour :  
  - Se connecter (`/login-page`).  
  - S’inscrire (`/register-page`).  
  - Commencer immédiatement (`/newone`).  

#### Styles  
- Une structure CSS immersive avec une mise en page en pleine page et des styles attractifs.  

---

### 3. **`login.html`**  
#### Rôle  
Permet aux utilisateurs de se connecter à leur compte.  

#### Contenu  
- **Formulaire de connexion** :  
  - Champ pour le nom d’utilisateur.  
  - Champ pour le mot de passe.  
  - Bouton pour soumettre le formulaire.  

#### Scripts  
- Envoi des données au backend via **`fetch`** pour validation.  
- Gestion des erreurs : Affichage dynamique des messages en cas de problème.  

---

### 4. **`register.html`**  
#### Rôle  
Page dédiée à l’inscription des nouveaux utilisateurs.  

#### Contenu  
- **Formulaire d’inscription** :  
  - Champ pour le nom d’utilisateur.  
  - Champ pour l’adresse email.  
  - Champ pour le mot de passe.  
  - Bouton pour soumettre les informations.  

#### Particularités  
- Fonctionnalité proche de `login.html` avec un focus sur la validation des données utilisateur.  

---

### 5. **`chat.html`**  
#### Rôle  
Interface principale pour discuter en temps réel avec d’autres utilisateurs.  

#### Contenu  
- **Colonne gauche** : Liste des utilisateurs connectés, avec des liens pour démarrer une conversation.  
- **Section principale** :  
  - Affiche les messages échangés avec l’utilisateur sélectionné.  
  - Formulaire pour envoyer de nouveaux messages.  

#### Scripts  
- Chargement dynamique des messages via l’API `/get-messages`.  
- Envoi des messages via l’API `/send-message`.  
- Rechargement automatique pour actualiser les messages après chaque envoi.  

---

### 6. **`dashboard.html`**  
#### Rôle  
Tableau de bord affichant une vue globale des utilisateurs connectés.  

#### Contenu  
- Liste des utilisateurs disponibles, avec des liens directs pour accéder aux conversations.  
- Message de bienvenue personnalisé pour l’utilisateur connecté.  

#### Particularités  
- Facilite l’accès rapide aux conversations.  

---

## Relations entre les Fichiers  

- **Héritage** : Toutes les pages HTML dépendent de `base.html` pour les composants communs (navigation, styles).  
- **CSS** : Les fichiers situés dans `../static/css` assurent une mise en page cohérente et élégante.  
- **API** : Les pages interagissent avec le backend via Flask pour les opérations critiques comme l’inscription, la connexion, et la messagerie.  

---

## Instructions pour Ajouter de Nouveaux Fichiers  

1. **Créer un fichier HTML** dans le dossier `templates`.  
2. Utiliser `{% extends 'base.html' %}` pour intégrer la navigation et les styles communs.  
3. Ajouter le contenu spécifique de la page dans un bloc `{% block content %}`.  

---

## Résumé  

Ce README fournit une vue complète de la structure et du rôle des fichiers HTML du projet **VaultRoom**. Grâce à une organisation claire et des relations bien définies entre les fichiers, il est facile d’étendre ou d’adapter l’interface utilisateur selon vos besoins.  

Profitez de cette base solide pour construire des interfaces engageantes et performantes ! 🚀  
