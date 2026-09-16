def sumar(a: float, b: float) -> float:
    return a + b


def restar(a: float, b: float) -> float:
    return a - b


def multiplicar(a: float, b: float) -> float:
    return a * b


def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("No se puede dividir por cero.")
    return a / b


def pedir_numero(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Ingrese un numero valido.")


def main() -> None:
    operaciones = {
        "1": ("Sumar", sumar),
        "2": ("Restar", restar),
        "3": ("Multiplicar", multiplicar),
        "4": ("Dividir", dividir),
    }

    print("=== Calculadora CLI ===")
    for clave, (nombre, _) in operaciones.items():
        print(f"{clave}. {nombre}")

    opcion = input("Seleccione una opcion: ")
    if opcion not in operaciones:
        print("Opcion invalida.")
        return

    primer_numero = pedir_numero("Primer numero: ")
    segundo_numero = pedir_numero("Segundo numero: ")

    try:
        nombre, operacion = operaciones[opcion]
        resultado = operacion(primer_numero, segundo_numero)
        print(f"{nombre}: {resultado:.2f}")
    except ValueError as exc:
        print(exc)


if __name__ == "__main__":
    main()
