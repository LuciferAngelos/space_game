import pygame

# делаем на основе класса sprite


class Alien(pygame.sprite.Sprite):
    '''класс одного пришельца'''

    def __init__(self, screen):
        '''инициализирую и задаю начальную позицию'''

        super(Alien, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        # положение по оси х
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw_alien(self):
        '''вывод пришельца на экран'''
        # метод отрисовывает инопланетянина (рисунок и где)
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''перемещает пришельцев на пушку'''
        self.y += 0.1
        self.rect.y = self.y
