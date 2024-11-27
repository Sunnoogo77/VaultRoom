from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
from extensions import db, bcrypt
from models import User, Message

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
        
        # Enregistrement des informations dans la session
        session['user_id'] = user.id
        session['username'] = user.username

        # 5. Retourner une réponse si tout est OK
        #return jsonify({'message': f'Bienvenue {user.username} !'}), 200

        #Si la connexion est réussi, rediriger vers le Dashboard
        return redirect(url_for('main.dashboard'))
        

    except Exception as e:
        # Gestion des erreurs inattendues
        return jsonify({'error': 'Erreur interne.', 'details': str(e)}), 500

#Route pour envoyer les messages
@main.route('/send-message', methods=['POST'])
def send_message():

    if 'user_id' not in session:
        return jsonify({'error': 'Vous devez être connecté pour envoyer un message.'}), 401
    
    if request.is_json:
        data = request.get_json()
    else:
        data = request.form.to_dict()

    sender_id = session['user_id']
    receiver_id = data.get('receiver_id')
    room = data.get('room')
    content = data.get('message')

    #if not sender_id or not content:
        #return jsonify({'error': 'Les champs sender_id et content sont requis.'}), 400

    # Création du message
    #{message = Message(sender_id=sender_id, receiver_id=receiver_id, room=room, content=content)
    
    try:
        # Ajouter le message dans la base de données
        new_message = Message(
            sender_id=sender_id,
            receiver_id=receiver_id,
            content=content
        )

        db.session.add(message)
        db.session.commit()

        return jsonify({
            'sender': 'Moi',
            'content': content,
            'timestamp': new_message.timestamp.strftime('%d/%m/%Y %H:%M:%S')
        }), 201
    
        #return jsonify({'message': 'Message envoyé avec succès.'}), 201
    except Exception as e:
        return jsonify({'error': 'Erreur lors de l\'envoi du message.', 'details': str(e)}), 500

#Routes pour recevoir les messages
@main.route('/get-messages/<int:receiver_id>', methods=['GET'])
def get_messages():
    if 'user_id' not in session:
        return jsonify({'error': 'Vous devez être connecté pour voir les messages.'}), 401
    
    room = request.args.get('room')
    sender_id = session['user_id']
    receiver_id = request.args.get('receiver_id')

    try:
        if room:
            messages = Message.query.filter_by(room=room).all()
        elif sender_id and receiver_id:
            messages = Message.query.filter(
                (Message.sender_id == sender_id) & (Message.receiver_id == receiver_id) |
                (Message.sender_id == receiver_id) & (Message.receiver_id == sender_id)
            ).all()
        else:
            return jsonify({'error': 'Veuillez spécifier une room ou un sender_id/receiver_id.'}), 400

        return jsonify([{
            'id': msg.id,
            'sender_id': msg.sender_id,
            'receiver_id': msg.receiver_id,
            'room': msg.room,
            'content': msg.content,
            'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        } for msg in messages]), 200

    except Exception as e:
        return jsonify({'error': 'Erreur lors de la récupération des messages.', 'details': str(e)}), 500

#route pour afficher Dashboard
@main.route('/dashboard')
def dashboard():
    try:
        #Vérifie si l'utilisateur est connecter
        if 'user_id' not in session:
            return redirect(url_for('main.login_page'))  # Redirige vers login si pas connecté
        # Exemple d'utilisateur connecté (remplacez ceci par l'authentification réelle)
        current_user = {
            "id": session['user_id'],
            "username": session['username']}  

        # Récupérer tous les utilisateurs dans la base de données
        users = User.query.filter(User.username != current_user['username']).all()
        
        return render_template('dashboard.html', users=users, user=current_user)
    except Exception as e:
        return jsonify({"error": "Erreur lors du chargement des utilisateurs", "details": str(e)})

#Route pour le Chats
@main.route('/chat', methods=['GET', 'POST'])
def chat():
    # Récupérer les informations utilisateur à partir de la session
    current_user_id = session.get('user_id')
    if not current_user_id:
        return jsonify({"error": "Utilisateur non authentifié"}), 401

    if request.method == 'GET':
        recipient_id = request.args.get('user_id')
        recipient = User.query.get(recipient_id)

        if not recipient:
            return jsonify({"error": "Utilisateur non trouvé"}), 404

        # Récupérer les messages entre l'utilisateur actuel et le destinataire
        messages = Message.query.filter(
            ((Message.sender_id == current_user_id) & (Message.receiver_id == recipient.id)) |
            ((Message.sender_id == recipient.id) & (Message.receiver_id == current_user_id))
        ).order_by(Message.timestamp.asc()).all()

        return render_template('chat.html', messages=messages, recipient=recipient, user={"id": current_user_id})

    elif request.method == 'POST':
        # Envoi d'un message
        data = request.form
        content = data.get('message')
        recipient_id = data.get('recipient_id')

        if not content:
            return jsonify({"error": "Le message ne peut pas être vide"}), 400

        try:
            new_message = Message(sender_id=current_user_id, receiver_id=recipient_id, content=content)
            db.session.add(new_message)
            db.session.commit()
            return jsonify({
                "message": "Message envoyé avec succès",
                "content": content,
                "timestamp": new_message.timestamp.strftime('%d/%m/%Y %H:%M:%S')
            }), 200
        except Exception as e:
            return jsonify({"error": "Erreur lors de l'envoi du message", "details": str(e)}), 500


@main.route("/test-db")
def test_db():
    try:
        users = User.query.all()  # Tente de récupérer tous les utilisateurs
        return jsonify({"message": f"{len(users)} utilisateurs trouvés.", "status": "success"})
    except Exception as e:
        return jsonify({"message": str(e), "status": "error"})

@main.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', message="Page non trouvée."), 404

@main.errorhandler(500)
def internal_server_error(e):
    return render_template('error.html', message="Erreur interne du serveur."), 500
