Puis je vais faire une interface graphique avec flutter pour pouvoir selectionner les groupes,effectuer les recherches et voir les messages.

L'interface aura les options suivantes:
- Une page pour  se connecter sur telegram
- selectionner telegram dans les options de connexion (desactive pour l'instant)
- selectionner les groupes parmi ceux auxquels j'appartiens
- me permettre de rechercher un message precis et l'enregistrer dans ma base de donnee
- voir les messages des groupes selectionnés
- rechercher un utilisateur dans un groupe et voir ses messages


# Rules
- On va commencer par creer un script qui va se connecter a telegram et recuperer les messages
- On va creer une api avec flask pour gerer les requetes de l'interface
- On va creer une interface graphique avec flutter