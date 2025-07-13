from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import models, schemas
from database import SessionLocal, engine
from typing import List
from fastapi import HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware




# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost:8080",  # Puerto por defecto donde corre Vue dev server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] para permitir todos (no recomendado en prod)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener sesión
def get_db():
    db = SessionLocal()
    print("📡 Conectado a la base de datos")  # <-- esto es útil para ver si se abre sesión
    try:
        yield db
    finally:
        db.close()

@app.post("/post_material/", response_model=schemas.MaterialOut)
def crear_material(material: schemas.MaterialBase, db: Session = Depends(get_db)):
    db_material = models.Material(
        nombre=material.nombre,
        tipo=material.tipo,
        cantidad=material.cantidad,
        color=material.color
    )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material


@app.get("/get_material/", response_model=schemas.MaterialOut)
def obtener_material(nombre: str = Query(...), db: Session = Depends(get_db)):
    material = db.query(models.Material).filter(models.Material.nombre == nombre).first()
    if material is None:
        raise HTTPException(status_code=404, detail="Material no encontrado")
    return material

@app.get("/get_all_materials/", response_model=List[schemas.MaterialOut])
def obtener_todos_los_material(db: Session = Depends(get_db)):
    material = db.query(models.Material).all()
    return material