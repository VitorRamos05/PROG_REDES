import socket
import threading

PORTA = 5678
SERVIDOR = 'localhost'
MENSAGEM = 'Digite sua mensagem, caso possua duvida digite /help: '

def Cliente(sock):
    while True:
        try:
            msg = input(MENSAGEM)
            if msg != '':
                sock.send(msg.encode('utf-8'))
                if msg == '/disconnect':
                    print('Conexão encerrada pelo cliente.')
                    break
        except:
            print('Conexão encerrada.')
            break

def Servidor(sock):
    msg = b' '
    while msg != b'':
        try:
            msg = sock.recv(512)
            decoded_msg = msg.decode('utf-8')
            print("\n" + decoded_msg + "\n" + MENSAGEM)
            
            if decoded_msg == '/exit':
                print('Conexão encerrada pelo cliente.')
                break
        except:
            msg = b''

def Encerrar(sock):
    try:
        sock.close()
    except:
        None

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVIDOR, PORTA))
    print("Você esta conectado ao: ", (SERVIDOR, PORTA))
    coenection_server = threading.Thread(target=Servidor, args=(sock,))
    conection_user = threading.Thread(target=Cliente, args=(sock,))
    coenection_server.start()
    conection_user.start()
    conection_user.join()
except Exception as e:
    print("ERRO", e)
finally:
    Encerrar(sock)
