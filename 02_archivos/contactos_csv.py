import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Contacto:
    nombre: str
    email: str
    telefono: str


class ContactoRepository:
    def __init__(self, archivo: Path) -> None:
        self.archivo = archivo
        self.archivo.parent.mkdir(parents=True, exist_ok=True)

    def guardar(self, contactos: list[Contacto]) -> None:
        with self.archivo.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["nombre", "email", "telefono"])
            writer.writeheader()
            for contacto in contactos:
                writer.writerow(contacto.__dict__)

    def leer(self) -> list[Contacto]:
        if not self.archivo.exists():
            return []

        with self.archivo.open("r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return [Contacto(**row) for row in reader]


def main() -> None:
    repository = ContactoRepository(Path("data/contactos.csv"))
    contactos = [
        Contacto("Ana Gomez", "ana@email.com", "1111-2222"),
        Contacto("Bruno Diaz", "bruno@email.com", "3333-4444"),
        Contacto("Carla Ruiz", "carla@email.com", "5555-6666"),
    ]

    repository.guardar(contactos)

    print("=== Contactos CSV ===")
    for contacto in repository.leer():
        print(f"{contacto.nombre} | {contacto.email} | {contacto.telefono}")


if __name__ == "__main__":
    main()
