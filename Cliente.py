import socket
import threading

# Configurações do cliente
host = '192.168.10.126'  # Substitua pelo IP do servidor
port = 12345

NOME = input("Digite o seu nome de usúario: ")

# Cria o socket do cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
print("Conexão estabelecida.")

# Função para enviar mensagens
def enviar_mensagem():
    while True:
        mensagem = input()
        mensagem = '['+NOME+']' + mensagem
        client_socket.send(mensagem.encode())

# Função para receber mensagens
def receber_mensagem():
    while True:
        data = client_socket.recv(1024)
        print(data.decode())

# Inicia threads para enviar e receber mensagens
enviar_thread = threading.Thread(target=enviar_mensagem)
receber_thread = threading.Thread(target=receber_mensagem)

enviar_thread.start()
receber_thread.start()
