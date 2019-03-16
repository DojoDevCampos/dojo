import random

class Jogo_detetive():

    def definir_morte(self, quem, arma, onde):
        self.quem = quem
        self.arma = arma
        self.onde = onde

    def avalia_hipotese(self, quem, arma, onde):
        resultado = []
        if onde != self.onde:
            resultado.append(1)
        if arma != self.arma:
            resultado.append(2)
        if quem != self.quem:
            resultado.append(3)

        tam_resultados = len(resultado)
        if tam_resultados == 0:
            return 0
        if tam_resultados == 1:
            return resultado[0]

        sorteio = random.randint(0,tam_resultados -1)
        return resultado[sorteio]

    def iniciacao(self):
        pass