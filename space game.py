import pygame, controls
import sys
from spacecraft import Spacecraft

# Конструкция def определяет функцию(блок где пишется некоторое количество запросов, после чего можно будет
# обращаться к ней несколько раз)
def run():
    # команда инициализации игры
    pygame.init()
    # Отображаемая област, где будут все графические элементы игры
    screen = pygame.display.set_mode((700, 750))
    # Заголовок для графической окна
    pygame.display.set_caption("Инопланетный взрыв")
    # Фоновый цвет для дисплея в RGB
    bg_color = (102, 102, 102)
    # Отрисовка корабля на экране
    spacecraft = Spacecraft(screen)
    # Создание контейнера с пулями
    bullets = pygame.sprite.Group()

    # Главный цикл игры
    while True:

        # Вызвать из файла controls функцию events
        controls.events(screen, bullets, spacecraft)
        # Вызвать из файла spacecraft функцию логической переменной
        spacecraft.update_spacecraft()
        # Вызвать из файла bullet функцию update
        bullets.update()
        # Вызвать из файла controls функцию update
        controls.update(bg_color, screen, spacecraft, bullets)




run()
