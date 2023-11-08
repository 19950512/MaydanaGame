import socket
import pickle
import threading

class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 5555))
        self.server_socket.listen(2)

        self.client_sockets = []
        self.addresses = []

    def accept_connections(self):
        while True:
            client_socket, address = self.server_socket.accept()
            print(f"Connection from {address} has been established.")
            self.client_sockets.append(client_socket)
            self.addresses.append(address)

    def send_data_to_clients(self, data):
        serialized_data = pickle.dumps(data)
        for client_socket in self.client_sockets:
            client_socket.send(serialized_data)

    def receive_data_from_client(self, client_socket):
        serialized_data = client_socket.recv(1024)
        data = pickle.loads(serialized_data)
        return data

    def receive_data_from_clients(self):
        all_data = []
        for client_socket in self.client_sockets:
            data = self.receive_data_from_client(client_socket)
            all_data.append(data)
        return all_data

    def close_connections(self):
        for client_socket in self.client_sockets:
            client_socket.close()
        self.server_socket.close()

    def run_server(self):
        thread = threading.Thread(target=self.accept_connections)
        thread.daemon = True  # Permite que a thread seja encerrada quando o programa principal terminar
        thread.start()

if __name__ == '__main__':
    print("Server is running...")
    server = Server()
    server.run_server()

    while True:
        received_data = server.receive_data_from_clients()

        # Lógica para processar os dados recebidos
        data_to_send = {"players": [
            {"x": 10, "y": 10},
            {"x": 20, "y": 20}
        ]}
        server.send_data_to_clients(data_to_send)

    server.close_connections()
