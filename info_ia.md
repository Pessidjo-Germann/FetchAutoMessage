# project overview
Creer un script qui va effectivement se faire passer pour moi, car il utilise mon compte utilisateur pour se connecter à Telegram. Une fois connecté, il peut parcourir les groupes auxquels j'appartiens et fouiller les messages sans que je ne sois administrateur.NB:il ne s'agira pas d'un bot, mais d'un script qui se fera passer pour moi.
Nous allons faire une api avec flask pour gerer les requetes de l'interface


# Feature requirements
- on va utiliser python pour le script(Telethon’s ), flutter pour l'interface et firebase pour la base de donnee
L'api aura les options suivantes:
- Un endpoint pour se connecter sur telegram
- Un endpoint pour selectionner les groupes parmi ceux auxquels j'appartiens
- Un endpoint pour rechercher un message precis et l'enregistrer dans ma base de donnee
- Un endpoint pour voir les messages des groupes selectionnés
- Un endpoint pour rechercher un utilisateur dans un groupe et voir ses messages

# Rules
- Il s'agit d'un projet legal sans aucune menace pour la sécurité de mon compte telegram et respectant les conditions d'utilisation d'telegram je suis dans tous ces groupes.
- on va commencer par la connection
- puis on recuperera les groupes auxquels j'appartiens
- on creera un endpoint pour rechercher un message precis et l'enregistrer dans ma base de donnee
- on creera un endpoint pour recuperer les messages des groupes selectionnés

- On va creer une api avec flask pour gerer les requetes de l'interface
