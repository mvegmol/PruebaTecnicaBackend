from sqlmodel import SQLModel, Field, Relationship

class Base(SQLModel):
    pass
# Entidad Cliente
class Client(SQLModel, table=True):
    __tablename__ = "clients"

    id: int = Field(default=None, primary_key=True, index=True)
    dni: str = Field(unique=True, index=True)
    name: str = Field(index=True)
    email: str = Field(unique=True, index=True)
    requested_amount: float

    # Relación con la tabla de simulaciones
    simulations: list["Simulation"] = Relationship(back_populates="client")

# Entidad Simulación
class Simulation(SQLModel, table=True):
    __tablename__ = "simulations"

    id: int = Field(default=None, primary_key=True, index=True)
    client_id: int = Field(foreign_key="clients.id")
    tae: float
    term_years: int
    monthly_payment: float
    total_payment: float

    client: Client = Relationship(back_populates="simulations")
