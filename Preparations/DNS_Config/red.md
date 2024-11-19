# Configuration DNS : vaultroom.local  

## 🎯 Objectif  
Ce dossier contient les fichiers nécessaires pour configurer un serveur DNS local avec Bind9. Cette configuration permet de résoudre le nom de domaine `vaultroom.local` en une adresse IP spécifique (192.168.1.2).  

---

## 🛠️ Étapes de Configuration  

### 1. Installer Bind9  
Utilisez la commande suivante pour installer Bind9 :  
```bash
sudo apt update && sudo apt install bind9
```

### 2. Configurer le Fichier `named.conf.local`  
Ajoutez la configuration suivante dans `/etc/bind/named.conf.local` :  
```plaintext
zone "vaultroom.local" {
    type master;
    file "/etc/bind/zones/db.vaultroom.local";
};
```
Créez le répertoire pour les fichiers de zones :  
```bash
sudo mkdir -p /etc/bind/zones
```

### 3. Créer le Fichier de Zone  
Créez et éditez `/etc/bind/zones/db.vaultroom.local` :  
```bash
sudo nano /etc/bind/zones/db.vaultroom.local
```
Ajoutez les informations suivantes :  
```plaintext
$TTL    604800
@       IN      SOA     vaultroom.local. root.vaultroom.local. (
                  2         ; Serial
             604800         ; Refresh
              86400         ; Retry
            2419200         ; Expire
             604800 )       ; Negative Cache TTL

; DNS records
@       IN      NS      vaultroom.local.
@       IN      A       192.168.1.2   ; Adresse IP de ton serveur DNS
www     IN      A       192.168.1.2   ; Adresse IP pour www.vaultroom.local

```

### 4. Redémarrer le Serveur DNS  
Appliquez les modifications :  
```bash
sudo systemctl restart bind9
```


## 📸 Captures d’Écran  

1. **ping_test_windows.png**  
   - Résultat de la commande `ping vaultroom.local` sur un client Windows.  

2. **dns_settings_windows.png**  
   - Paramètres réseau configurés pour utiliser `192.168.1.2` comme serveur DNS.  

---

## 📂 Fichiers Inclus  

1. `dns_zone_config.txt` : Contenu du fichier `/etc/bind/zones/db.vaultroom.local`.  
2. `bind9_config.txt` : Modifications apportées à `/etc/bind/named.conf.local`.
   
---

## 🚀 Lien avec le Projet Principal  

Cette configuration réseau garantit que les différentes machines et composants du projet **SecureCommHub** peuvent communiquer efficacement. Elle pose les bases pour une communication fiable entre le serveur et les clients.  

---


## 📖 Notes  
- Assurez-vous que le serveur DNS est accessible via l’adresse IP `192.168.1.2`.  
- Si le client ne peut pas résoudre `vaultroom.local`, vérifiez la configuration DNS sur le client.
