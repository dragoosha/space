# Все, что касается коробля: передвижение, прорисовка - отдельный пайтон файл

import pygame

# Собираем логику корабли в один класс
class Spacecraft():

    # Метод ее инициализации + изображение
    def __init__(self, screen):

        # Придать кораблю образ
        self.screen = screen
        # Загрузка изображения корабля
        self.image = pygame.image.load('images/spacecraft.png')
# Все графические объекты представлены в виде прямоугольнике
        # Получение графического объекта (корабля) в качестве прямоугольника
        self.rect = self.image.get_rect()
        # Получить объект (экран) в качестве прямоугольника
        self.screen_rect = screen.get_rect()
        # Расположение пушки
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        # Создание логической переменной с true and false
        self.mright = False
        self.mleft = False

    # Создание функции, которая будет отрисовывать корабль - вывод на экран
    def output(self):
        self.screen.blit(self.image, self.rect)

    def update_spacecraft(self):
        """Обновление позиции кораблся"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 2.5
        if self.mleft and self.rect.left > self.screen_rect.left:
            self.center += -2.5

        self.rect.centerx = self.center


