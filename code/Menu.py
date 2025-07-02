
import pygame
class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.transform.scale( (800, 600))

    def draw(self):
        self.screen.blit(self.image, (0, 0))