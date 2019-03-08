'''
Métodos a serem implementados:
    verificar_validade(n)
    listar_naturais_menores(n)
    verificar_primo(x)
    filtrar_primos(n)
    filtrar_divisores(x, n)
    retornar_fatores_primos(n)
'''
class Fatores_primos:
    def verificar_validade(self, numero):
        if type(numero) != int:
            return False
        if numero <= 1:
            return False
        return True
    
    def listar_naturais_menores(self, numero):
        if self.verificar_validade(numero) == False:
            raise TypeError('Tipo invalido, argumento invalido,invalido!')
            
        lista_menores_que_n = []
        for menor in range(numero):
            lista_menores_que_n.append(menor)
        return lista_menores_que_n