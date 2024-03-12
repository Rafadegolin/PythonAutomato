# Usar a classe abstrata base
from automato import Automato

# Classe que representa um autômato que reconhece a linguagem L = aba* | ba*ba
class M1(Automato):
    # Construtor dessa classe
    def __init__(self):
        # Construtor da superclasse, passando o conjunto de estados e aceitação
        super().__init__([2, 5])

    # Implementar a função f
    def f(self, estado, simbolo):
        if estado == 0 and simbolo == 'a':
            return 1
        elif estado == 0 and simbolo == 'b':
            return 3
        elif estado == 1 and simbolo == 'b':
            return 2
        elif estado == 2 and simbolo == 'a':
            return 2
        elif estado == 3 and simbolo == 'a':
            return 3
        elif estado == 3 and simbolo == 'b':
            return 4
        elif estado == 4 and simbolo == 'a':
            return 5
        
        return 6