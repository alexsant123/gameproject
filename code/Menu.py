
from pygame import Surface, Rect
from pygame.font import Font



import pygame
import os

class Menu:
    def __init__(self, screen):
        self.screen = screen

        # 1. Carrega a imagem original
        self.image = pygame.image.load(os.path.join('asset', 'menu.png')).convert_alpha()

        # 2. Redimensiona a imagem para 600×600 (ou use screen.get_size())
        self.image = pygame.transform.scale(self.image, (600, 600))

        # 3. Guarda o rect (se precisar para cliques, etc.)
        self.rect = self.image.get_rect()

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()          # encerra o loop

            # Desenha o fundo do menu
            self.screen.blit(self.image, (0, 0))

            # Aqui você pode desenhar textos, botões, etc.

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()






    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
     text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
     text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
     text_rect: Rect = text_surf.get_rect(center=text_center_pos)
     self.screen.blit(source=text_surf, dest=text_rect)