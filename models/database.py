from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    "postgresql://postgres:postgres@0.0.0.0:5432/postgres", echo=True
)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
