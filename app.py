from flask import Flask, jsonify, request
import asyncio
import os
from main import connect_to_telegram, list_groups, search_messages_in_group,save_messages_to_firebase

app = Flask(__name__)

# Crée une boucle d'événements globale
loop = asyncio.get_event_loop()

# Stocke l'état de connexion à Telegram
telegram_client_connected = False


@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

@app.route('/connect', methods=['GET'])
def connect():
    # Connexion à Telegram
    global telegram_client_connected
    if not telegram_client_connected:
        try:
            loop.run_until_complete(connect_to_telegram())
            telegram_client_connected = True
            return jsonify({"message": "Connected to Telegram"})
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"message": "Already connected to Telegram"})

@app.route('/save_messages', methods=['POST'])
def save_messages():
    """
    Enregistre les messages dans Firebase.
    Expects JSON payload with 'group_id' and 'messages'
    """
    data = request.json
    group_id = data.get('group_id')
    messages = data.get('messages')

    # Vérification des paramètres
    if not group_id or not messages:
        return jsonify({"error": "group_id and messages are required"}), 400

    try:
        # Enregistrer les messages dans Firebase
        save_result = asyncio.run(save_messages_to_firebase(group_id, messages))
        return jsonify({"message": save_result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/groups', methods=['GET'])
def groups():
    # Récupération des groupes
    try:
        if telegram_client_connected:
            groups = loop.run_until_complete(list_groups())
            return jsonify(groups)
        else:
            return jsonify({"error": "Not connected to Telegram"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/search_messages', methods=['POST'])
def search_messages():
    """
    Recherche les messages dans un groupe contenant un mot-clé spécifique.
    Expects JSON payload with 'group_id' and 'keyword'
    """
    data = request.json
    group_id = data.get('group_id')
    keyword = data.get('keyword')

    # Vérification des paramètres
    if not group_id or not keyword:
        return jsonify({"error": "group_id and keyword are required"}), 400

    # Effectuer la recherche des messages
    if telegram_client_connected:
        messages = loop.run_until_complete(search_messages_in_group(group_id, keyword))
        return jsonify({"messages": messages})
    else:
        return jsonify({"error": "Not connected to Telegram"}), 400

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
