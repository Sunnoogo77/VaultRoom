import socket
import ssl
import logging

# Configuration des logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Chemins vers les certificats
CERT_FILE = "/etc/vaultroom/ssl/vaultroom.crt"
KEY_FILE = "/etc/vaultroom/ssl/vaultroom.key"

# Créer une socket normale
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8443))  # Le serveur écoute sur le port 8443
server_socket.listen(5)
logging.info("Serveur TLS en attente de connexions sécurisées sur le port 8443...")

# Ajouter TLS/SSL à la socket
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

with context.wrap_socket(server_socket, server_side=True) as secure_socket:
    while True:
        try:
            client_socket, addr = secure_socket.accept()
            logging.info(f"Connexion sécurisée de {addr}")

            # Recevoir des données du client
            data = client_socket.recv(1024).decode()
            logging.info(f"Données reçues : {data}")

            # Envoyer une réponse au client
            client_socket.sendall("Bienvenue sur VaultRoom en mode sécurisé!".encode("utf-8"))

        except Exception as e:
            logging.error(f"Erreur pendant la connexion sécurisée : {e}")

        finally:
            client_socket.close()
