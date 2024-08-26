import math
import pygame
import sys
import random
from config import *
from functions import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
bg = pygame.image.load("img/bg2.png")

class Up_grade:
    def __init__(self, x, y, img_path, w, h):
        self.rect = pygame.Rect(x, y, 20, 20)
        img_orig = pygame.transform.scale(pygame.image.load(img_path), (w, h))
        self.img = pygame.transform.scale(img_orig, (w, h))
        self.disposable = True
        self.img_path = img_path
        self.speed_y = 0
        self.speed_x = 0
    
    def draw(self):
        global player_hp
        global last_d_time
        global lvlbullets
        if self.disposable == True:
            screen.blit(self.img, self.rect)
            if self.img_path == "img/kit.png":    
                if player.collide(kits[0]):
                    self.disposable = False
                    player_hp += 20
            elif self.img_path == "img/speed_up.png":    
                if player.collide(kits[1]):
                    player.img = pygame.image.load("img/fast.png")
                    player.img = pygame.transform.scale(player.img, (25, 41))
                    self.disposable = False
                    self.speed_x = 5
                    self.speed_y = 5
            elif self.img_path == "img/Ammunition_box.png":
                if player.collide(kits[2]):
                    self.disposable = False
                    lvlbullets += 3

object1 = Foreign_Objects(19, 100, 30, 30, "img/torch.png")
object3 = Foreign_Objects(19, 200, 30, 30, "img/torch.png")
object5 = Foreign_Objects(19, 300, 30, 30, "img/torch.png")
object7 = Foreign_Objects(19, 400, 30, 30, "img/torch.png")

object4 = Foreign_Objects(451, 100, 30, 30, "img/torch2.png")
object6 = Foreign_Objects(451, 200, 30, 30, "img/torch2.png")
object8 = Foreign_Objects(451, 300, 30, 30, "img/torch2.png")

object2 = Foreign_Objects(450, 390, 30, 45, "img/torch1.png")

hide_object1 = Place_to_hide(200, 30, 50, 50, "img/Arm_Chair.png", "img/hide.png")
hide_object2 = Place_to_hide(400, 250, 50, 50, "img/Arm_Chair.png", "img/hide.png")
hide_object3 = Place_to_hide(430, 220, 50, 50, "img/Arm_Chair.png", "img/hide.png")

object9 = Foreign_Objects(190, 210, 30, 30, "img/locker.png")
object10 = Foreign_Objects(200, 350, 50, 50, "img/boxes.png")
object11 = Foreign_Objects(390, 20, 50, 50, "img/wooden box.png")
object12 = Foreign_Objects(275, 180, 50, 60, "img/wardrobe.png")
object13 = Foreign_Objects(250, 390, 50, 50, "img/boxes.png")
object14 = Foreign_Objects(200, 100, 50, 50, "img/boxes.png")
object15 = Foreign_Objects(180, 390, 50, 50, "img/boxes.png")
object16 = Foreign_Objects(230, 410, 70, 70, "img/boxes.png")
object17 = Foreign_Objects(20, 450, 30, 30, "img/locker.png")
object18 = Foreign_Objects(420, 60, 50, 50, "img/boxes.png")
object19 = Foreign_Objects(140, 20, 50, 60, "img/wardrobe.png")

enemy1 = Enemy(20, 20, 60, 80, "img/Enemy1.png", "horiz", 430, 10, 3)
enemy2 = Enemy(400, 20, 40, 60, "img/Enemy2.png", "vert", 400, 10, 1)
enemy3 = Enemy(20, 410, 50, 70, "img/Enemy3.png", "horiz", 430, 13, 6)
enemy4 = Enemy(250, 150, 40, 55, "img/Enemy4.png", "vert", 450, 10, 10)
enemy5 = Enemy(20, 430, 50, 60, "img/Enemy5.png", "horiz", 430, 5, 7)
enemy6 = Enemy(400, 20, 40, 60, "img/Enemy6.png", "vert", 400, 5, 3)
enemy7 = Enemy(260, 20, 35, 50, "img/Enemy7.png", "vert", 450, 5, 10)
enemy8 = Enemy(20, 430, 50, 60, "img/Enemy8.png", "horiz", 430, 5, 10)
enemy9 = Enemy(400, 20, 60, 90, "img/Enemy9.png", "vert", 400, 5, 10)
enemy10 = Enemy(130, 20, 200, 230, "img/Enemy10.png", "vert", 270, 10, 100)

barbed_wire1 = Enemy(260, 300, 60, 60, "img/barbed_wire.png", "vert", 2000, 0, 1000)
barbed_wire2 = Enemy(320, 100, 60, 200, "img/barbed_wire1.png", "vert", 2000, 0, 1000)
barbed_wire3 = Enemy(260, 60, 20, 20, "img/barbed_wire.png", "vert", 2000, 0, 1000)
barbed_wire4 = Enemy(160, 360, 40, 20, "img/barbed_wire.png", "vert", 2000, 0, 1000)
barbed_wire5 = Enemy(60, 120, 20, 40, "img/barbed_wire1.png", "vert", 2000, 0, 1000)
barbed_wire6 = Enemy(260, 60, 20, 20, "img/barbed_wire.png", "vert", 2000, 0, 1000)

aid_kit1 = Up_grade(440, 20, "img/kit.png", 40, 35)
aid_kit2 = Up_grade(80, 460, "img/speed_up.png", 20, 20)
aid_kit3 = Up_grade(400, 200, "img/Ammunition_box.png", 35, 40)

max_money = Enemy(0, 10, 166, 250, "img/max_money.png", "vert", 2000, 0, 100)
max_power = Enemy(167, 10, 166, 250, "img/max_power.png", "vert", 2000, 0, 100)
max_bullet = Enemy(334, 10, 166, 250, "img/max_bullet.png", "vert", 2000, 0, 100)
coin_draw = Enemy(0, 270, 50, 50, "img/coin.png", "vert", 2000, 0, 100)
play = Enemy(168, 330, 150, 165, "img/play.png", "vert", 2000, 0, 100)
menu = Enemy(460, 0, 20, 20, "img/menu.png", "vert", 2000, 0, 100)
continue1 = Enemy(100, 300, 300, 100, "img/continue.png", "vert", 2000, 0, 100)
stop2 = Enemy(430, 0, 20, 20, "img/Stop.png", "vert", 2000, 0, 100)
exit1 = Enemy(100, 0, 300, 200, "img/exit.png", "vert", 2000, 0, 100)

lvl1enemies = [enemy1, enemy2, enemy3, barbed_wire1]
lvl2enemies = [enemy4, enemy5, enemy6, barbed_wire2]
lvl3enemies = [enemy7, enemy8, enemy9, barbed_wire3, barbed_wire4, barbed_wire5, barbed_wire6]
lvl4enemies = [enemy7, enemy8, enemy9, enemy1]
lvl5enemies = [enemy1, enemy2, enemy3, enemy4, enemy5]
lvl6enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6]
lvl7enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7]
lvl8enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8]
lvl9enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9]
lvl10enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10]

lvlenemies = [lvl1enemies, lvl2enemies, lvl3enemies, lvl4enemies, lvl5enemies, lvl6enemies, lvl7enemies, lvl8enemies, lvl9enemies, lvl10enemies]

kits = [aid_kit1, aid_kit2, aid_kit3]

interaction_obj1 = [hide_object1]
interaction_obj2 = [hide_object2]
interaction_obj3 = [hide_object3]
interaction_obj4 = [hide_object1]
interaction_obj5 = [hide_object1]
interaction_obj6 = [hide_object1]
interaction_obj7 = [hide_object1]
interaction_obj8 = [hide_object1]
interaction_obj9 = [hide_object1]
interaction_obj10 = [hide_object1]


interaction_objects = [interaction_obj1, interaction_obj2, interaction_obj3, interaction_obj4, interaction_obj5, interaction_obj6, interaction_obj7, interaction_obj8, interaction_obj9, interaction_obj10]

def reset_enemy():
    global lvl1enemies, lvl2enemies, lvl3enemies, lvl4enemies, lvl5enemies, lvl6enemies, lvl7enemies, lvl8enemies, lvl9enemies, lvl10enemies, lvlenemies
    enemy1 = Enemy(20, 20, 60, 80, "img/Enemy1.png", "horiz", 430, 10, 3)
    enemy2 = Enemy(400, 20, 40, 60, "img/Enemy2.png", "vert", 400, 10, 1)
    enemy3 = Enemy(20, 410, 50, 70, "img/Enemy3.png", "horiz", 430, 13, 6)
    enemy4 = Enemy(250, 150, 40, 55, "img/Enemy4.png", "vert", 450, 10, 10)
    enemy5 = Enemy(20, 430, 50, 60, "img/Enemy5.png", "horiz", 430, 5, 7)
    enemy6 = Enemy(400, 20, 40, 60, "img/Enemy6.png", "vert", 400, 5, 3)
    enemy7 = Enemy(260, 20, 35, 50, "img/Enemy7.png", "vert", 450, 5, 10)
    enemy8 = Enemy(20, 430, 50, 60, "img/Enemy8.png", "horiz", 430, 5, 10)
    enemy9 = Enemy(400, 20, 60, 90, "img/Enemy9.png", "vert", 400, 5, 10)
    enemy10 = Enemy(130, 20, 200, 230, "img/Enemy10.png", "vert", 270, 10, 100)

    barbed_wire1 = Enemy(260, 300, 60, 60, "img/barbed_wire.png", "vert", 2000, 0, 1000)
    barbed_wire2 = Enemy(320, 100, 60, 200, "img/barbed_wire1.png", "vert", 2000, 0, 1000)
    barbed_wire3 = Enemy(260, 60, 20, 20, "img/barbed_wire.png", "vert", 2000, 0, 1000)
    barbed_wire4 = Enemy(160, 360, 40, 20, "img/barbed_wire.png", "vert", 2000, 0, 1000)
    barbed_wire5 = Enemy(60, 120, 20, 40, "img/barbed_wire1.png", "vert", 2000, 0, 1000)
    barbed_wire6 = Enemy(260, 60, 20, 20, "img/barbed_wire.png", "vert", 2000, 0, 1000)

    lvl1enemies = [enemy1, enemy2, enemy3, barbed_wire1]
    lvl2enemies = [enemy4, enemy5, enemy6, barbed_wire2]
    lvl3enemies = [enemy7, enemy8, enemy9, barbed_wire3, barbed_wire4, barbed_wire5, barbed_wire6]
    lvl4enemies = [enemy7, enemy8, enemy9, enemy1]
    lvl5enemies = [enemy1, enemy2, enemy3, enemy4, enemy5]
    lvl6enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6]
    lvl7enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7]
    lvl8enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8]
    lvl9enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9]
    lvl10enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10]
    lvlenemies = [lvl1enemies, lvl2enemies, lvl3enemies, lvl4enemies, lvl5enemies, lvl6enemies, lvl7enemies, lvl8enemies, lvl9enemies, lvl10enemies]

lvl1objects = [object1, object2, object3, object4, object5, object6, object7, object8, object9, object10, object12, object13, object14, object15, object16]
lvl2objects = [object1, object2, object3, object5, object7, object4, object6, object8, object19, object18, object17]
lvl3objects = [object11, object17, object18]
lvl4objects = []
lvl5objects = []
lvl6objects = []
lvl7objects = []
lvl8objects = []
lvl9objects = []
lvl10objects = []

lvlobjects = [lvl1objects, lvl2objects, lvl3objects, lvl4objects, lvl5objects, lvl6objects, lvl7objects, lvl8objects, lvl9objects, lvl10objects]

player_skins = ["img/player.png", "img/player1.png", "img/player2.png", "img/player3.png", "img/player4.png", "img/player5.png"]
time_skin = 0

for file in maps:
    with open(file, "r") as map:
        row = 0
        col = 0
        for line in map.read().split('\n'):
            x = list(line)
            col = 0
            for i in x:
                if i == "1":
                    walls[maps.index(file)].append(Wall(col * 20, row * 20, 20, 20, walls_img[random.randint(0, len(walls_img)-1)]))
                col += 1
            row += 1

player = Player(20, 20, 25, 40, player_skins[time_skin], lvl1walls, lvl1objects, interaction_obj1)

while True:
    current_time = pygame.time.get_ticks()
    
    if game_state == 0:
        screen.fill((25, 255, 225))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                with open("assets/statistics.txt", "w") as stat:
                    stat.write(f"{number_of_bullets}\n{bullet_damage}\n{number_of_upgrades}\n{expenses}\n{price_m1}\n{price_p2}\n{price_b3}")
                sys.exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    if max_money.rect.collidepoint(pygame.mouse.get_pos()) and cash >= price_m1:
                        expenses += price_m1
                        cash -= price_m1
                        random_money += 10
                        price_m1 *= 1.5
                        price_m1 = math.ceil(price_m1)
                        number_of_upgrades += 1
                    elif max_power.rect.collidepoint(pygame.mouse.get_pos()) and cash >= price_p2:
                        expenses += price_p2
                        cash -= price_p2
                        power_bul += 1
                        price_p2 *= 1.5
                        price_p2 = math.ceil(price_p2)
                        bullet_damage += 1
                    elif max_bullet.rect.collidepoint(pygame.mouse.get_pos()) and cash >= price_b3:
                        expenses += price_b3
                        cash -= price_b3
                        lvlbullets += 1
                        price_b3 *= 2
                        price_b3 = math.ceil(price_b3)
                        number_of_bullets += 1
                    elif play.rect.collidepoint(pygame.mouse.get_pos()):
                        game_state = 1   

        play.draw()
        coin_draw.draw()
        max_money.draw()
        max_power.draw()   
        max_bullet.draw()
        money_print(cash)
        statistics_print(bullet_damage, number_of_bullets, number_of_upgrades, price_m1, price_p2, price_b3, color)

    elif game_state == 2:
        screen.fill((25, 255, 225))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    if continue1.rect.collidepoint(pygame.mouse.get_pos()):
                        game_state = 1
                    elif exit1.rect.collidepoint(pygame.mouse.get_pos()):
                        game_state = 0
                        level = 1
                        player_hp = 100          
                        reset_enemy()

        exit1.draw()            
        continue1.draw()

    elif game_state == 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                with open("assets/statistics.txt", "w") as stat:
                    stat.write(f"{number_of_bullets}\n{bullet_damage}\n{number_of_upgrades}\n{expenses}\n{price_m1}\n{price_p2}\n{price_b3}")
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_a:
                    player.x_speed = -5 - aid_kit2.speed_x
                elif e.key == pygame.K_w:
                    player.y_speed = -5 - aid_kit2.speed_y
                elif e.key == pygame.K_d:
                    player.x_speed = 5 + aid_kit2.speed_x
                elif e.key == pygame.K_s:
                    player.y_speed = 5 + aid_kit2.speed_y
                elif e.key == pygame.K_h:        
                    for i in player.interact_obj:
                        if player.collide(i):
                            hide = not hide   
                elif e.key == pygame.K_LEFT:
                    if time_skin > 0:
                        time_skin -= 1
                    else:
                        time_skin = len(player_skins) - 1
                    player.img = pygame.transform.scale(pygame.image.load(player_skins[time_skin]), (player.rect.width, player.rect.height))

                elif e.key == pygame.K_RIGHT:
                    if time_skin < len(player_skins) - 1:
                        time_skin += 1
                    else:
                        time_skin = 0
                    player.img = pygame.transform.scale(pygame.image.load(player_skins[time_skin]), (player.rect.width, player.rect.height))
                
            elif e.type == pygame.KEYUP:
                if e.key == pygame.K_a or e.key == pygame.K_d:
                    player.x_speed = 0
                elif e.key == pygame.K_s or e.key == pygame.K_w:
                    player.y_speed = 0
            
            elif e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 1:
                    if menu.rect.collidepoint(pygame.mouse.get_pos()):
                        game_state = 0
                    elif stop2.rect.collidepoint(pygame.mouse.get_pos()):
                        game_state = 2
                    elif hide == False and lvlbullets > quantity:
                        bullet = Bullet(player.rect.centerx, player.rect.centery, 5, 20, "img/bullet.png", e.pos)
                        bullets.append(bullet)
                        quantity += 1

        draw_bg()

        for interac in interaction_objects[level-1]:
            interac.draw(hide)
        
        for e in kits:
            e.draw()
        
        for wall in walls[level-1]:
            wall.draw()

        for obj in lvlobjects[level-1]:
            obj.draw()

        for enemy in lvlenemies[level-1]:
            for bullet in bullets:
                if bullet.collide(enemy):
                    enemy.hp -= power_bul
                    if enemy.hp <= 0:
                        lvlenemies[level-1].remove(enemy)
                    bullets.remove(bullet)
                    break     
            if hide == False:
                if player.collide(enemy):
                    if current_time - last_d_time > invisible_time:
                        player_hp -= enemy.damage
                        player.rect.x = 20
                        player.rect.y = 20
                        last_d_time = current_time
            enemy.draw()
            enemy.move()

        player.walls = walls[level-1]
        player.objects = lvlobjects[level-1]
        player.interact_obj = interaction_objects[level-1]

        for bullet in bullets:
            if bullet.rect.x >= 500 or bullet.rect.y >= 500:
                bullets.remove(bullet)
                break

        if player.rect.x >= 500 or player.rect.y >= 500:
            with open("assets/money.txt", "a") as money:
                money.write(f"\n{random.randint(1, random_money)}")
            with open("assets/money.txt", "r") as money:
                wallot = list(money.read().split('\n'))
                cash += int(wallot[-1])
                  
            interaction_objects[level-1].clear()
            player_hp = 100
            level += 1
            player.img = pygame.image.load("img/player.png")
            player.img = pygame.transform.scale(player.img, (25, 40))
            for ki in kits:
                ki.speed_x, ki.speed_y = 0, 0
                ki.disposable = True
            for foe in lvlenemies:
                for q in foe:
                    q.hp += 5
            quantity = 0

            player.rect.x, player.rect.y = 20, 20

        for bullet in bullets:
            bullet.draw()
            bullet.move()
        
        if hide == False:   
            if player_hp > 0:
                player.draw()
                player.move()
        
        for wall in player.walls:
            for bullet in bullets:
                if bullet.collide(wall):
                    bullets.remove(bullet)
                    break
        
        for obj in player.objects:
            for bullet in bullets:
                if bullet.collide(obj):
                    bullets.remove(bullet)
                    break
        
        if player_hp <= 0:
            game_over()
        for i in range(0, player_hp, 20):
            life = HP(260 + i, 0, 20, 20, "img/hard.png")
            life.draw()
        menu.draw()
        stop2.draw()
        draw_bullets_info(lvlbullets, quantity, level)
        play_hp()
        
    pygame.display.update()
    clock.tick(60)