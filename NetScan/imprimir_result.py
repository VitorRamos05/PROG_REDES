def imprimir_resultados(linhas):
    for linha in linhas:
        porta, protocolo, descrição = int(linha[0]), linha[1], linha[2]
        print(f'Porta {porta} --> Protocolo {protocolo}: {descrição}')
