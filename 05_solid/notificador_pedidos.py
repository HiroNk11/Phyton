from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class Pedido:
    numero: int
    cliente: str
    total: float


class Notificador(ABC):
    @abstractmethod
    def enviar(self, pedido: Pedido) -> None:
        raise NotImplementedError


class EmailNotificador(Notificador):
    def enviar(self, pedido: Pedido) -> None:
        print(f"[EMAIL] Pedido {pedido.numero} confirmado para {pedido.cliente}.")


class SmsNotificador(Notificador):
    def enviar(self, pedido: Pedido) -> None:
        print(f"[SMS] Pedido {pedido.numero} por ${pedido.total:.2f}.")


class PedidoService:
    def __init__(self, notificadores: list[Notificador]) -> None:
        self.notificadores = notificadores

    def confirmar(self, pedido: Pedido) -> None:
        print(f"Confirmando pedido {pedido.numero}.")
        for notificador in self.notificadores:
            notificador.enviar(pedido)


def main() -> None:
    pedido = Pedido(1001, "Ana Gomez", 150000)
    service = PedidoService([EmailNotificador(), SmsNotificador()])

    print("=== SOLID - Notificador de pedidos ===")
    service.confirmar(pedido)


if __name__ == "__main__":
    main()
