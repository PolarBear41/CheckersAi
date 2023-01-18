import pygame

WIDTH = 600
HEIGHT = 600
ROWS = 8
COLS = 8
SQUARE_SIZE = WIDTH//COLS

# definirea constantelor care pot fi schimbate doar din acest fisier
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128,128,128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))