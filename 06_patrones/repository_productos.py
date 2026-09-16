from dataclasses import dataclass


@dataclass
class Producto:
    id: int
    nombre: str
    precio: float
    stock: int


class ProductoRepository:
    def __init__(self) -> None:
        self._productos: dict[int, Producto] = {}

    def agregar(self, producto: Producto) -> None:
        self._productos[producto.id] = producto

    def obtener(self, producto_id: int) -> Producto | None:
        return self._productos.get(producto_id)

    def listar(self) -> list[Producto]:
        return list(self._productos.values())


class ProductoService:
    def __init__(self, repository: ProductoRepository) -> None:
        self.repository = repository

    def vender(self, producto_id: int, cantidad: int) -> bool:
        producto = self.repository.obtener(producto_id)
        if producto is None or cantidad <= 0 or producto.stock < cantidad:
            return False

        producto.stock -= cantidad
        return True


def main() -> None:
    repository = ProductoRepository()
    repository.agregar(Producto(1, "Notebook", 1200000, 5))
    repository.agregar(Producto(2, "Monitor", 260000, 10))

    service = ProductoService(repository)
    service.vender(1, 2)

    print("=== Repository - Productos ===")
    for producto in repository.listar():
        print(f"{producto.id}. {producto.nombre} | Stock: {producto.stock}")


if __name__ == "__main__":
    main()
