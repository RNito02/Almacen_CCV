from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# ✅ Asegúrate de que esta línea tiene el driver postgresql
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Nito1234@localhost:5432/ziemann"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
