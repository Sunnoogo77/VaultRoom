from flask import Flask, session
from flask_socketio import SocketIO
from extensions import db, bcrypt
from routes import main
from socketio_instance import socketio
import os

socketio = SocketIO()  # Initialisation de SocketIO
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
    app.secret_key = "votre_clé_secrète_super_secure_ici"

    # Initialiser les extensions
    db.init_app(app)
    bcrypt.init_app(app)
    socketio.init_app(app)  # Attacher SocketIO à Flask

    # Enregistrer les routes
    app.register_blueprint(main)

    return app



from flask_migrate import Migrate

migrate = Migrate()





if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)  # Utilisation de socketio.run au lieu de app.run
    print("Tables créées avec succès.")


def create_app():
    app = Flask(__name__,
                template_folder="../Frontend/templates",
                static_folder="../Frontend/static")

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.abspath('db.sqlite3')}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "votre_clé_secrète_super_secure_ici"

    db.init_app(app)
    migrate.init_app(app, db)  # Initialiser Flask-Migrate

    return app

