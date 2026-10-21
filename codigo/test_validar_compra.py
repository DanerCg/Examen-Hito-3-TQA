"""Casos de caja blanca CB-01 a CB-05 (ver docs/analisis_caja_blanca.md).

Ejecutar desde la carpeta codigo/:   python -m unittest -v
"""
import unittest
from validar_compra import validar_compra


class TestValidarCompra(unittest.TestCase):
    def test_cb01_edad_menor(self):
        # D1 = verdadero
        self.assertEqual(validar_compra(17, True, 100, 50), "Compra no permitida: edad")

    def test_cb02_cuenta_inactiva(self):
        # D1 = falso, D2 = verdadero
        self.assertEqual(validar_compra(25, False, 100, 50), "Compra no permitida: cuenta")

    def test_cb03_compra_aprobada(self):
        # D1 = falso, D2 = falso, D3 = verdadero (C3 y C4 verdaderas)
        self.assertEqual(validar_compra(30, True, 100, 50), "Compra aprobada")

    def test_cb04_saldo_insuficiente(self):
        # D3 = falso (C3 falsa): ajuste necesario para cobertura de decisiones
        self.assertEqual(validar_compra(30, True, 20, 50), "Compra rechazada")

    def test_cb05_monto_cero(self):
        # C3 verdadera y C4 falsa: necesario para cobertura de condiciones
        self.assertEqual(validar_compra(30, True, 100, 0), "Compra rechazada")


if __name__ == "__main__":
    unittest.main()
