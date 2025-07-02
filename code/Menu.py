
import pygame
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('./asset/menu.png')
        self.image = pygame.transform.scale(self.image, (600, 600))  # largura, altura desejadas
    def draw(self):
        self.screen.blit(self.image, (0, 0))