from csv import reader
from os import walk
import pygame

WIDTH = 1280
HEIGHT = 720
FPS = 60
TILESIZE = 64
HITBOX_OFFSET = {
    'player': -26,
    'object': -40,
    'grass': -10,
    'invisible': 0}

# ui 
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../SOFTWARE/Helga/graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# weapons 
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15, 'graphic': '../SOFTWARE/Helga/graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 10, 'damage': 100, 'graphic': '../SOFTWARE/Helga/graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'graphic': '../SOFTWARE/Helga/graphics/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'graphic': '../SOFTWARE/Helga/graphics/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'graphic': '../SOFTWARE/Helga/graphics/weapons/sai/full.png'}}

# magic
magic_data = {
    'flame': {'strength': 5, 'cost': 20, 'graphic': '../SOFTWARE/Helga/graphics/particles/flame/fire.png'},
    'heal': {'strength': 20, 'cost': 10, 'graphic': '../SOFTWARE/Helga/graphics/particles/heal/heal.png'}}

# enemy
monster_data = {
    'squid': {
        'health': 75,
        'exp': 20,
        'damage': 5,
        'attack_type': 'slash',
        'attack_sound': '../SOFTWARE/Helga/audio/attack/slash.wav',
        'speed': 2,
        'resistance': 3,
        'attack_radius': 80,
        'notice_radius': 200,
        'attack_cooldown': 500,
        'invincibility_duration': 300,
        'respawn_time': 7000,
        'animation_speed': 0.15
    },
    'raccoon': {
        'health': 800,
        'exp': 250,
        'damage': 40,
        'attack_type': 'claw',
        'attack_sound': '../SOFTWARE/Helga/audio/attack/claw.wav',
        'speed': 1,
        'resistance': 4,
        'attack_radius': 100,
        'notice_radius': 500,
        'attack_cooldown': 800,
        'invincibility_duration': 600,
        'respawn_time': 15000,
        'animation_speed': 0.1
    },
    'spirit': {
        'health': 30,
        'exp': 5,
        'damage':3,
        'attack_type': 'thunder',
        'attack_sound': '../SOFTWARE/Helga/audio/attack/fireball.wav',
        'speed': 3,
        'resistance': 3,
        'attack_radius': 60,
        'notice_radius': 200,
        'attack_cooldown': 300,
        'invincibility_duration': 200,
        'respawn_time': 5000,
        'animation_speed': 0.2
    },
    'bamboo': {
        'health': 50,
        'exp': 10,
        'damage': 2,
        'attack_type': 'leaf_attack',
        'attack_sound': '../SOFTWARE/Helga/audio/attack/slash.wav',
        'speed': 2,
        'resistance': 3,
        'attack_radius': 50,
        'notice_radius': 200,
        'attack_cooldown': 400,
        'invincibility_duration': 300,
        'respawn_time': 5000,
        'animation_speed': 0.25
    }
}

def import_csv_layout(path):
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map


def import_folder(path):
    surface_list = []

    for _, __, img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)

    return surface_list
