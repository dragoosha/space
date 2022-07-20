import pygame

# Класс pygame.sprite.Sprite встроен в модуль pygame. Sprite - обЪект на экране который может двигаться
class Bullet (pygame.sprite.Sprite):


    def __init__(self, screen, spacecraft):
        """Создание пули в текущей позиции корабля"""
        # У pygame есть class Sprite, class Bullet обращается к class Sprite. Чтобы обратиться к class Sprite без ввода
        # кодов на инициализацию пули, super(Bullet(Sprite))
        super(Bullet).__init__()
        # Загрузка экрана, где будут создаваться пули
        self.screen = screen
        # Отрисовка прямоугольника pygame.rect([координата X], [координата Y],[Ширина {pixel}], [Высота {pixel}])
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = 178, 34, 3
        self.speed = 1.5
        # Пуля должна появляться в верхней части корабли
        self.rect.centerx = spacecraft.rect.centerx
        self.rect.top = spacecraft.rect.top
        # Координата по Y
        self.y = float(self.rect.y)


    def update(self):
        """Пермещение пули вверх"""
        # Координата Y будет уменьшаться на заданную скорость
        self.y -= self.speed
        # Обновление позиции прямоугольника
        self.rect.y = self.y

    def draw_bullet(self):
        """Рисуем пулю на экране"""
        pygame.draw.rect(self.screen, self.color, self.rect)