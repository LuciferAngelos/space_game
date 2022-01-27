from email.headerregistry import Group
import pygame.font
from mini_battle_gun import Mini_gun
from pygame.sprite import Group


class Scores():
    '''вывод игровой информации, очков'''

    def __init__(self, screen, stats):
        '''инициализация подсчет очков'''
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (155, 38, 176)
        self.high_score_color = (252, 219, 3)
        # шрифт из библиотеки 2 аргумента
        # 1 - семейство шрифта (none - дефолт), 2 - размер шрифта
        self.font = pygame.font.SysFont(None, 46)
        # преобразование текста в изображение и дальнейшая отрисовка на экране
        self.image_score()
        self.image_high_score()
        self.image_lives()

    def image_score(self):
        '''преобразовывает текст счета в графическое изображение'''
        # преобразование текста счёта в картинку
        # args to .render(): 1 - счёт, 2 - хз, 3 - цвет текста, 4 - цвет фона
        self.score_img = self.font.render(
            str(self.stats.score), True, self.text_color, (0, 0, 0))
        # прямоугольник для текста
        self.score_rect = self.score_img.get_rect()
        # размещение на экране
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        '''преобразование рекорда в графическое изображение'''
        self.high_score_image = self.font.render(
            str(self.stats.high_score), True, self.high_score_color, (0, 0, 0))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 40
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_lives(self):
        ''''количество жизней'''
        self.lives = Group()

        for lives_number in range(self.stats.lives):
            live = Mini_gun(self.screen)
            self.screen_rect = self.screen.get_rect()
            live.rect.x = 260 + lives_number * live.rect.width
            live.rect.y = 20
            self.lives.add(live)

    def show_score(self):
        '''вывод счета на экран'''
        # что рисуем, где рисуем
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.lives.draw(self.screen)
