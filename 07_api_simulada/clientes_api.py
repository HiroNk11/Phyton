from dataclasses import dataclass


@dataclass(frozen=True)
class Cliente:
    id: int
    nombre: str
    activo: bool


class ClientesApiClient:
    def obtener_clientes(self) -> list[dict]:
        return [
            {"id": 1, "nombre": "Ana Gomez", "activo": True},
            {"id": 2, "nombre": "Bruno Diaz", "activo": False},
            {"id": 3, "nombre": "Carla Ruiz", "activo": True},
        ]


class ClienteService:
    def __init__(self, api_client: ClientesApiClient) -> None:
        self.api_client = api_client

    def listar_activos(self) -> list[Cliente]:
        clientes = [Cliente(**item) for item in self.api_client.obtener_clientes()]
        return [cliente for cliente in clientes if cliente.activo]


def main() -> None:
    service = ClienteService(ClientesApiClient())

    print("=== API simulada - Clientes activos ===")
    for cliente in service.listar_activos():
        print(f"{cliente.id}. {cliente.nombre}")


if __name__ == "__main__":
    main()
