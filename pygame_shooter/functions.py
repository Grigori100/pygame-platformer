import math
import pygame
import sys
import random
from config import WIDTH, HEIGHT, hide

screen = pygame.display.set_mode((WIDTH, HEIGHT))
bg = pygame.image.load("img/bg2.png")


class Wall():
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (w, h))

    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

class Player():
    def __init__(self, x, y, w, h, img_path, walls, objects, interact_obj):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (w, h))
        self.x_speed = 0
        self.y_speed = 0
        self.walls = walls
        self.objects = objects
        self.interact_obj = interact_obj

    def move(self):
        if hide == False:
            self.rect.x += self.x_speed
            for wall in self.walls:
                if self.collide(wall):
                    self.rect.x -= self.x_speed
            for obj in self.objects:
                if self.collide(obj):
                    self.rect.x -= self.x_speed
        
            self.rect.y += self.y_speed
            for wall in self.walls:
                if self.collide(wall):
                    self.rect.y -= self.y_speed
            for obj in self.objects:
                if self.collide(obj):
                    self.rect.y -= self.y_speed

    def collide(self, obj):    
        return self.rect.colliderect(obj.rect)

    def draw(self):        
        screen.blit(self.img, (self.rect.x, self.rect.y))

class Foreign_Objects():
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (w, h))
    
    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

class Place_to_hide():
    def __init__(self, x, y, w, h, img_path, hide_img):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (w, h))
        self.hide_img = pygame.image.load(hide_img)
        self.hide_img = pygame.transform.scale(self.hide_img, (w, h))

    def draw(self, hides):
        if hides == True:
            screen.blit(self.hide_img, (self.rect.x, self.rect.y))
        else:
            screen.blit(self.img, (self.rect.x, self.rect.y))

class Enemy():
    def __init__(self, x, y, w, h, img_path, vert_or_horiz, final_coord, speed, hp, damage=20):
        self.rect = pygame.Rect(x, y, w, h)
        self.img = pygame.image.load(img_path)
        self.img = pygame.transform.scale(self.img, (w, h))
        self.x_speed = speed
        self.y_speed = speed
        self.vert_or_horiz = vert_or_horiz
        self.final_coord = final_coord    
        self.initial_coord = 0
        self.hp = hp
        self.damage = damage
        if self.vert_or_horiz == "vert":
            self.initial_coord = self.rect.y
        elif self.vert_or_horiz == "horiz":
            self.initial_coord = self.rect.x

    def move(self):
        if self.vert_or_horiz == "vert":
            if self.y_speed != 0:
                while (self.final_coord - self.rect.y) % self.y_speed != 0:
                    self.final_coord += 1
            self.rect.y += self.y_speed
            if self.rect.y == self.final_coord:
                self.y_speed *= -1
            elif self.rect.y == self.initial_coord:
                self.y_speed = abs(self.y_speed)
        elif self.vert_or_horiz == "horiz":
            if self.y_speed != 0:
                while (self.final_coord - self.rect.x) % self.x_speed != 0:
                    self.final_coord += 1
            self.rect.x += self.x_speed
            if self.rect.x == self.final_coord:
                self.x_speed *= -1
            elif self.rect.x == self.initial_coord:
                self.x_speed = abs(self.x_speed)
        
        
    def draw(self):
        screen.blit(self.img, (self.rect.x, self.rect.y))

class Bullet:
    def __init__(self, x, y, w, h, img_path, mouse):
        self.rect = pygame.Rect(x, y, w, h)
        self.img_orig = pygame.transform.scale(pygame.image.load(img_path), (w, h))
        self.img = pygame.transform.scale(self.img_orig, (w, h))
        self.mouse = mouse
        self.x_speed = 0
        self.y_speed = 0
        self.default_speed = 6
        self.float_x = x
        self.float_y = y
        self.set_speed(mouse)
    
    def set_speed(self, to_point):
        x_from, y_from = self.rect.centerx, self.rect.centery
        x_to, y_to = to_point
        dx = x_to - x_from
        dy = y_to - y_from
        x_speed = round(abs((self.default_speed * dx) / math.sqrt(dx**2 + dy**2)), 3)
        y_speed = round(abs((x_speed * dy) / dx), 3)
        if x_to < x_from:
            x_speed *= -1
        if y_to < y_from:
            y_speed *= -1

        self.x_speed = x_speed
        self.y_speed = y_speed
        self.rotate_to_point(self.mouse)

    def move(self):
        self.float_x += self.x_speed
        self.float_y += self.y_speed
        self.rect.x = round(self.float_x)
        self.rect.y = round(self.float_y)

    def draw(self):
        screen.blit(self.img, self.rect)

    def collide(self, obj):
        return self.rect.colliderect(obj.rect)
    
    def rotate_to_point(self, mouse):
        dx, dy = mouse[0] - self.rect.centerx, mouse[1] - self.rect.centery
        angle = math.degrees(math.atan2(-dy, dx)) - 90
        self.img = pygame.transform.rotate(self.img_orig, angle)
        self.rect = self.img.get_rect(center=self.rect.center)
        self.float_x = self.rect.x
        self.float_y = self.rect.y

class HP:
    def __init__(self, x, y, w, h, img_path):
        self.rect = pygame.Rect(x, y, w, h)
        img_orig = pygame.transform.scale(pygame.image.load(img_path), (w, h))
        self.img = pygame.transform.scale(img_orig, (w, h))    
        
    def draw(self):
        screen.blit(self.img, self.rect)

def draw_bullets_info(lvlbullets, q, level):
    font = pygame.font.SysFont('French Script MT', 24)    
    text = font.render(f'Уровнь {level}: {lvlbullets - q} пули', True, (100, 0, 250), (100, 255, 105))
    screen.blit(text, (20, 1))

def play_hp():
    font = pygame.font.SysFont('French Script MT', 25)    
    text = font.render(f'HP:', True, (255, 0, 0), (60, 25, 25))
    screen.blit(text, (230, 2))

def game_over():
    font = pygame.font.SysFont('Bodoni MT Black', 100)    
    text = font.render(f'Game over', True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    text_width = text.get_width()
    text_height = text.get_height()
    centerx = WIDTH // 2 - (text_width // 2)
    centery = HEIGHT // 2 - (text_height // 2)
    screen.blit(text, (centerx, centery))

def draw_bg():
    bg_width, bg_height = bg.get_size()
    for x in range(0, WIDTH, bg_width):
         for y in range(0, HEIGHT, bg_height):
            screen.blit(bg, (x, y))

def money_print(cash1):
    font = pygame.font.SysFont('Bodoni MT Black', 50)    
    text = font.render(f'x{cash1}', True, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    screen.blit(text, (50, 282))

def statistics_print(b_d1, n_b1, mon1, mon2, b_d2, n_b2, color):
    font = pygame.font.SysFont('Appetite New', 15)
    text1 = font.render(f'Кол-во покупок:{mon1}', True, color)
    text11 = font.render(f'Стоимость:{mon2}', True, color)
    text2 = font.render(f'Кол-во покупок:{b_d1}', True, color)
    text3 = font.render(f'Кол-во покупок:{n_b1}', True, color)
    text22 = font.render(f'Стоимость:{b_d2}', True, color)
    text33 = font.render(f'Стоимость:{n_b2}', True, color)

    screen.blit(text1, (12, 208))
    screen.blit(text2, (179, 208))
    screen.blit(text3, (346, 208))
    screen.blit(text11, (12, 232))
    screen.blit(text22, (179, 232))
    screen.blit(text33, (346, 232))