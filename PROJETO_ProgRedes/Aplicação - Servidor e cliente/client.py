import socket

#--------------------------------------------------------------------------------
HOST_SERVER = 'localhost'   
SOCKET_PORT = 50000         
BUFFER_SIZE = 512           
CODE_PAGE   = 'utf-8'       
MAX_LISTEN  = 1   
#--------------------------------------------------------------------------------

mapeamento_key = {
 'help': 'Retorna uma mensagem de ajuda, como um breve texto sobre o que o bot pode fazer e uma lista de comandos',
 'history': 'Retorna o historico de navegação',
 'conf': 'Retorna as opções de configuração',
 'start': 'Inicia a interação com o usuário',
 'connect': 'Conecta-se ao servidor',
 'disconnect': 'Desconecta-se do servidor',
 'pause': 'Pausa a comunicação com o servidor',
 'resume': 'retoma a comunicação com o servidor'
}

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect((HOST_SERVER, SOCKET_PORT))

while True:
    key = tcp_socket.recv(BUFFER_SIZE).decode(CODE_PAGE)
    
    if key in mapeamento_key:
        descricao = mapeamento_key[key]
        print(f'Recebido: {key}. Descrição: {descricao}')

        tcp_socket.send(descricao.encode(CODE_PAGE))
    else:
        print(f'Chave não indentificada: {key}')
    
    tcp_socket.close()
