class Observer:
    notificado = False
    observado = None

    def __init__(self, ob):
        self.notificado = False
        self.observado = ob
        self.observado.register(self)

    def isNotified(self):
        return self.notificado

    def update(self):
        self.observado.getDados()
        self.notificado = False

    def notify(self, observado):
        self.notificado = True

class Observed:
    observadores = []
    dado = 0

    def __init__(self):
        self.observadores = []
        self.dado = 0

    def register(self, elemento):
        self.observadores.append(elemento)
        return True

    def isObserver(self, elemento):
        return (elemento in self.observadores)

    def setDados(self, valor):
        self.dado = valor
        self.notify()

    def getDados(self):
        return self.dado

    def unregister(self, elemento):
        if self.isObserver(elemento):
            self.observadores.remove(elemento)
            return True
        return False

    def notify(self):
        for ob in self.observadores:
            ob.notify(self)

