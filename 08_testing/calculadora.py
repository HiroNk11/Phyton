def sumar(a: float, b: float) -> float:
    return a + b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b


def porcentaje(total: float, porcentaje_valor: float) -> float:
    if porcentaje_valor < 0:
        raise ValueError("El porcentaje no puede ser negativo.")
    return total * porcentaje_valor / 100
