from flask import Flask, session
from flask_socketio import SocketIO
from extensions import db, bcrypt
from routes import main
from socketio_instance import socketio
from flask_migrate import Migrate
import os

socketio = SocketIO()  # Initialisation de SocketIO
migrate = Migrate()
#++
def create_app():
    #app = Flask(__name__)
    app = Flask(__name__,
    template_folder="../Frontend/templates",
    static_folder="../Frontend/static"
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.abspath('db.sqlite3')}"
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Clé secrète pour sécuriser les sessions
    app.secret_key = "t0nPr0jetVaultR00mEstBienS3cur1sé!"

    # Initialiser les extensions
    db.init_app(app)
    bcrypt.init_app(app)
    socketio.init_app(app)  # Attacher SocketIO à Flask
    migrate.init_app(app, db)

    # Enregistrer les routes
    app.register_blueprint(main)

    return app






if __name__ == "__main__":
    app = create_app()

    # Chemins vers les certificats
    CERT_FILE = "/etc/vaultroom/ssl/vaultroom.crt"
    KEY_FILE = "/etc/vaultroom/ssl/vaultroom.key"

    with app.app_context():
        db.create_all()

    #Lancer le serveur via https
    socketio.run(app, debug=True, host="0.0.0.0", port=80, ssl_context=(CERT_FILE, KEY_FILE))  # Utilisation de socketio.run au lieu de app.run

