import os
from Funcoes_02 import ler_arquivo, ordena_bubble, ordena_insertion, ordena_selection, ordena_quick, salvar_arquivo

def main():
    nome_arquivo = input('Escreva o nome do arquivo que deseja ordenar: ')
    leitura, lista = ler_arquivo(nome_arquivo)

    if leitura:
        print('Lista original:')
        imprimir_lista(lista)
    else:
        print('Falha na leitura do arquivo original')

    if lista:

        metodo = input('Escolha um método de ordenação (Bubble, Quick, Selection ou Insertion):')

        if metodo == 'Bubble':
            ordenar, lista_ordenada = ordena_bubble(lista)
        elif metodo == 'Insertion':
            ordenar, lista_ordenada = ordena_insertion(lista)
        elif metodo == 'Selection':
            ordenar, lista_ordenada = ordena_selection(lista)
        elif metodo == 'Quick':
            ordenar, lista_ordenada = ordena_quick(lista)
        else:
            return False

        if ordenar:
            print('Lista Ordenada:')
            imprimir_lista(lista_ordenada)

        arquivo_saida = input('Digite o nome que deseja salvar o arquivo após a ordenção: ')
        salvar_arquivo(lista_ordenada, arquivo_saida)


def imprimir_lista(lista):
    for numero in lista:
        print(numero)

if __name__ == "__main__":
    main()
