# Usar a classe abstrata base
from automato import Automato

# Classe que representa um autômato que reconhece a linguagem L = aba* | ba*ba
class M2(Automato):
    # Construtor dessa classe
    def __init__(self):
        # Construtor da superclasse, passando o conjunto de estados e aceitação
        super().__init__([2])

    # Implementar a função f
    # L = ab*a
    def f(self, estado, simbolo):
        if estado == 0 and simbolo == 'a':
            return 1
        elif estado == 1 and simbolo == 'a':
            return 2
        elif estado == 1 and simbolo == 'b':
            return 1
    
        return 3