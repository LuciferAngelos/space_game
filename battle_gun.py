import pygame
from pygame.sprite import Sprite

# наследование от класса Sprite в аргументе


class Gun(Sprite):
    '''Класс пушки'''

    def __init__(self, screen):
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/battle_ship.png')
        # получил картинку корабля, как прямоугольник
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # координата х пушки будет по центру экрана
        self.rect.centerx = self.screen_rect.centerx
        # координата y пушки будет внизу экрана
        self.rect.bottom = self.screen_rect.bottom - 15
        # нажатие\отжатие клавиши
        self.center = float(self.rect.centerx)
        self.mright = False
        self.mleft = False

    def output(self):
        '''рисование пушки'''
        # метод отрисовывает пушку (рисунок и где)
        self.screen.blit(self.image, self.rect)

    '''обновление позиции'''

    def update_gun(self):
        # если тру и положение квадрата пушки меньше края экрана
        if self.mright and self.rect.right < self.screen_rect.right:
            # если тру - двигаем вправо
            self.center += 1.5
        if self.mleft and self.rect.left > self.screen_rect.left:
            # если тру - двигаем вправо
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        '''размещает пушку внизу по центру'''
        self.center = self.screen_rect.centerx
