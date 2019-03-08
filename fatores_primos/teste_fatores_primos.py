import unittest
from fatores_primos import Fatores_primos

class Test_fatores_primos(unittest.TestCase):
    def setUp(self):
        self.fatores_primos = Fatores_primos()

    def test_validade_negativo(self):
        self.assertFalse(self.fatores_primos.verificar_validade(-1))

    def test_validade_float(self):
        self.assertFalse(self.fatores_primos.verificar_validade(1.5))

    def test_validade_float_negativo(self):
        self.assertFalse(self.fatores_primos.verificar_validade(-1.5))

    def test_validade_numero_valido(self):
        self.assertTrue(self.fatores_primos.verificar_validade(6))

    def test_validade_zero(self):
        self.assertFalse(self.fatores_primos.verificar_validade(0))

    def test_validade_um(self):
        self.assertFalse(self.fatores_primos.verificar_validade(1))

    def test_validade_tipo(self):
        self.assertFalse(self.fatores_primos.verificar_validade('4'))
    
    def test_validade_boolean(self):
        self.assertFalse(self.fatores_primos.verificar_validade(True))
    
    def test_listar_menores_que_n(self):
        self.assertEqual([0, 1, 2, 3, 4], self.fatores_primos.listar_naturais_menores(5))
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], self.fatores_primos.listar_naturais_menores(10))

    def test_validade_listar_menores_que_n(self):
        with self.assertRaises(TypeError):
            self.fatores_primos.listar_naturais_menores('-11')
        
        # try: 
        #     self.fatores_primos.listar_naturais_menores('-11')
        # except TypeError:
        #     pass


if __name__ == '__main__':
    unittest.main(verbosity=3)