# Sécurisation avec TLS/SSL  

## 🎯 Objectif  
Ce dossier contient les fichiers nécessaires pour sécuriser les communications entre le serveur et les clients VaultRoom à l'aide de TLS/SSL.  

---

## 🛠️ Étapes de Configuration  

### 1. Génération des Certificats  
Les certificats ont été générés avec les commandes suivantes :  
```bash
sudo openssl genrsa -out vaultroom.key 2048
sudo openssl req -new -x509 -key vaultroom.key -out vaultroom.crt -days 365
```

### 2. Fichiers Inclus  
1. `vaultroom.crt` : Certificat SSL auto-signé.  
2. `vaultroom.key` : Clé privée utilisée pour signer le certificat.  

### 3. Intégration au Serveur Python  
- Voir le fichier `server_tls.py` pour un exemple d’utilisation.  

---

## 📖 Notes  
- Les certificats auto-signés ne sont pas recommandés en production. Pour un déploiement réel, utilisez un certificat signé par une autorité de certification (CA).
