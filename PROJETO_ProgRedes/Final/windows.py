import platform
import subprocess
import os
import sqlite3
from browser_history.browsers import Chrome, Edge, Firefox

def obter_informacoes_hardware():
    try:
        sistema_operacional = platform.system()
        processador = platform.processor()
        arquitetura = f"{platform.architecture()[0]} {platform.architecture()[1]}"

        resultado_memoria = subprocess.run(['systeminfo'], capture_output=True, text=True)
        memoria_total = [linha for linha in resultado_memoria.stdout.split('\n') if 'Memória física total:' in linha]
        total = memoria_total[0].split(':')[-1].strip()
        memoria_dis = [linha for linha in resultado_memoria.stdout.split('\n') if 'Memória física disponível:' in linha]
        disponivel = memoria_dis[0].split(':')[-1].strip()

        resultado_disco = subprocess.run(['wmic', 'logicaldisk', 'get', 'size,freespace,caption'], capture_output=True, text=True)
        linhas_disco = resultado_disco.stdout.strip().split('\n')
        dados_disco = linhas_disco[2].split()
        espaco_livre = int(dados_disco[1]) / (1024 ** 3)
        total_disco = int(dados_disco[2]) / (1024 ** 3)

        informacoes = (
            f"Sistema Operacional: {sistema_operacional}\n"
            f"Processador: {processador}\n"
            f"Arquitetura: {arquitetura}\n"
            f"\n----- INFORMAÇÕES DE DISCO -----\n"
            f"Espaço livre em disco: {espaco_livre:.2f} GB\n"
            f"Espaço total em disco: {total_disco:.2f} GB\n"
            f"\n----- INFORMAÇÕES DE MEMÓRIA -----\n"
            f"Memória Total: {total}\n"
            f"Memória Disponível: {disponivel}"
        )

        return informacoes

    except Exception as e:
        return f'Não foi possível obter as informações de Hardware: {str(e)}'

def obter_historico_navegador(classe_navegador):
    try:
        navegador = classe_navegador()
        saidas = navegador.fetch_history()

        historico = [saidas.histories[0]]
        for i in range(1, len(saidas.histories)):
            if saidas.histories[i] != saidas.histories[i-1]:
                historico.append(saidas.histories[i])

        for info in historico[-10:]:
            print("=" * 50)
            print(f"Data e Hora: {info[0]}")
            print(f"URL: {info[1]}")
            print(f"Título: {info[2]}")

    except Exception as e:
        return f"Erro ao tentar receber histórico de navegação do navegador!!! {str(e)}"

# Exemplos de uso:
print(obter_informacoes_hardware())
obter_historico_navegador(Chrome)
obter_historico_navegador(Edge)
obter_historico_navegador(Firefox)
