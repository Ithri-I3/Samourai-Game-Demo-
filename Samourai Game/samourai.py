import pygame

class Samourai:
    def __init__(self):
        self.actual_hp = 100
        self.total_hp = 100
        self.attack = 10
        self.speed = 2
        self.jump = 50
        self.image = pygame.transform.scale(pygame.image.load('player origin.png'), (65, 80))
        self.attack_img = pygame.transform.scale(pygame.image.load('attack0.png'), (120, 80))

    def move_animation(self):
        image1 = pygame.transform.scale(pygame.image.load('move1.png'), (65, 80))
        image2 = pygame.transform.scale(pygame.image.load('move2.png'), (65, 80))
        image3 = pygame.transform.scale(pygame.image.load('move3.png'), (65, 80))
        image4 = pygame.transform.scale(pygame.image.load('move4.png'), (65, 80))
        image5 = pygame.transform.scale(pygame.image.load('move5.png'), (65, 80))
        image6 = pygame.transform.scale(pygame.image.load('move6.png'), (65, 80))
        move_list = [image1, image2, image3, image4, image5, image6]
        return move_list
    def static_animation(self):
        img1 = pygame.transform.scale(pygame.image.load('static1.png'), (65, 80))
        img2 = pygame.transform.scale(pygame.image.load('static2.png'), (65, 80))
        img3 = pygame.transform.scale(pygame.image.load('static3.png'), (65, 80))
        img4 = pygame.transform.scale(pygame.image.load('static4.png'), (65, 80))
        img5 = pygame.transform.scale(pygame.image.load('static5.png'), (65, 80))
        static_list = [self.image, img1, img2, img3, img4, img5]
        return static_list
    def left_attack_animation(self):
        im1 = pygame.transform.scale(pygame.image.load('downattack1.png'), (120, 120))
        im2 = pygame.transform.scale(pygame.image.load('downattack2.png'), (65, 80))
        im3 = pygame.transform.scale(pygame.image.load('downattack3.png'), (65, 80))
        left_attack_list = [self.attack_img, im1, im2, im3]
        return left_attack_list
    def right_attack_animation(self):
        imm1 = pygame.transform.scale(pygame.image.load('upattack1.png'), (125, 125))
        imm2 = pygame.transform.scale(pygame.image.load('upattack2.png'), (135, 135))
        imm3 = pygame.transform.scale(pygame.image.load('upattack3.png'), (135, 135))
        imm4 = pygame.transform.scale(pygame.image.load('upattack4.png'), (135, 135))
        imm5 = pygame.transform.scale(pygame.image.load('upattack5.png'), (135, 135))
        right_attack_list = [self.attack_img, imm1, imm2, imm3, imm4, imm5]
        return right_attack_list
    def heavy_attack_animation(self):
        ig1 = pygame.transform.scale(pygame.image.load('slamattack1.png'), (110, 80))
        ig2 = pygame.transform.scale(pygame.image.load('slamattack2.png'), (110, 80))
        ig3 = pygame.transform.scale(pygame.image.load('slamattack3.png'), (300, 86))
        ig4 = pygame.transform.scale(pygame.image.load('slamattack4.png'), (110, 80))
        ig5 = pygame.transform.scale(pygame.image.load('slamattack5.png'), (110, 80))
        ig6 = pygame.transform.scale(pygame.image.load('slamattack6.png'), (110, 80))
        heavy_attack_list = [self.attack_img, ig1, ig2, ig3, ig4, ig5, ig6]
        return heavy_attack_list
