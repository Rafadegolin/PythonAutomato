# Para implementar uma classe abstrata
from abc import abstractmethod, ABC

# Criar uma classe abstrata
class Automato(ABC):
    # definir construtor em python
    def __init__(self, aceitacao):
        # Definir os atributos da classe
        self.estado = 0
        self.aceitacao = aceitacao

    # Definição de um método abstrato em Python
    @abstractmethod
    def f(self, estado, simbolo):
        pass

    # Recebe a fita e muda de estado até o final da palavra
    def aceita(self, fita):
        # Inicializa o estado inicial
        self.estado = 0
        # Percorrendo a fita e mudando de estado
        for simbolo in fita:
            self.estado = self.f(self.estado, simbolo)
        # Ao terminar de ler a fita
        return self.estado in self.aceitacao