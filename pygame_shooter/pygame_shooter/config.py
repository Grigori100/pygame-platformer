import pygame, random

pygame.init()

WIDTH, HEIGHT = 500, 500
player_hp = 100
hide = False
taken_dam = False
last_d_time = 0
invisible_time = 500
enemies = []
random_money = 10

price_m1 = 30
price_p2 = 150
price_b3 = 20
expenses = 0
power_bul = 1

lvlbullets = 0
kits = []

number_of_bullets = 0
bullet_damage = 0
number_of_upgrades = 0

with open("assets/statistics.txt", "r") as stat:
    statistics_list = list(stat.read().split("\n"))
    number_of_bullets = int(statistics_list[0])
    bullet_damage = int(statistics_list[1])
    number_of_upgrades = int(statistics_list[2])
    expenses = int(statistics_list[3])
    price_m1 = int(statistics_list[4])
    price_p2 = int(statistics_list[5])
    price_b3 = int(statistics_list[6])

random_money = (10 * number_of_upgrades) + 10
power_bul = bullet_damage + 1
lvlbullets = number_of_bullets

quantity = 0
game_state = 0

lvl1walls = []
lvl2walls = []
lvl3walls = []
lvl4walls = []
lvl5walls = []
lvl6walls = []
lvl7walls = []
lvl8walls = []
lvl9walls = []
lvl10walls = []

walls = [lvl1walls, lvl2walls, lvl3walls, lvl4walls, lvl5walls, lvl6walls, lvl7walls, lvl8walls, lvl9walls, lvl10walls]

level = 1
bullets = []

maps = ["assets/map.txt", "assets/map1.txt", "assets/map2.txt", "assets/map3.txt", "assets/map4.txt", "assets/map5.txt", "assets/map6.txt", "assets/map7.txt", "assets/map8.txt", "assets/map9.txt"]

walls_img = ["img/wall.png", "img/wall1.png", "img/wall2.png", "img/wall3.png", "img/wall4.png"]

cash = 0

with open("assets/money.txt", "r") as money:
        for coin in list(money.read().split("\n")):
            cash += int(coin)
cash -= expenses

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

exited = False