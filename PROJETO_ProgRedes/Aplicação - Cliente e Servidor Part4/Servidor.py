import socket
import threading

PORT = 5678
SERVER = '0.0.0.0'

def main():
    print('Recebendo Mensagens...\n\n')

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        tcp_socket.bind((SERVER, PORT))
        tcp_socket.listen(5)

        while True:
            conexao, cliente = tcp_socket.accept()
            print('Conectado: ', cliente)
            conexao_cliente = threading.Thread(target=Cliente, args=(conexao, cliente))
            conexao_cliente.start()
    except OSError as os_err:
        print(f'ERRO: {os_err}')
    finally:
        tcp_socket.close()

def Cliente(conexao, cliente):
    try:
        while True:
            mensagem_cliente = conexao.recv(512).decode('utf-8')
            
            if not mensagem_cliente:
                break
            
            print(f'Mensagem do cliente {cliente}: {mensagem_cliente}')
            if mensagem_cliente == '/exit':
                break

    except Exception as e:
        print(f'Erro na comunicação, o {cliente} está com o problema: {e}')
    finally:
        conexao.close()
        print(f'Conexão com {cliente} encerrada.')

main()
