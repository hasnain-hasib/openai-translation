import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')



SQLALCHEMY_DATABASE_URL =os. getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker (autocomit= False, autoflush=False, bind= engine)

def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally :
        db.close
        
