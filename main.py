import pygame
import random
import os
pygame.init()

WIN_W = 280
WIN_H = 50
file_path = os.path.dirname(os.path.realpath(__file__))

FPS = 60
# colors in game
colors = {
    "BLACK"     : (0,0,0),
    "WHITE"     : (255,255,255),
}

screen = pygame.display.set_mode([WIN_W, WIN_H])
pygame.display.set_caption('Text Animation')

class INFOTEXT():
    def __init__(self):
        self.fonts_array = "1234567890-[],./abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.text = "***********"
        self.text_original = "Hello World"
        self.index = 0

    def draw_text(self):
        font = pygame.font.Font(file_path + '\\researcher-researcher-bold-700.ttf', 36)
        self.text_for_show = self.text
        text = font.render(self.text_for_show, True, colors["WHITE"])
        textRect = text.get_rect()
        textRect.left = (10)
        textRect.top = (10)
        screen.blit(text, textRect)

    def animate_text(self, i):
        self.text = self.text_original[0:i] + self.fonts_array[random.randint(0,67)] + self.text[i+1:]

do_animation = False
animation = 0
index_i = 0
index_j = 0
info_text = INFOTEXT()
GAME_CLOCK = pygame.time.Clock()

#   Start Game Engine
running = True
while running:
    #   Get event in pygame
    event_list = pygame.event.get()
    for event in event_list:
        #   Closing window event
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not do_animation:
                    do_animation = True
                    animation = 0
                    index_i = 0
                    index_j = 0

    #   Fill screen with BLACK color
    screen.fill(colors["BLACK"])
    #   Put the background image
    info_text.draw_text()
    
    if do_animation:
        if animation < 2:
            animation += 1
        else:
            animation = 0
            if index_i < len(info_text.text):
                info_text.animate_text(index_i)
                index_j += 1
            else:
                info_text.text = info_text.text_original
                do_animation = False
            if index_j == 5:
                index_j = 0
                index_i += 1

    #   Set FPS for game
    GAME_CLOCK.tick(FPS)
    #   Display construced screen
    pygame.display.update()

#   Exit pygame
pygame.quit()
#   Close the window
exit()