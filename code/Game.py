

import pygame
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Meu Jogo")
        self.clock = pygame.time.Clock()
        self.running = True
        self.menu = Menu(self.screen)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.menu.draw()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
