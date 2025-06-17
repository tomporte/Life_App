# Life_App
Creation of a Life input data app

# Structure of the App
main.py
models.py
database.db

Spec App

Stockage Data :
Permettre le stockage d’entrées journalières sur des critères prédéfinis Ces critères pourront être modifiés par la suite dans de nouvelles versions Les critères doivent être de type oui/non ou graduels.
Les critères doivent être anonymises pour éviter la fuite de données sensibles (affichage en clair par contre)

Data : 
date (en automatique)
hour (en automatique)
satisfaction_pro (sur 10)
satisfaction_couple (sur 10)
stamina (sur 10)
session_couple (Oui/Non)
session_loisir (Oui/Non)
session_sport (None, indoor_short, indoor_long, outdoor_short, outdoor_long, dedicated_day)
german_study (None, Anki, Anki+New, Anki+Lesson)
speaking_time (en min)

Interface :
Il doit être possible de passer de l’interface Sortie à l’interface Entrée par un bouton largement visible.
Sortie :
L’interface doit afficher les résultats sur une page web minimaliste L’utilisateur doit pouvoir sélectionner différentes vues (temporelles, critère à afficher, corrélation, …) La selection de l’affichage doit se faire avec des menus déroulants et boutons simples

Entrée :
L’interface doit proposer sur une seule page sans menu déroulant, l’intégralité des entrées utilisateur à completer avec des tick boxes ou sliders.
Il doit exister un bouton unique pour valider les entrées d’un seul tenant, cela doit réinitialiser les entrées par défaut.
En cas d’entrée répétée un meme jour, la deuxième entrée efface la premiere.




LDEV :
Le tout sur github, créer :
- un fichier models.py avec l’initialisation de la base, le lien avec le fichier .db, le chargement de la base dans le fichier avec les colonnes associées, la création de la session d’accès.
Outils à utiliser : Git, Python, SQLAlchemy
- un fichier main.py avec le gros du code applicatif : avec toute la définition des scripts, ainsi que l’interface ou en tout cas le mode de fonctionnement (menu)
Outils à utiliser : Git, Python, SQLAlchemy
- La base de donnée .db sera créé automatiquement mais il est utile d’avoir DB Browser Lite 
Outils à utiliser : Git, Python, SQLAlchemy, DB Browser Lite
Développement de la BDD pour connaitre les entrées Développement d’un outil local de visualisation associé (python) 
----- A ce stade, une V0.1 peut être ‘deployée’ en local car on doit avoir un code qui vient interagir avec une BDD et qui peut l’incrémenter / la décrémenter
Développement d’un outil local d’input associé (python) 
----- Une V0.2 pourra être créée pour ajouter les fonctionnalités de la SPEC en terme d’input (cf ci-dessus)
Développement de l’interface streamlit locale 
----- Une V0.3 pourra être créée pour ajouter l’interface web associée au code Python en local.
Hébergement sur Heroku et déploiement via Github Push (erase data)
----- Une V1 pourra alors être déployée avec un usage en ligne
Les prochaines améliorations comprendront : 
Refonte de la BDD pour anonymiser les données
Création d’une interface de visualisation et de traitement


