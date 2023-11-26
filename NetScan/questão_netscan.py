import socket, sys, os
from verificar_portas import verificar_porta
from imprimir_result import imprimir_resultados

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
arquivo_protocolos = os.path.join(diretorio_atual, 'NET_SCAN.csv')

try:
    host = input("Informe o Host que deseja: ")
    ip = socket.gethostbyname(host)

except Exception as e:
    print(f"Erro: informe um nome de Host valido: {e}")
    sys.exit(1)

try:
    with open(arquivo_protocolos, 'r', encoding='utf-8') as arquivo_protocolos:
        linhas = [linha.strip().strip('"').split('", "') for linha in arquivo_protocolos]

except FileNotFoundError:
    print(f"Erro: O arquivo {arquivo_protocolos} não foi encontrado.")
    sys.exit(1)

except Exception as e:
    print(f"Erro: Não foi possivel abrir o arquivo: {e}")
    sys.exit(1)

TCP, UDP, TCP_UDP = [], [], []

for linha in linhas:
    portas, protocolo, descrição = int(linha[0]), linha[1], linha[2]

    if protocolo == "TCP,UDP":
        TCP_UDP.append(portas)
    elif protocolo == "TCP":
        TCP.append(portas)
    elif protocolo == "UDP":
        UDP.append(portas)

try:
    for portas in linhas:
        porta, protocolo, descrição = int(portas[0]), portas[1], portas[2]

        try:
            if porta in TCP or (porta in TCP_UDP and protocolo == 'TCP'):
                verificar_porta(ip, porta, 'TCP', descrição)
            if porta in UDP or (porta in TCP_UDP and protocolo == 'UDP'):
                verificar_porta(ip, porta, 'UDP', descrição)

        except Exception as e:
            print(f"Erro: Nâo foi possivel verificar a porta {porta}: {e}")

except KeyboardInterrupt:
    print("\nVerificação de portas interrompida manualmente.")
    sys.exit(0)

imprimir_resultados(linhas)
