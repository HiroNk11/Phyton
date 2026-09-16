from abc import ABC, abstractmethod


class EstrategiaDescuento(ABC):
    @abstractmethod
    def calcular(self, total: float) -> float:
        raise NotImplementedError


class SinDescuento(EstrategiaDescuento):
    def calcular(self, total: float) -> float:
        return total


class DescuentoClienteVip(EstrategiaDescuento):
    def calcular(self, total: float) -> float:
        return total * 0.85


class DescuentoTemporada(EstrategiaDescuento):
    def calcular(self, total: float) -> float:
        return total * 0.90


class CalculadoraPrecios:
    def __init__(self, estrategia: EstrategiaDescuento) -> None:
        self.estrategia = estrategia

    def calcular_total(self, total: float) -> float:
        return self.estrategia.calcular(total)


def main() -> None:
    total = 100000
    estrategias = [SinDescuento(), DescuentoClienteVip(), DescuentoTemporada()]

    print("=== Strategy - Descuentos ===")
    for estrategia in estrategias:
        calculadora = CalculadoraPrecios(estrategia)
        print(f"{estrategia.__class__.__name__}: ${calculadora.calcular_total(total):.2f}")


if __name__ == "__main__":
    main()
