import unittest
from observer_observed import Observer, Observed

class Test_Observer_obseved(unittest.TestCase):
    def setUp(self):
        self.observed = Observed()
        self.observer = Observer(self.observed)
        # self.observed.register(self.observer)

    def test_registrar_observador(self):
        self.assertTrue(self.observed.register(self.observer), 'Não conseguiu registrar!')
        self.assertTrue(self.observed.isObserver(self.observer))

    def test_registro_nao_observador(self):
        dummy2 = Observed()
        dummy = Observer(dummy2)

        self.assertFalse(self.observed.isObserver(dummy))


    def test_obter_dados(self):
        self.observed.setDados(10)
        self.assertEqual(10, self.observed.getDados(), 'Dados errados!')


    def test_apagar_observador(self):
        # inicialização

        # exercitar o comportamento
        retorno = self.observed.unregister(self.observer)

        # avaliação da expectativa
        self.assertTrue(retorno, "Deveria funcionar porque foi registrado")

        retorno = self.observed.unregister(self.observer)
        self.assertFalse(retorno, "Não deveria existir porque já foi removido")

        # falhar porque não estava registrado
        dummy2 = Observed()
        dummy = Observer(dummy2)
        retorno = self.observed.unregister(dummy)
        self.assertFalse(retorno, "Deveria falhar porque não foi registrado")

    def test_observador_deve_ser_notificado(self):
        #inicialização
        ob1 = Observer(self.observed)
        ob2 = Observer(self.observed)

        #Avaliação de expectativas
        self.assertFalse(ob1.isNotified())
        self.assertFalse(ob2.isNotified())

        self.observed.setDados(10)
        self.assertTrue(ob1.isNotified())
        self.assertTrue(ob2.isNotified())

        ob1.update()
        self.assertFalse(ob1.isNotified())
        ob2.update()
        self.assertFalse(ob2.isNotified())
