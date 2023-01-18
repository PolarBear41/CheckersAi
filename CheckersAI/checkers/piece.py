from .constants import RED, WHITE, SQUARE_SIZE, GREY, CROWN
import pygame

#definirea clasei Piece care va fi folosita pentru algoritmul minimax si pentru functionarea jocului
class Piece:
    PADDING = 15
    OUTLINE = 2

    #definirea pieselor 
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    #calculeaza pozitia pieselor
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    #va fi de folos pentru a schimba o piesa in rege
    def make_king(self):
        self.king = True
    
    #desenarea pieselor pe tabla
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2)) #daca o piesa devine rege, atunci acesta isi va schimba aparenta cu imaginea din /asssets

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    def __repr__(self):
        return str(self.color)