from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL de connexion à la base de données PostgreSQL
URL_DATABASE = 'postgresql://postgres:0000@localhost:5432/quizApp'

# Créer l'engine SQLAlchemy
engine = create_engine(URL_DATABASE)

# Créer une session locale pour les requêtes
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Créer une classe de base pour les modèles
Base = declarative_base()
