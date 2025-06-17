# Default global variables definition - Possible to also store it in the main database or in a separate database
satisfaction_pro_std = 0
satisfaction_couple_std = 0
stamina_std = 0
session_couple_std = False # True = yes, False = no
session_loisir_std = False # True = yes, False = no
session_sport_std = "None" # None, indoor_short, indoor_long, outdoor_short, outdoor_long, dedicated_day
german_study_std = "None" # None, Anki, Anki+
speaking_time_std = 0

# Pour les variables multichoix, liste des choix
liste_german_study = ["None","Anki","Anki+New","Anki+Lesson"]
liste_session_sport = ["None", "indoor_short", "indoor_long", "outdoor_short", "outdoor_long", "dedicated_day"]

from models import Life, Session
from datetime import datetime

def ajouter_tache():
    # Input manuel des informations
    satisfaction_pro = int(input("Description de la satisfaction_pro /10 : "))
    satisfaction_couple = int(input("Description de la satisfaction_couple /10 : "))
    stamina = int(input("Description de la stamina /10 : "))
    session_couple = int(input("Description de la session_couple (1/0): "))
    session_loisir = int(input("Description de la session_loisir (1/0): "))
    # session_sport = str(input("Description de la session_sport (Oui/Non): "))
    session_sport = get_from_list(liste_session_sport)
    # german_study = str(input("Description de la german_study (Oui/Non) : "))
    german_study = get_from_list(liste_german_study)
    speaking_time = int(input("Description de la speaking_time (min): "))

    # Real date and hour implemented
    now = datetime.now()
    date = now.strftime("%d%m%Y")
    hour = now.strftime("%H%M")

    # Creating the "Session" object
    session = Session()

    # Création d'un objet de classe Life qui recupère les infos
    input_data = Life(date = date, hour = hour,satisfaction_pro=satisfaction_pro, satisfaction_couple=satisfaction_couple, stamina=stamina, session_couple=session_couple,session_loisir=session_loisir, session_sport=session_sport, german_study=german_study, speaking_time=speaking_time)
    
    # Add and commit
    session.add(input_data)
    session.commit()
    print("✅ Tâche ajoutée !")

def lister_taches():
    session = Session()

    #  database query with SQLAlchemy to get all the lines of the Life table
    input_data = session.query(Life).all()
    print("\n📋 Liste des entrées :")
    for t in input_data:
        print(f"{t.id}. {t.date} à {t.hour}h - pro: {t.satisfaction_pro} / couple: {t.satisfaction_couple} / stamina: {t.stamina}")
    session.close()

def supprimer_tache():
    id_input_data = input("ID de l’entrée à supprimer : ")
    session = Session()

    #  Requête à la base de données avec SQLAlchemy pour récupérer la ligne de la table Life avec un certain ID
    input_data = session.query(Life).get(int(id_input_data))
    if input_data:
        session.delete(input_data)
        session.commit()
        print("🗑️ Entrée supprimée.")
    else:
        print("❗Entrée introuvable.")
    session.close()

def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Ajouter une entrée")
        print("2. Lister les entrée")
        print("3. Supprimer une tâche")
        print("4. Quitter")
        choix = input("Choix : ")

        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            lister_taches()
        elif choix == "3":
            supprimer_tache()
        elif choix == "4":
            break
        else:
            print("⛔ Choix invalide.")


# Temporary, to test the implementation of multi select choices
def get_session_sport():
    print("\n 0 = None, 1 = indoor_short, 2 = indoor_long, 3 = outdoor_short, 4 = outdoor_long, 5 = dedicated_day")
    input_session_sport = int(input("Choice : "))
    if input_session_sport == 1:
        return "None"
    elif input_session_sport == 2:
        return "indoor_short"
    elif input_session_sport == 3:
        return "outdoor_short"
    elif input_session_sport == 4:
        return "outdoor_long"
    elif input_session_sport == 5:
        return "dedicated_day"
    else:
        return "None"

def get_from_list(options):
    print(", ".join([f'{i} = "{val}"' for i, val in enumerate(options)]))
    input_from_list = int(input("Choice : "))
    return options[input_from_list]

if __name__ == "__main__":
    menu()