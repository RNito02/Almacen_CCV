from sqlalchemy import Column, Integer, String
from database import Base

class Material(Base):
    __tablename__ = "material"

    numero_parte = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    tipo = Column(String)
    cantidad = Column(String)
    color = Column(String)
