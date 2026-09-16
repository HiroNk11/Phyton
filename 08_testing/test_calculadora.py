import unittest

from calculadora import dividir, porcentaje, sumar


class CalculadoraTests(unittest.TestCase):
    def test_sumar(self) -> None:
        self.assertEqual(sumar(10, 15), 25)

    def test_dividir(self) -> None:
        self.assertEqual(dividir(20, 4), 5)

    def test_dividir_por_cero(self) -> None:
        with self.assertRaises(ValueError):
            dividir(10, 0)

    def test_porcentaje(self) -> None:
        self.assertEqual(porcentaje(1000, 15), 150)


if __name__ == "__main__":
    unittest.main()
