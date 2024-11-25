from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_socketio import SocketIO, emit, join_room, leave_room
import os

from extensions import db


#app = Flask(__name__)
app = Flask(
    __name__,
    template_folder="../Frontend/templates",  # Chemin relatif au fichier app.py
    static_folder="../Frontend/static"
)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)


bcrypt = Bcrypt(app)
socketio = SocketIO(app)

# Importer les modèles
from models import User

# Routes HTML
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

# API pour l'enregistrement
@app.route('/register', methods=['POST'])
def register():
    #data = request.json
    # Vérifier si la requête contient du JSON
    if request.is_json:
        data = request.get_json()
    else:
        # Gérer les données envoyées en `x-www-form-urlencoded`
        data = request.form.to_dict()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Tous les champs sont requis.'}), 400

    # Vérifier si l'utilisateur existe déjà
    if User.query.filter_by(username=username).first():
        return jsonify({'error': 'Nom d’utilisateur déjà pris.'}), 400
    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Email déjà utilisé.'}), 400

    # Hacher le mot de passe
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Utilisateur créé avec succès.'}), 201

# API pour la connexion
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Tous les champs sont requis.'}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'error': 'Nom d’utilisateur ou mot de passe incorrect.'}), 401

    return jsonify({'message': f'Bienvenue {user.username} !'}), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)
