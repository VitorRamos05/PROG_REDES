import socket, threading, requests

SERVIDOR = 'localhost'
PORTA_SERVIDOR = 5678
PORTA_TELEGRAM = 65000
TAMANHO_BUFFER = 512
CODIFICACAO = 'utf-8'

mapeamento_key_server = {
    'help': 'Retorna uma mensagem de ajuda...',
    'history': 'Retorna o historico de navegação',
    'conf': 'Retorna as opções de configuração',
    'start': 'Inicia a interação com o usuário',
    'connect': 'Conecta-se ao servidor',
    'disconnect': 'Desconecta-se do servidor',
    'pause': 'Pausa a comunicação com o servidor',
    'resume': 'retoma a comunicação com o servidor'
}

def lidar_com_cliente(conexao, endereco):
    print(f"Conexão estabelecida com {endereco}")

    try:
        chave_servidor = conexao.recv(TAMANHO_BUFFER).decode(CODIFICACAO)
        print(f"Chave do servidor recebida de {endereco}: {chave_servidor}")

        if chave_servidor in mapeamento_chave_servidor:
            descricao_servidor = mapeamento_chave_servidor[chave_servidor]
            conexao.send(descricao_servidor.encode(CODIFICACAO))

            # Processa o comando recebido do cliente
            resposta = processar_mensagem(chave_servidor)
            conexao.sendall(resposta.encode(CODIFICACAO))

        else:
            print('Chave não identificada')
            conexao.send("Chave não identificada".encode(CODIFICACAO))

    except ConnectionResetError:
        print(f"Conexão redefinida por {endereco}")
    except Exception as e:
        print(f"Erro ao lidar com a conexão: {str(e)}")

    finally:
        conexao.close()
        print(f"Conexão fechada por {endereco}")

def principal():
    thread_servidor = threading.Thread(target=start_server)
    thread_cliente = threading.Thread(target=enviar_comandos)
    thread_servidor.start()
    thread_cliente.start()

if __name__ == '__main__':
    principal()
