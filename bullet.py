import pygame


class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        '''создание пули в текущей позиции пушки'''

        super(Bullet, self).__init__()
        self.screen = screen
        # отрисовываем пулю. Пуля - маленький прямоугольник
        #Rect(0, 0, 2, 12) - (координаты, координаты, ширина, высота)
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = (155, 38, 176)
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        '''перемещение пули по оси у вверх'''
        self.y -= self.speed
        # обновление позиции пули
        self.rect.y = self.y

    def draw_bullet(self):
        '''отрисовка пули на экране'''
        pygame.draw.rect(self.screen, self.color, self.rect)
