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
from npc import NPC, Textbox  # Import NPC and Textbox classes

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        self.floor_surf = pygame.image.load('../SOFTWARE/Helga/graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft=(0, 0))

    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf, floor_offset_pos)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

    def enemy_update(self, player):
        enemy_sprites = [sprite for sprite in self.sprites() if
                         hasattr(sprite, 'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)

class Level:
    def __init__(self, character='player'):
        self.display_surface = pygame.display.get_surface()
        self.game_paused = False
        self.selected_character = character

        # Sprite groups
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()

        # Attack groups
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        # UI, upgrade, particles
        self.ui = UI()
        
        # Create map and player
        self.npc_group = pygame.sprite.GroupSingle()
        self.create_map()
        
        self.upgrade = Upgrade(self.player)
        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)

        # Dialogue system setup
        self.font = pygame.font.Font(None, 30)
        self.textbox = Textbox(400, 450, 500, 100, self.font)
        self.dialogue_active = False
        self.current_dialogue = ""

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
                        if style == 'grass':
                            random_grass_image = choice(graphics['grass'])
                            Tile(
                                (x, y),
                                [self.visible_sprites, self.obstacle_sprites, self.attackable_sprites],
                                'grass',
                                random_grass_image)
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'object', surf)
                        if style == 'entities':
                            if col == '394':
                                self.player = Player(
                                    (x, y),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic,
                                    character=self.selected_character)
                            else:
                                if col == '390':
                                    monster_name = 'bamboo'
                                elif col == '391':
                                    monster_name = 'spirit'
                                elif col == '392':
                                    monster_name = 'raccoon'
                                else:
                                    monster_name = 'squid'
                                Enemy(
                                    monster_name,
                                    (x, y),
                                    [self.visible_sprites, self.attackable_sprites],
                                    self.obstacle_sprites,
                                    self.damage_player,
                                    self.trigger_death_particles,
                                    self.add_exp)

        # Add an NPC manually (static image)
        npc_position = (37 * TILESIZE, 21.5 * TILESIZE)
        npc = NPC(npc_position, '../SOFTWARE/Helga/graphics/npc/npc.png')
        self.npc_group.add(npc)
        self.visible_sprites.add(npc)

    def create_attack(self):
        self.current_attack = Weapon(self.player, [self.visible_sprites, self.attack_sprites])

    def create_magic(self, style, strength, cost):
        if style == 'heal':
            self.magic_player.heal(self.player, strength, cost, [self.visible_sprites])
        if style == 'flame':
            self.magic_player.flame(self.player, cost, [self.visible_sprites, self.attack_sprites])

    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite, self.attackable_sprites, False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            pos = target_sprite.rect.center
                            offset = pygame.math.Vector2(0, 75)
                            for leaf in range(randint(3, 6)):
                                self.animation_player.create_grass_particles(pos - offset, [self.visible_sprites])
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player, attack_sprite.sprite_type)

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
        # If game paused, show upgrade menu only
        if self.game_paused:
            self.upgrade.display()
            self.ui.display(self.player)  # still display UI
            self.visible_sprites.custom_draw(self.player)  # still draw world
            return

        # Update and draw world
        self.visible_sprites.update()
        self.visible_sprites.enemy_update(self.player)
        self.player_attack_logic()
        self.visible_sprites.custom_draw(self.player)
        self.ui.display(self.player)

        # NPC interaction and dialogue system
        npc = self.npc_group.sprite
        keys = pygame.key.get_pressed()

        if npc:
            # If dialogue active, prevent player movement and draw textbox
            if self.dialogue_active:
                # Draw dialogue box
                self.textbox.draw(self.display_surface)
                # Close dialogue if player presses RETURN
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.dialogue_active = False
                            self.textbox.set_text("test")
            else:
                if self.player.rect.colliderect(npc.rect.inflate(500, 20)):
                    if keys[pygame.K_SPACE]:
                        self.current_dialogue = npc.interact()
                        self.textbox.set_text(self.current_dialogue)
                        self.dialogue_active = True

