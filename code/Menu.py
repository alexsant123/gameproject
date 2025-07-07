
from pygame import Surface, Rect
from pygame.font import Font



import pygame
import os

from code.const import COLOR, MENU_OPTION, WIN_WIDTH, COLOR2


class Menu:
    def __init__(self, screen):
        self.screen = screen

        # 1. Carrega a imagem original
        self.image = pygame.image.load(os.path.join('asset', 'menu.png')).convert_alpha()

        # 2. Redimensiona a imagem para 600×600 (ou use screen.get_size())
        self.image = pygame.transform.scale(self.image, (800, 600))

        # 3. Guarda o rect (se precisar para cliques, etc.)
        self.rect = self.image.get_rect()

    def run(self):
        menu_option = 0

        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                   quit() # sair do loop principal
            self.screen.blit(self.image, (0, 0))
            self.menu_text(50, "SPACE TRAVEL", COLOR, (800 // 2, 30))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR2, ((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:  # DOWN KEY
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:  # UP KEY
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:  # ENTER
                        return MENU_OPTION[menu_option]


            pygame.display.flip()
            clock.tick(60)

        pygame.quit()




    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
     text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
     text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
     text_rect: Rect = text_surf.get_rect(center=text_center_pos)
     self.screen.blit(source=text_surf, dest=text_rect)