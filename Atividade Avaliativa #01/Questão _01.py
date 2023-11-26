import random,os,sys
from Funcoes_01 import gerar_lista

DIRATUAL = os.path.dirname(os.path.abspath(__file__))

try:
    quantidade = int(input('Indique a quantidade de elementos da lista: '))
    valormin = int(input('Indique o valor mínimo presente na lista: '))
    valormax = int(input('Indique o valor máximo presente na lista: '))
    
except ValueError:
    print('\nERRO: O número informado não é inteiro.\n')
    sys.exit()

if quantidade <= 0 or valormin <= 0 or valormax <= 0:
    print(f'\nAVISO: Informe um valor inteiro positivo...\n')
    sys.exit()

boolSucesso, lista_gerada = gerar_lista(quantidade, valormin, valormax)

if boolSucesso:
    print(f"{lista_gerada}")
else:
    print("Não foi possível gerar a lista corretamente.")
