import unittest
from numerosRomanos import NumerosRomanos

class testNumeroRomano(unittest.TestCase):
    def setUp(self):
        self.numero_romano = NumerosRomanos()

    def testdecimal_I(self):
        self.assertEqual('I', self.numero_romano.decimal_romano(1),
                         'I falhou')
        self.assertEqual('III', self.numero_romano.decimal_romano(3),
                         'III falhou')
        self.assertEqual('II', self.numero_romano.decimal_romano(2),
                         'II falhou')
    def testdecimal_IV(self):
        self.assertEqual('IV', self.numero_romano.decimal_romano(4),
                         'IV falhou')
    def testdecimal_V(self):
        self.assertEqual('V', self.numero_romano.decimal_romano(5),
                         'V falhou')
    def testdecimal_IX(self):
        self.assertEqual('IX', self.numero_romano.decimal_romano(9),
                         'IX falhou')
    def testdecimal_L(self):
        self.assertEqual('L', self.numero_romano.decimal_romano(50),
                          'L falhou')

    def testdecimal_XIX(self):
        self.assertEqual('XIX', self.numero_romano.decimal_romano(19),
                         'XIX falhou')

    def testdecimal_XL(self):
        self.assertEqual('XL', self.numero_romano.decimal_romano(40),
                         'XL falhou')



#  para quem roda o python pelo terminal inclua a linha 39  e 40 e tenha o unittest instalado
# if __name__ == '__main__':
#     unittest.main()
