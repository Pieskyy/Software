import pygame
from settings import *
from random import choice, randint
from upgrade import Upgrade, Weapon, MagicPlayer
from character import NPC, Textbox, Enemy, Player  # Import NPC and Textbox classes

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
                if self.player.rect.colliderect(npc.rect.inflate(20, 20)):
                    if keys[pygame.K_SPACE]:
                        self.current_dialogue = npc.interact()
                        self.textbox.set_text(self.current_dialogue)
                        self.dialogue_active = True

class UI:
    def __init__(self):

        # general
        self.display_surface = pygame.display.get_surface()
        self.font = pygame.font.Font(UI_FONT, UI_FONT_SIZE)

        # bar setup
        self.health_bar_rect = pygame.Rect(10, 10, HEALTH_BAR_WIDTH, BAR_HEIGHT)
        self.energy_bar_rect = pygame.Rect(10, 34, ENERGY_BAR_WIDTH, BAR_HEIGHT)

        # convert weapon dictionary
        self.weapon_graphics = []
        for weapon in weapon_data.values():
            path = weapon['graphic']
            weapon = pygame.image.load(path).convert_alpha()
            self.weapon_graphics.append(weapon)

        # convert magic dictionary
        self.magic_graphics = []
        for magic in magic_data.values():
            magic = pygame.image.load(magic['graphic']).convert_alpha()
            self.magic_graphics.append(magic)

    def show_bar(self, current, max_amount, bg_rect, color):
        # draw bg
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)

        # converting stat to pixel
        ratio = current / max_amount
        current_width = bg_rect.width * ratio
        current_rect = bg_rect.copy()
        current_rect.width = current_width

        # drawing the bar
        pygame.draw.rect(self.display_surface, color, current_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)

    def show_exp(self, exp):
        text_surf = self.font.render(str(int(exp)), False, TEXT_COLOR)
        x = self.display_surface.get_size()[0] - 20
        y = self.display_surface.get_size()[1] - 20
        text_rect = text_surf.get_rect(bottomright=(x, y))

        pygame.draw.rect(self.display_surface, UI_BG_COLOR, text_rect.inflate(20, 20))
        self.display_surface.blit(text_surf, text_rect)
        pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, text_rect.inflate(20, 20), 3)

    def selection_box(self, left, top, has_switched):
        bg_rect = pygame.Rect(left, top, ITEM_BOX_SIZE, ITEM_BOX_SIZE)
        pygame.draw.rect(self.display_surface, UI_BG_COLOR, bg_rect)
        if has_switched:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR_ACTIVE, bg_rect, 3)
        else:
            pygame.draw.rect(self.display_surface, UI_BORDER_COLOR, bg_rect, 3)
        return bg_rect

    def weapon_overlay(self, weapon_index, has_switched):
        bg_rect = self.selection_box(10, 630, has_switched)
        weapon_surf = self.weapon_graphics[weapon_index]
        weapon_rect = weapon_surf.get_rect(center=bg_rect.center)

        self.display_surface.blit(weapon_surf, weapon_rect)

    def magic_overlay(self, magic_index, has_switched):
        bg_rect = self.selection_box(80, 635, has_switched)
        magic_surf = self.magic_graphics[magic_index]
        magic_rect = magic_surf.get_rect(center=bg_rect.center)

        self.display_surface.blit(magic_surf, magic_rect)

    def display(self, player):
        self.show_bar(player.health, player.stats['health'], self.health_bar_rect, HEALTH_COLOR)
        self.show_bar(player.energy, player.stats['energy'], self.energy_bar_rect, ENERGY_COLOR)

        self.show_exp(player.exp)

        self.weapon_overlay(player.weapon_index, not player.can_switch_weapon)
        self.magic_overlay(player.magic_index, not player.can_switch_magic)

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups, sprite_type, surface=pygame.Surface((TILESIZE, TILESIZE))):
        super().__init__(groups)
        self.sprite_type = sprite_type
        y_offset = HITBOX_OFFSET[sprite_type]
        self.image = surface
        if sprite_type == 'object':
            self.rect = self.image.get_rect(topleft=(pos[0], pos[1] - TILESIZE))
        else:
            self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, y_offset)

class AnimationPlayer:
    def __init__(self):
        self.frames = {
            # magic
            'flame': import_folder('../SOFTWARE/Helga/graphics/particles/flame/frames'),
            'aura': import_folder('../SOFTWARE/Helga/graphics/particles/aura'),
            'heal': import_folder('../SOFTWARE/Helga/graphics/particles/heal/frames'),

            # attacks
            'claw': import_folder('../SOFTWARE/Helga/graphics/particles/claw'),
            'slash': import_folder('../SOFTWARE/Helga/graphics/particles/slash'),
            'sparkle': import_folder('../SOFTWARE/Helga/graphics/particles/sparkle'),
            'leaf_attack': import_folder('../SOFTWARE/Helga/graphics/particles/leaf_attack'),
            'thunder': import_folder('../SOFTWARE/Helga/graphics/particles/thunder'),

            # monster deaths
            'squid': import_folder('../SOFTWARE/Helga/graphics/particles/smoke_orange'),
            'raccoon': import_folder('../SOFTWARE/Helga/graphics/particles/raccoon'),
            'spirit': import_folder('../SOFTWARE/Helga/graphics/particles/nova'),
            'bamboo': import_folder('../SOFTWARE/Helga/graphics/particles/bamboo'),

            # leafs
            'leaf': (
                import_folder('../SOFTWARE/Helga/graphics/particles/leaf1'),
                import_folder('../SOFTWARE/Helga/graphics/particles/leaf2'),
                import_folder('../SOFTWARE/Helga/graphics/particles/leaf3'),
                import_folder('../SOFTWARE/Helga/graphics/particles/leaf4'),
                import_folder('../SOFTWARE/Helga/graphics/particles/leaf5'),
                import_folder('../SOFTWARE/Helga/graphics/particles/leaf6'),
                self.reflect_images(import_folder('../SOFTWARE/Helga/graphics/particles/leaf1')),
                self.reflect_images(import_folder('../SOFTWARE/Helga/graphics/particles/leaf2')),
                self.reflect_images(import_folder('../SOFTWARE/Helga/graphics/particles/leaf3')),
                self.reflect_images(import_folder('../SOFTWARE/Helga/graphics/particles/leaf4')),
                self.reflect_images(import_folder('../SOFTWARE/Helga/graphics/particles/leaf5')),
                self.reflect_images(import_folder('../SOFTWARE/Helga/graphics/particles/leaf6'))
            )
        }

    def reflect_images(self, frames):
        new_frames = []

        for frame in frames:
            flipped_frame = pygame.transform.flip(frame, True, False)
            new_frames.append(flipped_frame)
        return new_frames

    def create_grass_particles(self, pos, groups):
        animation_frames = choice(self.frames['leaf'])
        ParticleEffect(pos, animation_frames, groups)

    def create_particles(self, animation_type, pos, groups):
        animation_frames = self.frames[animation_type]
        ParticleEffect(pos, animation_frames, groups)

class ParticleEffect(pygame.sprite.Sprite):

    def __init__(self, pos, animation_frames, groups):
        super().__init__(groups)
        self.sprite_type = 'magic'
        self.frame_index = 0
        self.animation_speed = 0.15
        self.frames = animation_frames
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]

    def update(self):
        self.animate()

pygame.init()
font = pygame.font.Font(None, 30)

def debug(info, y=10, x=10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'White')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, 'Black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)
