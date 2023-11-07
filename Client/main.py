import pygame, sys
import socket  # Adicionando a biblioteca para comunicação via sockets
from settings import *
import time
from level import Level
from debug import debug

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Maydana Online')
        self.clock = pygame.time.Clock()

        self.min_time_between_updates = 0.5
        self.last_update_time = time.time() # Inicializa a variável com o tempo atual

        self.level = Level()

        # Estabelecer conexão com o servidor usando UDP
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def run(self):
        while True:

            current_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Encerra a aplicação e envia mensagem de encerramento para o servidor
                    self.server_socket.sendto(b'exit', (SERVER_IP, SERVER_PORT))
                    
                    pygame.quit()
                    sys.exit()

            self.screen.fill('black')
            self.level.run()


            # Aqui, você pode enviar e receber dados para e do servidor
            # Exemplo: self.server_socket.sendto(data, (SERVER_IP, SERVER_PORT)) para enviar dados ao servidor
            if self.level.player.last_position != self.level.player.direction and (current_time - self.last_update_time) > self.min_time_between_updates:
                self.level.player.last_position = self.level.player.direction
                message = 'Posicao do Player -' + str(self.level.player.direction.x)
                self.server_socket.sendto(message.encode(), (SERVER_IP, SERVER_PORT))
                self.last_update_time = current_time  # Atualiza o tempo da última atualização

            # Exemplo: received_data, server = self.server_socket.recvfrom(1024) para receber dados do servidor

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == '__main__':
    game = Game()
    game.run()