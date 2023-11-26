import socket

def verificar_porta(ip, porta, protocolo, descrição):
    sockt = None
    try:
        sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM if protocolo == 'TCP' else socket.SOCK_DGRAM)
        if sockt.connect_ex((ip, porta)) == 0:
            print(f'Porta {porta} --> Protocolo {protocolo}: {descrição} --> Status: Responde (Aberta)')
        else:
            print(f'Porta {porta} --> Protocolo {protocolo}: {descrição} --> Status: Não Responde (Fechada)')
    except Exception as e:
        print(f"Erro: Não foi possivel verificar a {porta}: {e}")
    finally:
        if sockt:
            sockt.close()
