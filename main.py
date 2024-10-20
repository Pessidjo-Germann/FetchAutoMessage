from telethon import TelegramClient

from telethon.tl.types import InputPeerChannel
from telethon.errors import ChannelInvalidError
from firebase_admin import  credentials, firestore, initialize_app


import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

 
db=firestore.client()
# Remplacez par vos propres valeurs
api_id = '27896793'
api_hash = 'dcbc58890bf1e032ce046fba5f90d943'
phone_number = '+237694357305'

client = TelegramClient('session_name', api_id, api_hash)


db = firestore.client()

async def save_messages_to_firebase(group_id, messages):
    """
    Enregistre les messages dans Firestore.
    
    :param group_id: ID ou nom du groupe.
    :param messages: Liste des messages à enregistrer.
    """
    try:
        # Créer une collection pour le groupe s'il n'existe pas
        group_ref = db.collection('groups').document(group_id)

        # Enregistrer chaque message
        for message in messages:
            message_ref = group_ref.collection('messages').document(str(message['message_id']))
            message_ref.set({
                'text': message['text'],
                'date': message['date'],
                'message_id': message['message_id'],
            })

        return "Messages enregistrés avec succès."
    except Exception as e:
        return f"Erreur lors de l'enregistrement des messages: {str(e)}"

async def search_messages_in_group(group_id, keyword):
    """
    Recherche les messages contenant un mot-clé dans un groupe.
    :param group_id: ID du groupe où chercher
    :param keyword: Mot-clé à rechercher
    :return: Liste des messages contenant le mot-clé
    """
    messages = []
    try:
        # Récupérer le groupe par son ID
        #group = await client.get_entity(InputPeerChannel(group_id, 0))
        group = await client.get_entity(group_id)  # Remplace 'group_id' par l'identifiant ou nom exact du groupe

        # Rechercher les messages dans le groupe contenant le mot-clé
        async for message in client.iter_messages(group, search=keyword):
            if message.text:
                messages.append({
                    'id': message.id,
                    'text': message.text,
                    'date': message.date.strftime('%Y-%m-%d %H:%M:%S'),
                    'sender_id': message.sender_id
                })
    except ChannelInvalidError:
        print("Invalid group/channel ID")
    
    return messages



async def connect_to_telegram():
    # Connexion à Telegram
    await client.start(phone_number)
    print(f"Connected to {client}")


async def list_groups():
    # Lister les groupes auxquels vous appartenez
    group=[]
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            print(f"Group: {dialog.name} (ID: {dialog.id})")
            group.append({'name':dialog.name, 'id':dialog.id})
    return group

# # Boucle d'exécution principale
# async def main():
#     await connect_to_telegram()
#     await list_groups()

# # Démarrer le client et exécuter le script
# client.loop.run_until_complete(main())
