import pygame
import sys
from bullet import Bullet

# Парамент spacecraft
def events(screen, spacecraft, bullets):
    """Обработка событий"""
    # Собираем все события пользователя, Клавиша нажата - это событие, клавиша отжата - это тоже событие
    for event in pygame.event.get():
        # Завершение игры
        if event.type == pygame.QUIT:
            sys.exit()
        # Событие нажатия клавиши

        elif event.type == pygame.KEYDOWN:
            # Событие нажатия клавиши D
            if event.key == pygame.K_d:
                # Перемещение объекта(прямоугольника) в право
                spacecraft.mright = True
            # Событие нажатия клавиши А
            elif event.key == pygame.K_a:
                spacecraft.mleft = True
            elif event.key == pygame.K_SPACE:
                # Создание пули на ПРОБЕЛ на основе class Bullet
                new_bullet = Bullet(screen, spacecraft,)
                # Добавление пули в контейнер
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    spacecraft.mright = False
                elif event.key == pygame.K_a:
                    spacecraft.mleft = False
def update(bg_color, screen, spacecraft, bullets):
    """Обновление экрана"""
    # Заливка фона в игре
    screen.fill(bg_color)
    # Отрисовка пуль
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # Отрисовка корабля
    spacecraft.output()
    # Финальный экран
    pygame.display.flip()
