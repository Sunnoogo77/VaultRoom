import socket
import ssl
import logging

# Configuration des logs
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# Configuration TLS
CERT_FILE = "/etc/vaultroom/ssl/vaultroom.crt"  # Certificat du serveur
context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
context.load_verify_locations(cafile=CERT_FILE)  # Vérifie le certificat du serveur
context.check_hostname = True  # Active la vérification du nom d'hôte

# Connexion au serveur
SERVER_HOST = "vaultroom.local"
SERVER_PORT = 8443

try:
    with socket.create_connection((SERVER_HOST, SERVER_PORT)) as client_socket:
        with context.wrap_socket(client_socket, server_hostname=SERVER_HOST) as secure_socket:
            logging.info("Connexion sécurisée établie avec le serveur.")
            
            # Envoyer des données au serveur
            secure_socket.sendall(b"Hello VaultRoom!")
            logging.info("Message envoyé au serveur.")

            # Recevoir une réponse du serveur
            response = secure_socket.recv(1024).decode()
            logging.info(f"Réponse du serveur : {response}")

except ssl.SSLError as e:
    logging.error(f"Erreur TLS/SSL : {e}")

except Exception as e:
    logging.error(f"Erreur pendant la connexion : {e}")
