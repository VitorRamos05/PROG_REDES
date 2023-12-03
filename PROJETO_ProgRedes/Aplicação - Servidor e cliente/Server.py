import socket

#--------------------------------------------------------------------------------
HOST_SERVER = 'localhost'   
SOCKET_PORT = 50000         
BUFFER_SIZE = 512           
CODE_PAGE   = 'utf-8'       
MAX_LISTEN  = 1     
#--------------------------------------------------------------------------------

mapeamento_key_server = {
 'help': 'Retorna uma mensagem de ajuda, como um breve texto sobre o que o bot pode fazer e uma lista de comandos',
 'history': 'Retorna o historico de navegação',
 'conf': 'Retorna as opções de configuração',
 'start': 'Inicia a interação com o usuário',
 'connect': 'Conecta-se ao servidor',
 'disconnect': 'Desconecta-se do servidor',
 'pause': 'Pausa a comunicação com o servidor',
 'resume': 'retoma a comunicação com o servidor'
}
print('Recebendo Mensagens...\n\n')

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind((HOST_SERVER, SOCKET_PORT))
tcp_socket.listen(MAX_LISTEN)

while True:
    connect, client = tcp_socket.accept()
    print('Conectado por: ', client)
    
    key_server = input("Digite a chave do servidor que deseja utilizar: ")

    if key_server in mapeamento_key_server:
        connect.send(key_server.encode(CODE_PAGE))
        descricao_client = connect.recv(BUFFER_SIZE).decode(CODE_PAGE)
        print(f'Cliente respondeu com a descrição: {descricao_client}')
    else:
        print('Chave não identificada')

    print('Fechando Conexão do Cliente ', client)
    connect.close()
