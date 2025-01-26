import re
from math import pow

#Validación del dni
def validate_dni(dni: str) -> bool:
    dni_pattern = r'^\d{8}[A-Z]$'
    if not re.match(dni_pattern, dni):
        return False

    letters = "TRWAGMYFPDXBNJZSQVHLCKE"
    number = int(dni[:-1])
    expected_letter = letters[number % 23]
    return dni[-1] == expected_letter


def calculate_mortgage(capital: float, tae: float, years: int) -> tuple[float, float]:
    if tae == 0:
        # Si la tasa es cero, simplemente dividimos el capital entre el número de meses
        n = years * 12
        monthly_payment = capital / n
        total_payment = monthly_payment * n
    else:
        i = (tae / 100) / 12  # Tasa de interés mensual
        n = years * 12  # Número de pagos mensuales
        monthly_payment = capital * i / (1 - pow(1 + i, -n))
        total_payment = monthly_payment * n
    
    return monthly_payment, total_payment

