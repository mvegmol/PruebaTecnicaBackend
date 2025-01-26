from pydantic import BaseModel, EmailStr

class ClientCreate(BaseModel):
    name: str
    dni: str
    email: EmailStr
    requested_amount: float


class SimulationCreate(BaseModel):
    tae: float
    term_years: int


class SimulationResponse(BaseModel):
    monthly_payment: float
    total_payment: float

    class Config:
        from_attributes  = True
