from sqlmodel import Session
from models import Client, Simulation
from schemas import ClientCreate, SimulationCreate
from utils import calculate_mortgage

# Crear cliente
def create_client(db: Session, client: ClientCreate):
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

# Obtener cliente por DNI
def get_client_by_dni(db: Session, dni: str):
    return db.query(Client).filter(Client.dni == dni).first()

# Crear simulación
def create_simulation(db: Session, client_id: int, simulation: SimulationCreate):
    # Obtener los datos del cliente
    client = db.query(Client).get(client_id)
    
    if client is None:
        raise ValueError("Client not found")

    # Realizar los cálculos de la hipoteca
    monthly_payment, total_payment = calculate_mortgage(
        capital=client.requested_amount,
        tae=simulation.tae,
        years=simulation.term_years
    )

    # Crear la simulación
    db_simulation = Simulation(
        client_id=client_id,
        tae=simulation.tae,
        term_years=simulation.term_years,
        monthly_payment=monthly_payment,
        total_payment=total_payment
    )
    
    # Guardar la simulación en la base de datos
    db.add(db_simulation)
    db.commit()
    db.refresh(db_simulation)
    
    return db_simulation
