from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session, select
from database import SessionLocal, engine
from models import Base
from schemas import ClientCreate, SimulationCreate, SimulationResponse
from crud import create_client, get_client_by_dni, create_simulation
from utils import validate_dni

# Crea todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/clients/", response_model=ClientCreate)
def create_new_client(client: ClientCreate, db: Session = Depends(get_db)):
    if not validate_dni(client.dni):
        raise HTTPException(status_code=400, detail="Invalid DNI")
    return create_client(db, client)

@app.get("/clients/{dni}", response_model=ClientCreate)
def read_client(dni: str, db: Session = Depends(get_db)):
    client = get_client_by_dni(db, dni)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@app.post("/clients/{dni}/simulate", response_model=SimulationResponse)
def simulate_mortgage(dni: str, simulation: SimulationCreate, db: Session = Depends(get_db)):
    client = get_client_by_dni(db, dni)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return create_simulation(db, client.id, simulation)
