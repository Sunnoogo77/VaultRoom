import socket
import ssl

# Chemins vers les certificats
CERT_FILE = "/etc/vaultroom/ssl/vaultroom.crt"
KEY_FILE = "/etc/vaultroom/ssl/vaultroom.key"

# Créer une socket normale
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8443))  # Le serveur écoute sur le port 8443
server_socket.listen(5)
print("Serveur TLS en attente de connexions sécurisées...")

# Ajouter TLS/SSL à la socket
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)

with context.wrap_socket(server_socket, server_side=True) as secure_socket:
    while True:
        client_socket, addr = secure_socket.accept()
        print(f"Connexion sécurisée de {addr}")
        data = client_socket.recv(1024).decode()
        print(f"Données reçues : {data}")
        client_socket.sendall("Bienvenue sur VaultRoom en mode sécurisé!".encode("utf-8"))
        client_socket.close()
