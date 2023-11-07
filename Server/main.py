import socket

# Defina o IP e porta que o servidor vai escutar
SERVER_IP = '127.0.0.1'  # Substitua pelo IP do servidor
SERVER_PORT = 5555  # Escolha uma porta disponível

# Criação do socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((SERVER_IP, SERVER_PORT))

print('Servidor iniciado. Aguardando conexões...')

while True:
    data, client_address = server_socket.recvfrom(1024)  # Recebe os dados do cliente
    print(f"Recebido de {client_address}: {data.decode()}")

    # Aqui você pode processar os dados recebidos e enviar respostas se necessário
    # Por exemplo:
    # server_socket.sendto(b'Mensagem de resposta', client_address)
