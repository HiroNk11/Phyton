from collections import defaultdict
from dataclasses import dataclass


@dataclass(frozen=True)
class Venta:
    vendedor: str
    region: str
    producto: str
    cantidad: int
    precio_unitario: float

    @property
    def total(self) -> float:
        return self.cantidad * self.precio_unitario


def total_por_vendedor(ventas: list[Venta]) -> dict[str, float]:
    resultado: dict[str, float] = defaultdict(float)
    for venta in ventas:
        resultado[venta.vendedor] += venta.total
    return dict(resultado)


def producto_mas_vendido(ventas: list[Venta]) -> str:
    cantidades: dict[str, int] = defaultdict(int)
    for venta in ventas:
        cantidades[venta.producto] += venta.cantidad
    return max(cantidades, key=cantidades.get)


def ventas_mayores_a(ventas: list[Venta], minimo: float) -> list[Venta]:
    return [venta for venta in ventas if venta.total >= minimo]


def crear_ventas() -> list[Venta]:
    return [
        Venta("Ana", "Norte", "Notebook", 1, 1200000),
        Venta("Bruno", "Sur", "Monitor", 2, 260000),
        Venta("Ana", "Norte", "Teclado", 4, 95000),
        Venta("Carla", "Centro", "Mouse", 5, 42000),
        Venta("Bruno", "Sur", "Notebook", 1, 1180000),
    ]


def main() -> None:
    ventas = crear_ventas()

    print("=== Reportes de ventas ===")
    print("Total por vendedor:")
    for vendedor, total in sorted(total_por_vendedor(ventas).items()):
        print(f"- {vendedor}: ${total:.2f}")

    print()
    print(f"Producto mas vendido: {producto_mas_vendido(ventas)}")

    print()
    print("Ventas mayores a $500000:")
    for venta in ventas_mayores_a(ventas, 500000):
        print(f"- {venta.vendedor} | {venta.producto} | ${venta.total:.2f}")


if __name__ == "__main__":
    main()
