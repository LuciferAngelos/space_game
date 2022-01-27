import pygame  # модуль самого игрового движка
from battle_gun import Gun
import controls
from pygame.sprite import Group
from stats import Stats
from scores import Scores
from mini_battle_gun import Mini_gun


def run():
    '''инициализация игры'''
    pygame.init()  # инициализация

    # указываю размеры окна. Указывается кортеж
    screen = pygame.display.set_mode((700, 800))

    # заголовок окна
    pygame.display.set_caption('Space defenders')

    # фоновый цвет окна
    bg_color = (0, 0, 0)

    gun = Gun(screen)
    mini_gun = Mini_gun(screen)
    bullets = Group()
    # объект инопланетян
    aliens = Group()

    controls.create_alien_army(screen, aliens)

    # stats
    stats = Stats()

    # scores
    scores = Scores(screen, stats)
    # чтобы окно сразу не закрывалось после запуска, создаю главный цикл игры
    while True:
        # функция прослушки ивентов
        controls.events(screen, gun, bullets)

        if stats.run_game:
            # обновление пушки
            gun.update_gun()

            # обновление пули
            controls.update_bullets(screen, stats, scores, aliens, bullets)

            # обновляет позицию пришельца
            controls.update_aliens_position(
                stats, screen, scores, gun, aliens, bullets)
            controls.update(bg_color, screen, stats,
                            scores, gun, aliens, bullets)


run()
