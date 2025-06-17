# Import des composants SQLAlchemy pour définir une base de données
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

# Déclare une classe de base pour tous nos modèles (tables)
Base = declarative_base()

# Définition du modèle "Tache" : correspond à une table en base de données
class Life(Base):
    __tablename__ = 'Life'  # Nom de la table dans la base SQLite

    # Définition des colonnes
    id = Column(Integer, primary_key=True)          # Clé primaire (identifiant unique auto-incrémenté)
    date = Column(Integer, nullable=False)  
    hour = Column(Integer, nullable=False)  
    satisfaction_pro = Column(Integer, nullable=True)  
    satisfaction_couple = Column(Integer, nullable=True)
    stamina = Column(Integer, nullable=True)
    session_couple = Column(Integer, nullable=True)
    session_loisir = Column(Integer, nullable=True)
    session_sport = Column(String, nullable=True)
    german_study = Column(String, nullable=True)
    speaking_time = Column(Integer, nullable=True)

# Création de l'"engine" = le lien vers la base SQLite (fichier .db)
engine = create_engine('sqlite:///database.db')

# Création des tables dans la base, selon les modèles définis (ici, Tache)
Base.metadata.create_all(engine)

# Création de la "Session" = une connexion à la base qu'on utilisera pour faire des requêtes
Session = sessionmaker(bind=engine)