from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base

engine = create_engine("sqlite:///games.db", echo=True)
Session = sessionmaker(bind=engine)

def create_db():
    Base.metadata.create_all(bind=engine)
