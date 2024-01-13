import platform, subprocess, socket, os, sqlite3
from browser_history.browsers import Chrome, Edge, Firefox

def obter_informacao_memoria():
    try:
        cabecalho = subprocess.run('free | grep "total"', capture_output=True, text=True, shell=True)
        memoria = subprocess.run('free -m | grep "Mem:"', capture_output=True, text=True, shell=True)

        informacao = f"\nInformações sobre a memória:\n{cabecalho.stdout}\n{memoria.stdout}"

        return informacao
    except Exception as e:
        return f"Erro ao obter informações de memória: {str(e)}"

def obter_informacao_disco():
    try:
        cabecalho = subprocess.run('df -h | grep -i "File"', shell=True, capture_output=True, text=True)
        discos = ["/dev/sda", "/dev/root", "/dev/mapper", "/dev/nvme0n1p1"]

        for disco in discos:
            try:
                armazenamento = subprocess.run(f'df -h | grep -i "{disco}"', capture_output=True, text=True, shell=True)
                break
            except:
                continue

        informacao = f"\nInformações do disco:\n\n{cabecalho.stdout}{armazenamento.stdout}"

        return informacao
    except Exception as e:
        return f"Erro ao obter informações de disco: {str(e)}"

def obter_informacao_hardware():
    try:
        sistema_operacional = platform.system()
        processador = platform.processor()
        arquitetura = platform.architecture()[0]

        informacoes = [
            f"Sistema Operacional: {sistema_operacional}\n",
            f"Processador: {processador}\n",
            f"Arquitetura: {arquitetura} {platform.architecture()[1]}\n",
            f"Informações do Disco: {obter_informacao_disco()}\n",
            f"Informações da Memória: {obter_informacao_memoria()}"
        ]

        return informacoes
    except Exception as e:
        return f'Não foi possível obter as informações de Hardware: {str(e)}'

def obter_programas_instalados():
    try:
        resultado = subprocess.run(['apt', 'list', '--installed'], capture_output=True, text=True, shell=True)
        linhas = resultado.stdout.splitlines()

        informacoes = "\n---------- INFORMAÇÕES DE PROGRAMAS INSTALADOS ----------\n\n"
        for linha in linhas[2:-3]:
            informacoes += linha + "\n"

        return informacoes
    except Exception as e:
        return f'Não foi possível obter as informações de programas instalados: {str(e)}'

def obter_informacao_usuario():
    try:
        usuario = os.getlogin()
        resultado_grupos = subprocess.run(['groups', usuario], capture_output=True, text=True, shell=True)
        primario = resultado_grupos.stdout.strip().split()
        secundario = ('\n'.join(primario[3:]))

        saida = f"\n--- Grupo Principal ---\n{primario[2]}\n\n--- Grupos Secundários ---\n{secundario}"
        return (
            f"Usuário: {usuario}\n"
            f"Diretório Inicial: {os.path.expanduser('~')}\n"
            f"Identificação de usuário: UID = {os.getuid()}\n"
            f"Os grupos do usuário são: {primario[2]}\n"
            f"\nO Shell padrão do Usuário é: {os.environ.get('SHELL', 'N/A')}"
        )
    except Exception as e:
        return f'Não foi possível obter informações do usuário: {str(e)}'

def obter_informacao_agente():
    try:
        informacoes = [
            f"Nome do host: {socket.gethostname()}\n"
            f"Usuário logado: {os.getlogin()}\n"
            f"IP do Host: {socket.gethostbyname(socket.gethostname())}\n"
        ]
        return informacoes
    except Exception as e:
        return f'Não foi possível obter as informações do Agente: {str(e)}'

def obter_historico_navegador(browser, caminho):
    try:
        con = sqlite3.connect(caminho)
        cur = con.cursor()
        cur.execute("select url, title, visit_count from urls")
        resultados = cur.fetchall()
        for resultado in resultados:
            print(resultado)
    except Exception as e:
        print(f'Erro ao obter histórico do {browser}: {str(e)}')

# Exemplos de como chamar as funções:
print(obter_informacao_hardware())
print(obter_programas_instalados())
print(obter_informacao_usuario())
print(obter_informacao_agente())
obter_historico_navegador("Google Chrome", f"/home/{os.getlogin()}/.config/google-chrome/Default/History")
obter_historico_navegador("Microsoft Edge", f"/home/{os.getlogin()}/.config/microsoft-edge/Default/History")
obter_historico_navegador("Opera", f"/home/{os.getlogin()}/.config/opera/Default/History")
