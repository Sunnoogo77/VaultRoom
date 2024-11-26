from flask import Blueprint, request, jsonify, render_template
from extensions import db, bcrypt
from models import User

main = Blueprint(
    "main",
    __name__,
    template_folder="../Frontend/templates",
    static_folder="../Frontend/static")

@main.route('/login-page')
def login_page():
    return render_template('login.html')

@main.route('/register-page')
def register_page():
    return render_template('register.html')


@main.route("/")
def home():
    return {"status": "Server is running successfully"}

# API pour l'enregistrement
@main.route('/register', methods=['POST'])
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
    #if User.query.filter_by(username=username).first():
     #   return jsonify({'error': 'Nom d’utilisateur déjà pris.'}), 400
    #if User.query.filter_by(email=email).first():
     #   return jsonify({'error': 'Email déjà utilisé.'}), 400

    try:
        if User.query.filter_by(username=username).first():
            return jsonify({'error': 'Nom d’utilisateur déjà pris.'}), 400
    except Exception as e:
        return jsonify({'error': 'Erreur de connexion à la base de données.', 'details': str(e)}), 500

    # Hacher le mot de passe
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    new_user = User(username=username, email=email, password=hashed_password)

    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'Utilisateur créé avec succès.'}), 201

# API pour la connexion
@main.route('/login', methods=['POST'])
def login():
    try:
        # 1. Récupérer les données envoyées par le client
        #data = request.json
        
        if request.is_json:
            data = request.get_json()
        else:
            # Gérer les données envoyées en `x-www-form-urlencoded`
            data = request.form.to_dict()
            
        username = data.get('username')
        password = data.get('password')

        # 2. Vérification des champs
        if not username or not password:
            return jsonify({'error': 'Tous les champs sont requis.'}), 400

        # 3. Rechercher l'utilisateur dans la base de données
        user = User.query.filter_by(username=username).first()
        if not user:
            return jsonify({'error': 'Nom d’utilisateur incorrect.'}), 401

        # 4. Vérifier le mot de passe
        if not bcrypt.check_password_hash(user.password, password):
            return jsonify({'error': 'Mot de passe incorrect.'}), 401

        # 5. Retourner une réponse si tout est OK
        return jsonify({'message': f'Bienvenue {user.username} !'}), 200

    except Exception as e:
        # Gestion des erreurs inattendues
        return jsonify({'error': 'Erreur interne.', 'details': str(e)}), 500


@main.route("/test-db")
def test_db():
    try:
        users = User.query.all()  # Tente de récupérer tous les utilisateurs
        return jsonify({"message": f"{len(users)} utilisateurs trouvés.", "status": "success"})
    except Exception as e:
        return jsonify({"message": str(e), "status": "error"})
