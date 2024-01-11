import struct
import subprocess
import time

def escrever_cabecalho_arquivo(nome_arquivo):
    formato_cabecalho = '!IHHIIIB'
    sequencial = 0xa1b2c3d4
    versao_maior = 2
    versao_menor = 4
    reservado1 = 0
    reservado2 = 0
    comprimento_snap = 65535
    fcs = 0
    tipo_link = 1  # Exemplo para Ethernet

    cabecalho = struct.pack(cabecalho_formato, numero_magico, versao_maior, versao_menor,
                            reservado1, reservado2, comprimento_snap, fcs | (tipo_link << 16))

    with open(nome_arquivo, 'wb') as arquivo:
        arquivo.write(cabecalho)

def escrever_pacote(nome_arquivo, timestamp_sec, timestamp_usec, comprimento_capturado, comprimento_original, dados_pacote):
  
    pacote_formato = '!IIII'
    
    pacote = struct.pack(pacote_formato, int(timestamp_sec), int(timestamp_usec),
                        int(comprimento_capturado), int(comprimento_original))

    with open(nome_arquivo, 'ab') as arquivo:
        arquivo.write(pacote)
        arquivo.write(dados_pacote)

def gravar_trafego(nome_arquivo):
    comando = ['tcpdump', '-w', nome_arquivo + '.cap']
    try:
        subprocess.run(comando, check=True)
        print(f"O tráfego foi gravado em {nome_arquivo}.cap")
        escrever_cabecalho_arquivo(nome_arquivo)
        timestamp_sec = time.time()
        timestamp_usec = 0
        comprimento_capturado = 14  # Tamanho capturado arbitrário para este exemplo
        comprimento_original = 14  # Tamanho original arbitrário para este exemplo
        dados_pacote = b'\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e'
        escrever_pacote(nome_arquivo, timestamp_sec, timestamp_usec, comprimento_capturado, comprimento_original, dados_pacote)

    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar tcpdump: {e}")

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo para gravar o tráfego: ")
    gravar_trafego(nome_arquivo)
