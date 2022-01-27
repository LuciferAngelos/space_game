import imp
import pygame
import sys
from bullet import Bullet
from alien import Alien
import time


def events(screen, gun, bullets):
    '''функция-обработчик событий'''
    # обрабатываю события действия пользователя
    # получаю все события пользователя
    for event in pygame.event.get():
        # если пришло события закрытия - закрыл окно через sys.exit()
        if event.type == pygame.QUIT:
            sys.exit()

        # программирование клавиш
        elif event.type == pygame.KEYDOWN:
            # проверяю, какая клавиша нажата
            # клавиша вправо D
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.mright = True

             # клавиша влево A
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.mleft = True

            # пробел или кнопка вверх для стрельбы
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                # по нажатию создаётся пуля и добавляется в контейнер bullets
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            # проверяю, какая клавиша нажата
            # клавиша вправо D
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                gun.mright = False

            # клавиша влево A
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                gun.mleft = False


def update(bg_color, screen, stats, scores, gun, aliens, bullets):
    # цвет заливки окна
    screen.fill(bg_color)
    scores.show_score()
    # показываем пули. Метод sprite вернёт все спрайты из контейнера
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # отрисовка пушки
    gun.output()
    # отрисовка инопланетянина
    aliens.draw(screen)
    # отрисовка "последнего" экрана игры
    pygame.display.flip()


def update_bullets(screen, stats, scores, aliens, bullets):
    '''обновление позиции пуль. Это нужно для того, чтобы не жралась память,
    т.к. пули никуда не деваются при выстреле, а у них бесконечно уменьшается позиция
    на 1 пиксель'''
    # обновление пули
    bullets.update()
    for bullet in bullets.copy():
        # проверка, что пуля достигла края экрана
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # проверяет коллизию, т.е. когда один спрайт пересекается с другим спрайтом
    # передаю пулю, пришельцев и True, True для того, чтобы проверить, что между ними
    # колиззия и будет удалять И пуля, И пришелец
    # при пересечении, создастся словарь с ключом пули и значением пришельца
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        # цикл нужен для того, чтобы очки учитывались адекватно при убийстве нескольких
        # пришельцев одной пулей
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)
        scores.image_score()
        check_high_score(stats, scores)
        scores.image_lives()

    # если кончились пришельцы
    if len(aliens) == 0:
        bullets.empty()
        create_alien_army(screen, aliens)


def gun_kill(stats, screen, scores, gun, aliens, bullets):
    '''столкновение пушки и пришельцев'''

    if stats.lives > 0:
        # если кол-во жизней больше нуля
        stats.lives -= 1
        scores.image_lives()
        # очистил группу с пришельцами и пулями при столкновении
        aliens.empty()
        bullets.empty()
        # затем нужно заново создать армию
        create_alien_army(screen, aliens)
        # обнуление очков после смерти
        # stats.score = 0
        # создаёт новую пушку
        gun.create_gun()
    else:
        # если равен нулю - переключаю на фолс и закрытие игры
        stats.run_game = False
        sys.exit()

    # модуль time здесь нужен для того, чтобы указать, сколько перезагрузка будет идти
    time.sleep(2)  # 2 сек


def update_aliens_position(stats, screen, scores, gun, aliens, bullets):
    '''обновляет позицию инопланетян'''
    aliens.update()

    # так же проверяет коллизию
    if pygame.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, scores, gun, aliens, bullets)

    # и проверил не дошли ли пришельцы до края экрана
    aliens_passed(stats, screen, scores, gun, aliens, bullets)


def aliens_passed(stats, screen, scores, gun, aliens, bullets):
    '''проверка, дошли ли пришельцы до края экрана'''
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, scores, gun, aliens, bullets)
            break


def create_alien_army(screen, aliens):
    '''создание армии пришельцев'''
    # сначала создаю 1 пришельца
    alien = Alien(screen)
    alien_width = alien.rect.width
    alien_height = alien.rect.height
    # ширина экрана - двойная ширина пришельца делённая на ширину пришельца
    aliens_amount_x = int((700 - 2 * alien_width) / alien_width)
    # высота рядов
    aliens_amount_y = int((800 - 100 - 2 * alien_height) / alien_height)

    for alien_row in range(aliens_amount_y - 1):
        for alien_number in range(aliens_amount_x):
            alien = Alien(screen)
            alien.x = alien_width + alien_width * alien_number
            alien.rect.x = alien.x
            alien.y = alien_height + alien_height * alien_row
            alien.rect.y = alien.rect.height + alien.rect.height * alien_row - alien_height
            aliens.add(alien)


def check_high_score(stats, scores):
    '''проверка новых рекордов'''
    # проверка, если текущий счёт больше рекорда
    # то текущий счёт записывает в рекорд
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        with open('highscore.txt', 'w') as file:
            file.write(str(stats.high_score))
        # и отрисовал новый рекорд
        scores.image_high_score()
