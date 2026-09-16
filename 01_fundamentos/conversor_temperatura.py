def celsius_a_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def fahrenheit_a_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def main() -> None:
    print("=== Conversor de temperatura ===")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")

    opcion = input("Seleccione una opcion: ")
    valor = float(input("Temperatura: "))

    if opcion == "1":
        print(f"Resultado: {celsius_a_fahrenheit(valor):.2f} F")
    elif opcion == "2":
        print(f"Resultado: {fahrenheit_a_celsius(valor):.2f} C")
    else:
        print("Opcion invalida.")


if __name__ == "__main__":
    main()
