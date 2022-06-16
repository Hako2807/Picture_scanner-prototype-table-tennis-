import pygame
import sys

class Visualization:
    def __init__(self, size, fps = 60):
        pygame.init()
        self.size = size
        self.screen = pygame.display.set_mode(self.size)
        self.fps = fps
        self.clock = pygame.time.Clock()

    def update(self, picture, rect_pos):
        self.check_events()
        self.screen.fill(("white"))

        self.show_picture(picture, rect_pos)
        if pygame.mouse.get_pressed()[0]: print(pygame.mouse.get_pos())

        pygame.display.update()
        self.clock.tick(self.fps)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def show_picture(self, picture, rect_pos):
        self.picture_surface = pygame.image.load("pictures/"+picture)
        pygame.transform.scale(self.picture_surface, self.screen.get_size())
        self.screen.blit(self.picture_surface, (0,0))
        self.draw_rectangle(rect_pos)

    def draw_rectangle(self, position):
        pygame.draw.rect(self.screen, "green", position, 4)
