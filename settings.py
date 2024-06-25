import os, sys
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta


DATABASE_URL = 'postgresql://dbAuto:dbAutoFarvater@db_auto/postgres'
PORT  =  8800

Base:DeclarativeMeta = declarative_base()
engine = create_engine(DATABASE_URL)
SessionLocal = sqlalchemy.orm.sessionmaker(autocommit=False,autoflush=False,bind=engine)


