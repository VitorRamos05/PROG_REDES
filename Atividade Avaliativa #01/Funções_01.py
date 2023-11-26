import random, os, sys

DIRATUAL = os.path.dirname(os.path.abspath(__file__))

arquivo = input("Informe o nome do arquivo a ser gerado: ")

def gerar_lista(quantidade: int, valor_minimo: int, valor_maximo: int):
    if quantidade <= 0 or valor_minimo >= valor_maximo:
        return False, None

    lista = [random.randint(valor_minimo, valor_maximo) for _ in range(quantidade)]
    salvar_sucesso = salvar_lista(lista, f'{arquivo}')

    return salvar_sucesso, lista

def salvar_lista(nome_lista: list, nome_arquivo: str):
    try:
        with open(nome_arquivo, 'w') as arquivo_output:
            arquivo_output.writelines([f'{item}\n' for item in nome_lista])
        return True
    except Exception as erro:
        print(f'\nERRO: {erro}')
        return False
