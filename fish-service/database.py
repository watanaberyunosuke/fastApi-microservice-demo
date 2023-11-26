"""
    DB Connection Utility File
"""
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy: used to handle database actions
load_dotenv()
db_username = os.environ.get('DATABASE_USERNAME')
db_password = os.environ.get('DATABASE_PASSWORD')

engine = create_engine(f"postgresql://{db_username}:{db_password}@localhost/dwh")
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
