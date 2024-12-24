## **VaultRoom Frontend**  

### 🖼️ **Description**  

Le frontend de VaultRoom regroupe tous les fichiers nécessaires pour une interface utilisateur élégante et interactive. Il inclut :  
- **Templates HTML** pour structurer les pages.  
- **CSS** pour les styles.  
- **JavaScript** pour des interactions dynamiques.  

---

### 📂 **Structure**  

```plaintext
Frontend/
├── templates/                  # Contient tous les fichiers HTML
│   ├── base.html               # Template principal
│   ├── home.html               # Page d'accueil
│   ├── login.html              # Page de connexion
│   ├── register.html           # Page d'inscription
│   ├── chat.html               # Interface de discussion
│   └── dashboard.html          # Tableau de bord utilisateur
│
├── static/                     # Contient CSS et JS
│   ├── css/
│   │   └── styles.css          # Feuille de style globale
│   ├── js/
│   │   └── app.js              # Scripts interactifs
```

---

### 💡 **Fonctionnalités**  

1. **Accueil (home.html)** : Présentation de l’application avec options pour se connecter ou s’inscrire.  
2. **Connexion (login.html)** : Formulaire sécurisé pour l’authentification.  
3. **Inscription (register.html)** : Création de nouveaux comptes.  
4. **Discussion (chat.html)** : Envoi et réception de messages en temps réel.  
5. **Tableau de bord (dashboard.html)** : Vue globale des utilisateurs connectés.  

---

### 🎨 **Style**  

Tous les styles sont centralisés dans le fichier **`styles.css`**, garantissant :  
- Une apparence uniforme sur toutes les pages.  
- Une maintenance simplifiée pour des modifications globales.  

---

### 📋 **Étapes pour Modifier**  

1. **Modifier une page** :  
   - Les fichiers HTML dans `templates/` peuvent être édités directement.  

2. **Changer les styles** :  
   - Modifiez les classes ou les propriétés dans `static/css/styles.css`.  

3. **Ajouter une fonctionnalité interactive** :  
   - Ajoutez ou modifiez les scripts dans `static/js/app.js`.  

---

### 🛠️ **Extension et Maintenance**  

Le frontend est conçu pour être facilement extensible. Si des fonctionnalités supplémentaires sont nécessaires, suivez ces étapes :  
1. Ajoutez un fichier HTML dans `templates/` pour une nouvelle page.  
2. Incluez les éléments de base en héritant de `base.html` avec `{% extends 'base.html' %}`.  
3. Appliquez vos styles dans **`styles.css`**.  
4. Ajoutez des interactions spécifiques dans **`app.js`**.  
