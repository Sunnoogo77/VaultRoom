# Configuration DHCP  

## 🎯 Objectif  
Ce dossier contient les fichiers nécessaires pour configurer un serveur DHCP avec isc-dhcp-server. Cette configuration attribue automatiquement des adresses IP aux clients sur le réseau local.  

---

## 🛠️ Étapes de Configuration  

### 1. Installer isc-dhcp-server  
Utilisez la commande suivante pour installer le serveur DHCP :  
```bash
sudo apt update && sudo apt install isc-dhcp-server
```

### 2. Configurer le Fichier `dhcpd.conf`  
Modifiez le fichier `/etc/dhcp/dhcpd.conf` pour définir la plage d’adresses et les options DHCP :  
```plaintext
subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.10 192.168.1.100;
    option routers 192.168.1.1;
    option domain-name-servers 192.168.1.2;
    option domain-name "vaultroom.local";
    default-lease-time 2592000;
    max-lease-time 2592000;
}
```

### 3. Configurer l’Interface Réseau  
Ajoutez ou modifiez `/etc/network/interfaces` pour configurer une adresse statique sur le serveur :  
```plaintext
iface ens36 inet static
    address 192.168.1.2
    netmask 255.255.255.0
```

### 4. Redémarrer le Serveur DHCP  
Appliquez les modifications avec les commandes suivantes :  
```bash
sudo systemctl restart isc-dhcp-server
sudo systemctl restart networking
```

### 5. Tester le DHCP  
Depuis un client Windows ou Linux, vérifiez que l’adresse IP est attribuée automatiquement :  
- **Sur Windows** :  
  Ouvrez l’invite de commandes et tapez :  
  ```cmd
  ipconfig /all
  ```
- **Sur Linux** :  
  Exécutez :  
  ```bash
  ip a
  ```

---

## 📸 Captures d’Écran  

1. **dhcp_ipconfig_windows.png**  
   - Résultat de la commande `ipconfig /all`, montrant que l’adresse IP a été attribuée dynamiquement.  

---

## 📂 Fichiers Inclus  

1. `dhcp_config.txt` : Contenu du fichier `/etc/dhcp/dhcpd.conf`.  
2. `interfaces_config.txt` : Contenu du fichier `/etc/network/interfaces`.  

---

## 📖 Notes  
- Pour modifier la durée des baux DHCP, ajustez les valeurs `default-lease-time` et `max-lease-time` dans le fichier `dhcpd.conf`.  
- Redémarrez les services réseau après toute modification.
