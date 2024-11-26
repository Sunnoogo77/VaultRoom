from flask import Flask
from extensions import db, bcrypt
from routes import main
import os

def create_app():
    #app = Flask(__name__)
    app = Flask(__name__,
    template_folder="../Frontend/templates",
    static_folder="../Frontend/static"
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.abspath('db.sqlite3')}"
    #app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialiser les extensions
    db.init_app(app)
    bcrypt.init_app(app)

    # Enregistrer les routes
    app.register_blueprint(main)

    return app



if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", debug=True)
    print("Tables créées avec succès.")

