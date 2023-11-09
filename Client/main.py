import pygame, sys
import socket  # Adicionando a biblioteca para comunicação via sockets
import pickle  # Módulo para serializar/deserializar dados
from settings import *
from level import Level
from debug import debug
class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((800, 800))
        pygame.display.set_caption('Maydana Online')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # Inicialização do socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(('localhost', 5555))  # Defina o endereço IP e a porta do servidor

        self.level.create_map()

    def send_data(self, data):
        serialized_data = pickle.dumps(data)
        self.client_socket.send(serialized_data)

    def receive_data(self):
        serialized_data = self.client_socket.recv(1024)  # Tamanho do buffer
        data = pickle.loads(serialized_data)
        return data

    def run(self):

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            data_to_send = {
                "minhaposição": "x: 10, y: 10"
            }  # Informações sobre o movimento do jogador local
            #self.send_data(data_to_send)

            #received_data = self.receive_data()
            # Atualize o estado do jogo com as informações recebidas

            self.level.run()

            debug('Players: ' + str(self.level.players))

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    
    game = Game()
    game.run()