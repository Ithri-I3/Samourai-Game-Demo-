import pygame


class Player:
    def __init__(self):
        self.actual_hp = 100
        self.total_hp = 100
        self.attack = 10
        self.speed = 2
        self.jump = 50
        self.image = pygame.transform.scale(pygame.image.load('ninja origin.png'), (110, 123))

    def move_animation(self):
        image1 = pygame.transform.scale(pygame.image.load('test1.png'), (110, 123))
        image2 = pygame.transform.scale(pygame.image.load('ninja2.png'), (90, 123))
        image3 = pygame.transform.scale(pygame.image.load('ninja3.png'), (96, 123))
        image4 = pygame.transform.scale(pygame.image.load('ninja4.png'), (96, 123))
        image5 = pygame.transform.scale(pygame.image.load('addi.png'), (120, 123))
        image6 = pygame.transform.scale(pygame.image.load('ninja6.png'), (96, 123))

        img_list = [image1, image2, image3, image4, image5, image6]
        return img_list












