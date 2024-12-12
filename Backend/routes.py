from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session
from flask_socketio import emit, join_room, leave_room
from extensions import db, bcrypt
from models import User, Message
from socketio_instance import socketio

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
    return render_template('home.html')

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
    return render_template('home.html')

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
    

#-----------------------------------

#Joinning Chat
@socketio.on('join_chat')
def handle_join_chat(data):
    # 1. Obtenir l'ID de l'utilisateur connecté
    user_id = session.get('user_id')
    
    # 2. Vérifier que l'utilisateur est bien authentifié
    if user_id:
        # 3. Ajouter l'utilisateur à une room dédiée (son user_id)
        join_room(str(user_id))
        
        # 4. Informer les autres (ou le système) qu'il a rejoint la room
        emit('info', {'message': f'{session["username"]} a rejoint la discussion.'}, room=str(user_id))



# Route pour envoyer un message via WebSocket
@socketio.on('send_message')
def handle_send_message(data):

    

    try:

        if 'user_id' not in session:
            return jsonify({'error': 'Vous devez être connecté pour voir les messages.'}), 401
    
        sender_id = session.get('user_id')
        receiver_id = data.get('receiver_id')
        content = data.get('message')

        if not sender_id or not receiver_id or not content:
            emit('error', {'error': 'Données incomplètes pour envoyer un message.'}, room=request.sid)
            return
    
        recipient = User.query.get(receiver_id)
        if not recipient:
            emit('error', {'error': 'Destinataire introuvable.'}, room=request.sid)
            return


        # Ajouter le message dans la base de données
        new_message = Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
        db.session.add(new_message)
        db.session.commit()

        # Émettre le message en temps réel au destinataire
        emit('receive_message', {
            'sender': 'Moi' if sender_id == session['user_id'] else User.query.get(sender_id).username,
            'content': content,
            'timestamp': new_message.timestamp.strftime('%d/%m/%Y %H:%M:%S')
        }, room=str(receiver_id))
    except Exception as e:
        emit('error', {'error': f'Erreur lors de l\'envoi du message : {str(e)}'}, room=request.sid)


# Route pour rejoindre une discussion
@main.route('/get-messages', methods=['GET'])
def get_messages():
    if 'user_id' not in session:
        return jsonify({'error': 'Vous devez être connecté pour voir les messages.'}), 401

    sender_id = session['user_id']
    receiver_id = request.args.get('receiver_id')

    if not receiver_id:
        return jsonify({'error': 'Aucun destinataire spécifié.'}), 400

    try:
        # Récupérer tous les messages envoyés et reçus dans une seule requête
        all_messages = Message.query.filter(
            ((Message.sender_id == sender_id) & (Message.receiver_id == receiver_id)) |
            ((Message.sender_id == receiver_id) & (Message.receiver_id == sender_id))
        ).order_by(Message.timestamp.asc()).all()

        # Formater les messages pour le JSON
        messages_json = [{
            'sender': 'Moi' if msg.sender_id == sender_id else User.query.get(msg.sender_id).username,
            'content': msg.content,
            'timestamp': msg.timestamp.strftime('%d/%m/%Y %H:%M:%S')
        } for msg in all_messages]

        return jsonify(messages_json), 200

    except Exception as e:
        return jsonify({'error': 'Erreur lors de la récupération des messages.', 'details': str(e)}), 500
    
# Route pour afficher la page de discussion
@main.route('/chat', methods=['GET'])
def chat():
    current_user_id = session.get('user_id')
    if not current_user_id:
        return jsonify({"error": "Utilisateur non authentifié"}), 401

    # Récupérer l'ID du destinataire à partir des paramètres de l'URL
    recipient_id = request.args.get('user_id')  # Cela doit correspondre à l'URL
    print(f"Recipient ID: {recipient_id}")  # DEBUG: Afficher l'ID du destinataire

    if not recipient_id:
        return jsonify({"error": "Aucun destinataire spécifié."}), 400

    # Vérifier si l'utilisateur existe dans la base de données
    recipient = User.query.get(recipient_id)
    print(f"Recipient Object: {recipient}")  # DEBUG: Afficher les détails de l'utilisateur

    if not recipient:
        return jsonify({"error": "Utilisateur non trouvé"}), 404

    user = {
        "id": current_user_id,
        "username": session.get('username')
    }
    return render_template('chat.html', recipient=recipient, user=user)
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
