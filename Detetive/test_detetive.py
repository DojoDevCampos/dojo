import unittest
from detetive import Jogo_detetive

class Test_jogo_detetive(unittest.TestCase):
    def setUp(self):
        self.detetive = Jogo_detetive()
        self.detetive.definir_morte(2, 3, 4)

    def test_definicao_morte(self):
        self.assertEqual(0, self.detetive.avalia_hipotese(2, 3, 4))
        self.assertNotEqual(0, self.detetive.avalia_hipotese(2, 3, 5))

    def test_1_erro (self):
        self.assertEqual(1, self.detetive.avalia_hipotese(1, 3, 4))
        self.assertEqual(2, self.detetive.avalia_hipotese(2, 2, 4))
        self.assertEqual(3, self.detetive.avalia_hipotese(2, 3, 5))

    def test_2_erro (self):
        self.assertNotIn(self.detetive.avalia_hipotese(2, 3, 4), [1, 2, 3])
        self.assertIn(self.detetive.avalia_hipotese(3, 4, 4), [1, 2])
        self.assertIn(self.detetive.avalia_hipotese(2, 4, 5), [2, 3])
        self.assertIn(self.detetive.avalia_hipotese(3, 3, 5), [1, 3])

    def test_3_erro (self):
        self.assertNotIn(self.detetive.avalia_hipotese(2, 3, 4), [1, 2, 3])
        self.assertIn(self.detetive.avalia_hipotese(1, 2, 3), [1, 2, 3])

