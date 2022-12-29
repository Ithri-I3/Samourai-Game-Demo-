import pygame
import time
import player
import samourai


def air_state(max_y, ground):
    global y
    global flying_autorisation_for_keyboard
    global can_fly
    if y > max_y and can_fly:
        if flying_autorisation_for_keyboard:
            y -= 1
    else:
        can_fly = False
        if y < ground:
            y += 1
        elif y == ground:
            flying_autorisation_for_keyboard = False
            can_fly = True


pygame.init()
icon = pygame.image.load('iconne.png')
pygame.display.set_caption("The Samurai")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((1080, 620))
background = pygame.image.load('bgg.png')
player = samourai.Samourai()
ground = 500
player_coor = pygame.Rect(0, ground, 35, 43)
gravity = 1
flying_autorisation_for_keyboard = False
can_fly = False
game_running = True
moving = False
to_left = False
attacking = False
left_attack = False
heavy_attack = False
x = player_coor.x
y = player_coor.y
anim_list = player.move_animation()
static_list = player.static_animation()
left_attack_list = player.left_attack_animation()
right_attack_list = player.right_attack_animation()
heavy_attack_list = player.heavy_attack_animation()
i = 0
j = 0
k = 0
p = 0
h = 0
while game_running:
    pygame.display.flip()
    clock = pygame.time.Clock()
    screen.blit(background, (0, 0))
    air_state(ground - player.jump, ground)
    if not moving and not attacking:
        if j > 5:
            j = 0
        try:
            screen.blit(static_list[j], (x, y))
        except TypeError:
            screen.blit(static_list[int(j)], (x, y))
        j += 0.04
    elif not attacking:
        if i > 5:
            i = 0
        if to_left:
            screen.blit(pygame.transform.flip(anim_list[i], True, False), (x, y))
        else:
          screen.blit(anim_list[i], (x, y))
          #clock.tick(1)
        i += 1
    else:
        if not heavy_attack:
            if left_attack:
                if to_left:
                    if k > 3:
                        k = 0
                        attacking = False
                    try:
                        screen.blit(pygame.transform.flip(left_attack_list[k], True, False), (x, y))
                    except TypeError:
                        screen.blit(pygame.transform.flip(left_attack_list[int(k)], True, False), (x, y))
                    k += 0.04
                else :
                    if k > 3:
                        k = 0
                        attacking = False
                    try:
                        screen.blit(left_attack_list[k], (x, y))
                    except TypeError:
                        screen.blit(left_attack_list[int(k)], (x, y))
                    k += 0.04
            else :
                if to_left:
                    if p > 5:
                        p = 0
                        attacking = False
                    try:
                        screen.blit(pygame.transform.flip(right_attack_list[p], True, False), (x, y))
                    except TypeError:
                        screen.blit(pygame.transform.flip(right_attack_list[int(p)], True, False), (x, y))
                    p += 0.04
                else:
                    if p > 5:
                        p = 0
                        attacking = False
                    try:
                        screen.blit(right_attack_list[p], (x, y))
                    except TypeError:
                        screen.blit(right_attack_list[int(p)], (x, y))
                    p += 0.04
                    #clock.tick(1)
        else:
            if to_left:
                if h > 6:
                    h = 0
                    attacking = False
                try:
                    screen.blit(pygame.transform.flip(heavy_attack_list[h], True, False), (x, y))
                except TypeError:
                    screen.blit(pygame.transform.flip(heavy_attack_list[int(h)], True, False), (x, y))
                h += 0.04
            else:
                if h > 6:
                    h = 0
                    attacking = False
                try:
                    screen.blit(heavy_attack_list[h], (x, y))
                except TypeError:
                    screen.blit(heavy_attack_list[int(h)], (x, y))
                h += 0.04

    moving = False
    touched_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if flying_autorisation_for_keyboard == False:
                if event.key == pygame.K_SPACE:
                    flying_autorisation_for_keyboard = True
                    can_fly = True
            if not attacking:
                if event.key == pygame.K_a:
                    attacking = True
                    heavy_attack = True
    if touched_keys[pygame.K_d] and x < 1050-player_coor.width:
        moving = True
        to_left = False
        x += player.speed
    if touched_keys[pygame.K_q] and x > 0:
        moving = True
        to_left = True
        x -= player.speed
    if not attacking:
        if pygame.mouse.get_pressed()[0]:
            attacking = True
            left_attack = True
            heavy_attack = False
        if pygame.mouse.get_pressed()[2]:
            attacking = True
            left_attack = False
            heavy_attack = False
    clock.tick(200)

