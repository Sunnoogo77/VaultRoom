import socket
import ssl

# Configuration TLS
context = ssl.create_default_context()
context.check_hostname = False  # Désactiver la vérification du nom d’hôte
context.verify_mode = ssl.CERT_NONE  # Ne pas vérifier le certificat (car auto-signé)

# Connexion au serveur
with socket.create_connection(("192.168.1.2", 8443)) as client_socket:
    with context.wrap_socket(client_socket, server_hostname="vaultroom.local") as secure_socket:
        secure_socket.sendall(b"Hello VaultRoom!")
        response = secure_socket.recv(1024).decode()
        print(f"Réponse du serveur : {response}")
