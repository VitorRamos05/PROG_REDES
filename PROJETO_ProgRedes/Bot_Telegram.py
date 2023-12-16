import requests, json

def Get_Messages(update_id, url_base):
    link = f'{url_base}getUpdates?timeout=100'
    if update_id:
        link = f'{link}&offset={update_id + 1}'   
    result = requests.get(link)
    try:
        data = json.loads(result.content)
        return data.get('result', [])
    except json.JSONDecodeError:
        return []

def Start():
    update_id = None
    token = '6409317827:AAHu7ChqyhJPsduRn8lFCQYrVYdcSX5vJic'
    url_base = f'https://api.telegram.org/bot{token}/'

    while True:
        update = Get_Messages(update_id, url_base)
        Messages = update
        if Messages:
            for message in Messages:
                update_id = message.get('update_id', update_id)
                chat_id = message['message']['from']['id']

                resposta = command(message, chat_id, url_base)
                Resposta(resposta, chat_id, url_base)
    
def command(message, chat_id, url_base):
    try:
        text = message['message']['text']
        
        if text == '/start':
            return 'Seja bem-vindo ao bot ProjectProgRedes! No que posso ajudá-lo? (Utilize o comando /help caso tenha alguma duvida) '
        elif text in ['/help', '/start', '/conf', '/connect', '/disconnect', '/pause', '/resume', '/history']:
            return Executar_comando(text)
        else:
            return 'Comando desconhecido. Utilize o /help para saber quais são os comandos executaveis.'
    except KeyError:
        return 'Não consigo execuatar esse tipo de solicitação. Utilize o /help para saber quais são os comandos executaveis'
    
def Executar_comando(command):
    if command == '/help':
        return 'Esses são os comandos que você podera utilizar: \n/history: Retorna o historico de navegação.\n/conf: Retorna as opções de configuração.\n/start: Inicia a interação com o usuário.\n/connect: Conecta-se ao servidor.\n/disconnect: Desconecta-se do servidor.\n/pause: Pausa a comunicação com o servidor.\n/resume: retoma a comunicação com o servidor.'
    elif command == '/start':
        return 'Comando em Execução:\nInicia a interação com o usuário.'
    elif command == '/conf':
        return 'Comando em Execução\nRetorna as opções de configuração.'
    elif command == '/connect':
        return 'Comando em Execução:\nConecta-se ao servidor.'
    elif command == '/disconnect':
        return 'Comando em Execução:\nDesconecta-se do servidor.'
    elif command == '/pause':
        return 'Comando em Execução:\nPausa a comunicação com o servidor.'
    elif command == '/resume':
        return 'Comando em Execução:\nRetoma a comunicação com o servidor.'
    elif command == '/history':
        return 'Comando em Execução:\nRetorna o historico de navegação.'
    
def Resposta(resposta, chat_id, url_base):
    link_envio = f'{url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_envio)

if __name__ == '__main__':
    Start()
