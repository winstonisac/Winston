import pygame

from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

FONT_STYLE = "freesansbold.ttf"
FONT_SIZE = 22
FONT_COLOR = (0, 0, 0)


def reusable_method(text, 
    screen,
    x_position,
    y_position,
    font_color = FONT_COLOR,
    font_size = FONT_SIZE
):

    font = pygame.font.Font(FONT_STYLE, font_size)
    text = font.render(text, True, font_color)
    text_rect = text.get_rect()
    text_rect.center = (x_position, y_position)
    screen.blit(text, text_rect)

