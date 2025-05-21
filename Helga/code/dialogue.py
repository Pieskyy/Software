import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade
from npc import NPC

class Level:
    def __init__(self, character='player'):
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False
        self.selected_character = character

        # Sprite groups
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()
        self.npc_group = pygame.sprite.GroupSingle()


        # Load map and entities
        self.create_map()

        # UI and other systems
        self.ui = UI()
        self.upgrade = Upgrade(self.player)
        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

        self.current_attack = None

    def create_map(self):
        layouts = {
            'boundary': import_csv_layout('../SOFTWARE/Helga/map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('../SOFTWARE/Helga/map/map_Grass.csv'),
            'object': import_csv_layout('../SOFTWARE/Helga/map/map_Objects.csv'),
            'entities': import_csv_layout('../SOFTWARE/Helga/map/map_Entities.csv')
        }
        graphics = {
            'grass': import_folder('../SOFTWARE/Helga/graphics/Grass'),
            'objects': import_folder('../SOFTWARE/Helga/graphics/objects')
        }

        for style, layout in layouts.items():
            for row_index, row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE

                        if style == 'boundary':
                            Tile((x, y), [self.obstacle_sprites], 'invisible')
                        elif style == 'grass':
                            grass_img = choice(graphics['grass'])
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites], 'grass', grass_img)
                        elif style == 'object':
                            obj_img = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', obj_img)
                        elif style == 'entities':
                            if col == '394':
                                self.player = Player(
                                    (x, y),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic,
                                    character=self.selected_character
                                )
                            elif col == '393':
                                # Add NPC to both groups
                                npc = NPC((x, y), [self.visible_sprites, self.npc_group])
                            else:
                                monster_name = {
                                    '390': 'bamboo',
                                    '391': 'spirit',
                                    '392': 'raccoon'
                                }.get(col, 'squid')
                                Enemy(monster_name, (x, y),
                                      [self.visible_sprites, self.attackable_sprites],
                                      self.obstacle_sprites,
                                      self.damage_player,
                                      self.trigger_death_particles,
                                      self.add_exp)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def create_magic(self, style, strength, cost):
        if style == 'heal':
            self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])
        elif style == 'flame':
            self.magic_player.flame(self.player, cost, [self.visible_sprites, self.attack_sprites])

    def player_attack_logic(self):
        for attack_sprite in self.attack_sprites:
            collisions = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
            for target in collisions:
                if target.sprite_type == 'grass':
                    pos = target.rect.center
                    offset = pygame.math.Vector2(0, 75)
                    for _ in range(randint(3, 6)):
                        self.animation_player.create_grass_particles(pos - offset, [self.visible_sprites])
                    target.kill()
                else:
                    target.get_damage(self.player, attack_sprite.sprite_type)

    def damage_player(self, amount, attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            self.animation_player.create_particles(attack_type, self.player.rect.center, [self.visible_sprites])

    def trigger_death_particles(self, pos, particle_type):
        self.animation_player.create_particles(particle_type, pos, self.visible_sprites)

    def add_exp(self, amount):
        self.player.exp += amount

    def toggle_menu(self):
        self.game_paused = not self.game_paused

    def run(self):
        # Draw everything
        self.visible_sprites.custom_draw(self.player)
        self.ui.display(self.player)

        if self.game_paused:
            self.upgrade.display()
        else:
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
            self.player_attack_logic()

            # NPC interaction handling
            npc = self.npc_group.sprite
            if npc:
                # Check proximity
                if self.player.rect.colliderect(npc.rect.inflate(40, 40)):
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_e]:
                        # Show dialogue only if not already active
                        if not self.dialogue_box.active:
                            self.dialogue_box.show([
                                "Hello there! Welcome to the world of Helga.",
                                "Feel free to explore and find secrets!"
                            ])
                else:
                    # Hide dialogue if player moves away
                    self.dialogue_box.hide()

        # Draw dialogue box if active
        self.dialogue_box.draw(self.display_surface)


class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('../SOFTWARE/Helga/graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_pos)

        for sprite in sorted(self.sprites(), key=lambda s: s.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def enemy_update(self, player):
        enemies = [s for s in self.sprites() if hasattr(s, 'sprite_type') and s.sprite_type == 'enemy']
        for enemy in enemies:
            enemy.enemy_update(player)
