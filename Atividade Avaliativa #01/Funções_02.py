import os, sys

DIRATUAL = os.path.dirname(os.path.abspath(__file__))

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as file:
            lista = [int(line.strip()) for line in file]
        return True, lista
    except FileNotFoundError:
        return False, None
    except Exception as x:
        print(f'\nErro não indentificado: {x}')
        sys.exit()

def ordena_bubble(lista):
    a = len(lista)
    for i in range(a):
        for z in range(0, a - i - 1):
            if lista[z] > lista[z + 1]:
                lista[z], lista[z + 1] = lista[z + 1], lista[z]
    return True, lista

def ordena_insertion(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and chave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return True, lista

def ordena_selection(lista):
    n = len(lista)

    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j

        lista[i], lista[menor] = lista[menor], lista[i]

    return True, lista

def ordena_quick(lista):
    if len(lista) <= 1:
        return True, lista
    
    central = lista[len(lista) // 2 ]
    esquerdo = [y for y in lista if y < central]
    meio = [y for y in lista if y == central]
    direito = [y for y in lista if y > central]
    
    return True, ordena_quick(esquerdo)[1] + meio + ordena_quick(direito)[1]

def salvar_arquivo(lista, nome_arquivo):
    try: 
        with open(f'{nome_arquivo}.txt', 'w') as arquivo:
            for numero in lista:
                arquivo.write(str(numero) + '\n')
        print(f'Lista salva em: {nome_arquivo}')
    except Exception as erro:
        print(f'Erro ao tentar salvar o arquivo:{erro}')
