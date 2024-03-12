# Carregar o automato
from m1 import M1
from m2 import M2
from m3 import M3
from m4 import M4
from m5 import M5
from m6 import M6

# Usar o automato
afd = M1()
afd_2 = M2()
afd_3 = M3()
afd_4 = M4()
afd_5 = M5()
afd_6 = M6()

fitas = ['aa', 'aba', 'abbbba', 'ab', 'bba', 'abaaa', 'abababa', 'babababa', 'aaaa', 'c', 'baaab', 'baa', 'baab', 'baba', 'aab', 'ab', 'aaba', 'a', 'b', 'aa', 'ab']

def analisa_palavra(maq):
    for fita in fitas:
        print(fita, ':', maq.aceita(fita))

print("-=-=-=-= M1 -=-=-=-=")
analisa_palavra(afd)

print("-=-=-=-= M2 -=-=-=-=")
analisa_palavra(afd_2)

print("-=-=-=-= M3 -=-=-=-=")
analisa_palavra(afd_3)

print("-=-=-=-= M4 -=-=-=-=")
analisa_palavra(afd_4)

print("-=-=-=-= M5 -=-=-=-=")
analisa_palavra(afd_5)

print("-=-=-=-= M6 -=-=-=-=")
analisa_palavra(afd_6)
