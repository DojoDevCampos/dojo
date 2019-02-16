import unittest
from numerosRomanos import NumerosRomanos

class testNumeroRomano(unittest.TestCase):
    def setUp(self):
        self.numero_romano = NumerosRomanos()
    
    def testdecimal_romano(self):
        self.assertEqual(self.numero_romano.decimal_romano(1),
                          'I', 'I falhou')
        
        self.assertEqual(self.numero_romano.decimal_romano(3), 
                         'III', 'III falhou')
        
        self.assertEqual(self.numero_romano.decimal_romano(5),
                          'V', 'V falhou')

        self.assertEqual(self.numero_romano.decimal_romano(50),
                          'L', 'L falhou')
        
        self.assertEqual(self.numero_romano.decimal_romano(2),
                          'II', 'II falhou')
        