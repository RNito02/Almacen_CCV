from pydantic import BaseModel

class MaterialBase(BaseModel):
    nombre: str
    tipo: str
    cantidad: str
    color: str

class MaterialCreate(MaterialBase):
    pass

class MaterialOut(MaterialBase):
    numero_parte: int

    class Config:
        from_attributes = True