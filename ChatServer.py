import socket
import threading
import os

#Função para coletar endereço local
def get_lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

# Configurações do servidor
host = get_lan_ip()
port = 12345
print(f"Endereço: {host} | Porta: {port}")

#Configuração do CMD
os.system(f'title PYCHAT SERVER - Endereço: {host} - Porta: {port}')

# Cria o socket do servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)  # Número máximo de conexões pendentes
print("Aguardando conexões...")

# Lista de clientes conectados
clientes = []

# Função para lidar com as mensagens dos clientes
def handle_client(client_socket):
    while True:
        try:
            # Recebe dados do cliente
            data = client_socket.recv(1024)
            if not data:
                break

            # Encaminha a mensagem para todos os clientes conectados
            for cliente in clientes:
                if cliente != client_socket: #Evita que a mensagem seja enviada para o remetente
                    cliente.send(data)

        except:
            break

# Loop principal do servidor
while True:
    client_socket, addr = server_socket.accept()
    print(f"Conexão estabelecida com {addr[0]}:{addr[1]}")
    
    # Adiciona o cliente à lista de clientes
    clientes.append(client_socket)
    
    # Inicia uma thread para lidar com o cliente
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()
