from dataclasses import dataclass, field


@dataclass
class Movimiento:
    tipo: str
    importe: float


@dataclass
class CuentaBancaria:
    titular: str
    saldo: float = 0
    movimientos: list[Movimiento] = field(default_factory=list)

    def depositar(self, importe: float) -> None:
        self._validar_importe(importe)
        self.saldo += importe
        self.movimientos.append(Movimiento("Deposito", importe))

    def extraer(self, importe: float) -> bool:
        self._validar_importe(importe)
        if importe > self.saldo:
            return False

        self.saldo -= importe
        self.movimientos.append(Movimiento("Extraccion", importe))
        return True

    @staticmethod
    def _validar_importe(importe: float) -> None:
        if importe <= 0:
            raise ValueError("El importe debe ser mayor a cero.")


def main() -> None:
    cuenta = CuentaBancaria("Nicolas", 100000)
    cuenta.depositar(25000)
    cuenta.extraer(40000)

    print("=== Cuenta bancaria ===")
    print(f"Titular: {cuenta.titular}")
    print(f"Saldo: ${cuenta.saldo:.2f}")
    print("Movimientos:")

    for movimiento in cuenta.movimientos:
        print(f"- {movimiento.tipo}: ${movimiento.importe:.2f}")


if __name__ == "__main__":
    main()
