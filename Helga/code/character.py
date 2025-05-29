import pygame
from settings import *
from math import sin

class Entity(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.frame_index = 0
        self.animation_speed = 0.15
        self.direction = pygame.math.Vector2()

    def move(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.hitbox.x += self.direction.x * speed
        self.collision('horizontal')
        self.hitbox.y += self.direction.y * speed
        self.collision('vertical')
        self.rect.center = self.hitbox.center

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.x > 0:  # moving right
                        self.hitbox.right = sprite.hitbox.left
                    if self.direction.x < 0:  # moving left
                        self.hitbox.left = sprite.hitbox.right

        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    if self.direction.y > 0:  # moving down
                        self.hitbox.bottom = sprite.hitbox.top
                    if self.direction.y < 0:  # moving up
                        self.hitbox.top = sprite.hitbox.bottom

    def wave_value(self):
        value = sin(pygame.time.get_ticks())
        if value >= 0:
            return 255
        else:
            return 0

class Player(Entity):
    def __init__(self, pos, groups, obstacle_sprites, create_attack, destroy_attack, create_magic, character='player'):
        super().__init__(groups)

        self.character = character
        self.starting_position = pos  # Save starting position

        # Load base image
        self.image = pygame.image.load(f'../SOFTWARE/Helga/graphics/player/{self.character}/down/down_0.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-6, HITBOX_OFFSET['player'])

        # Graphics setup
        self.import_player_assets()
        self.status = 'down'

        # Movement and action flags
        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None
        self.obstacle_sprites = obstacle_sprites

        # Weapon
        self.create_attack = create_attack
        self.destroy_attack = destroy_attack
        self.weapon_index = 0
        self.weapon = list(weapon_data.keys())[self.weapon_index]
        self.can_switch_weapon = True
        self.weapon_switch_time = None
        self.switch_duration_cooldown = 200

        # Magic
        self.create_magic = create_magic
        self.magic_index = 0
        self.magic = list(magic_data.keys())[self.magic_index]
        self.can_switch_magic = True
        self.magic_switch_time = None

        # Stats
        self.stats = {'health': 100, 'energy': 60, 'attack': 10, 'magic': 4, 'speed': 5}
        self.max_stats = {'health': 300, 'energy': 140, 'attack': 20, 'magic': 10, 'speed': 7}
        self.upgrade_cost = {'health': 50, 'energy': 50, 'attack': 50, 'magic': 50, 'speed': 50}
        self.health = self.stats['health'] * 1
        self.energy = self.stats['energy'] * 1
        self.exp = 0
        self.speed = self.stats['speed']

        # Damage timer
        self.vulnerable = True
        self.hurt_time = None
        self.invulnerability_duration = 500

        # Sounds
        self.weapon_attack_sound = pygame.mixer.Sound('../SOFTWARE/Helga/audio/sword.wav')
        self.weapon_attack_sound.set_volume(0.4)

    def import_player_assets(self):
        character_path = f'../SOFTWARE/Helga/graphics/player/{self.character}/'
        self.animations = {
            'up': [], 'down': [], 'left': [], 'right': [],
            'right_idle': [], 'left_idle': [], 'up_idle': [], 'down_idle': [],
            'right_attack': [], 'left_attack': [], 'up_attack': [], 'down_attack': []
        }

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def input(self):
        keys = pygame.key.get_pressed()

        if not self.attacking:
            # Movement input
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.direction.y = -1
                self.status = 'up'
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.direction.y = 1
                self.status = 'down'
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.direction.x = 1
                self.status = 'right'
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.direction.x = -1
                self.status = 'left'
            else:
                self.direction.x = 0

            # Attack input
            if keys[pygame.K_SPACE]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                self.create_attack()
                self.weapon_attack_sound.play()

            # Magic input
            if keys[pygame.K_LCTRL]:
                self.attacking = True
                self.attack_time = pygame.time.get_ticks()
                style = list(magic_data.keys())[self.magic_index]
                strength = self.stats['magic']
                cost = magic_data[style]['cost']
                self.create_magic(style, strength, cost)

            # Switch weapon
            if keys[pygame.K_q] and self.can_switch_weapon:
                self.can_switch_weapon = False
                self.weapon_switch_time = pygame.time.get_ticks()
                self.weapon_index = (self.weapon_index + 1) % len(weapon_data)
                self.weapon = list(weapon_data.keys())[self.weapon_index]

            # Switch magic
            if keys[pygame.K_e] and self.can_switch_magic:
                self.can_switch_magic = False
                self.magic_switch_time = pygame.time.get_ticks()
                self.magic_index = (self.magic_index + 1) % len(magic_data)
                self.magic = list(magic_data.keys())[self.magic_index]

    def get_status(self):
        if self.direction.x == 0 and self.direction.y == 0:
            if not 'idle' in self.status and not 'attack' in self.status:
                self.status = self.status + '_idle'

        if self.attacking:
            self.direction.x = 0
            self.direction.y = 0
            if not 'attack' in self.status:
                if 'idle' in self.status:
                    self.status = self.status.replace('_idle', '_attack')
                else:
                    self.status = self.status + '_attack'
        else:
            if 'attack' in self.status:
                self.status = self.status.replace('_attack', '')

    def cooldowns(self):
        current_time = pygame.time.get_ticks()

        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.destroy_attack()

        if not self.can_switch_weapon:
            if current_time - self.weapon_switch_time >= self.switch_duration_cooldown:
                self.can_switch_weapon = True

        if not self.can_switch_magic:
            if current_time - self.magic_switch_time >= self.switch_duration_cooldown:
                self.can_switch_magic = True

        if not self.vulnerable:
            if current_time - self.hurt_time >= self.invulnerability_duration:
                self.vulnerable = True

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def wave_value(self):
        value = pygame.time.get_ticks() % 500
        return 0 if value < 250 else 255

    def get_full_weapon_damage(self):
        base = self.stats['attack']
        weapon = weapon_data[self.weapon]['damage']
        return base + weapon

    def get_full_magic_damage(self):
        base = self.stats['magic']
        magic = magic_data[self.magic]['strength']
        return base + magic

    def get_value_by_index(self, index):
        return list(self.stats.values())[index]

    def get_cost_by_index(self, index):
        return list(self.upgrade_cost.values())[index]

    def energy_recovery(self):
        self.energy += 0.01 * self.stats['magic']
        if self.energy > self.stats['energy']:
            self.energy = self.stats['energy']

    def check_death(self):
        if self.health <= 0:
            self.respawn()

    def respawn(self):
        # Reset player stats and position
        self.health = self.stats['health']
        self.energy = self.stats['energy']
        self.rect.topleft = self.starting_position
        self.hitbox.topleft = self.starting_position
        self.vulnerable = True

    def update(self):
        self.input()
        self.cooldowns()
        self.get_status()
        self.animate()
        self.move(self.stats['speed'])
        self.energy_recovery()
        self.check_death()

class Textbox:
    def __init__(self, x, y, w, h, font, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = (255, 255, 255)
        self.text = text
        self.font = font
        self.txt_surface = font.render(text, True, self.color)

    def set_text(self, text):
        self.text = text
        self.txt_surface = self.font.render(self.text, True, self.color)

    def draw(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.rect)  # Background
        pygame.draw.rect(screen, self.color, self.rect, 2)  # Border
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))

class NPC(pygame.sprite.Sprite):
    def __init__(self, pos, image_path):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
        self.dialogue = [
    "GET AWAY YOU BEAST! I'LL GET Y-\n         Wait . . . \n\nYou dont look like a monster\n\n[Q] to close.",
    "Well uhm . . .  \nWhile i have you here . . .\nWould you be able to help me with something?\nTheres a reward if you do\n\n[Q] to close.",
    "I fear she's been captured.\nCan you help me find her??",
    "Before we get her, we have to train you up.\nCan you kill 5 bamboos for me?"
]

        self.dialogue_index = 0
        self.interacted = False

    def interact(self):
        if self.dialogue_index < len(self.dialogue):
            dialogue_line = self.dialogue[self.dialogue_index]
            self.dialogue_index += 1
            return dialogue_line
        else:
            self.interacted = True
            return "You're awesome!"

class Enemy(Entity):
    def __init__(self, monster_name, pos, groups, obstacle_sprites, damage_player, trigger_death_particles, add_exp):
        super().__init__(groups)
        self.sprite_type = 'enemy'

        # Graphics setup
        self.import_graphics(monster_name)
        self.status = 'idle'
        self.frame_index = 0

        self.monster_name = monster_name
        monster_info = monster_data[self.monster_name]

        self.animation_speed = monster_info['animation_speed']
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -10)
        self.obstacle_sprites = obstacle_sprites

        # Stats
        self.health = monster_info['health']
        self.exp = monster_info['exp']
        self.speed = monster_info['speed']
        self.attack_damage = monster_info['damage']
        self.resistance = monster_info['resistance']
        self.attack_radius = monster_info['attack_radius']
        self.notice_radius = monster_info['notice_radius']
        self.attack_type = monster_info['attack_type']

        # Player interaction
        self.can_attack = True
        self.attack_time = None
        self.attack_cooldown = monster_info['attack_cooldown']
        self.damage_player = damage_player
        self.trigger_death_particles = trigger_death_particles
        self.add_exp = add_exp

        # Invincibility timer
        self.vulnerable = True
        self.hit_time = None
        self.invincibility_duration = monster_info['invincibility_duration']

        # Sounds
        self.death_sound = pygame.mixer.Sound('../SOFTWARE/Helga/audio/death.wav')
        self.hit_sound = pygame.mixer.Sound('../SOFTWARE/Helga/audio/hit.wav')
        self.attack_sound = pygame.mixer.Sound(monster_info['attack_sound'])
        self.death_sound.set_volume(0.6)
        self.hit_sound.set_volume(0.6)
        self.attack_sound.set_volume(0.6)

        # Respawn
        self.alive = True
        self.respawn_time = monster_info['respawn_time']
        self.death_time = None
        self.starting_pos = pos

    def import_graphics(self, name):
        self.animations = {'idle': [], 'move': [], 'attack': [], 'death': []}
        main_path = f'../SOFTWARE/Helga/graphics/monsters/{name}/'
        for animation in self.animations.keys():
            self.animations[animation] = import_folder(main_path + animation)

    def get_player_distance_direction(self, player):
        enemy_vec = pygame.math.Vector2(self.rect.center)
        player_vec = pygame.math.Vector2(player.rect.center)
        distance = (player_vec - enemy_vec).magnitude()

        if distance > 0:
            direction = (player_vec - enemy_vec).normalize()
        else:
            direction = pygame.math.Vector2()

        return (distance, direction)

    def get_status(self, player):
        distance = self.get_player_distance_direction(player)[0]

        if distance <= self.attack_radius and self.can_attack:
            if self.status != 'attack':
                self.frame_index = 0
            self.status = 'attack'
        elif distance <= self.notice_radius:
            self.status = 'move'
        else:
            self.status = 'idle'

    def actions(self, player):
        if self.status == 'attack':
            self.attack_time = pygame.time.get_ticks()
            self.damage_player(self.attack_damage, self.attack_type)
            self.attack_sound.play()
        elif self.status == 'move':
            self.direction = self.get_player_distance_direction(player)[1]
        else:
            self.direction = pygame.math.Vector2()

    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed

        if self.status == 'death':
            if self.frame_index >= len(animation):
                self.frame_index = len(animation) - 1  # freeze on last frame
        else:
            if self.frame_index >= len(animation):
                if self.status == 'attack':
                    self.can_attack = False
                self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        self.rect = self.image.get_rect(center=self.hitbox.center)

        if not self.vulnerable:
            alpha = self.wave_value()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def cooldowns(self):
        current_time = pygame.time.get_ticks()
        if not self.can_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.can_attack = True

        if not self.vulnerable:
            if current_time - self.hit_time >= self.invincibility_duration:
                self.vulnerable = True

    def get_damage(self, player, attack_type):
        if self.vulnerable and self.alive:
            self.hit_sound.play()
            self.direction = self.get_player_distance_direction(player)[1]
            if attack_type == 'weapon':
                self.health -= player.get_full_weapon_damage()
            else:
                self.health -= player.get_full_magic_damage()
            self.hit_time = pygame.time.get_ticks()
            self.vulnerable = False

    def check_death(self):
        if self.health <= 0 and self.alive:
            self.alive = False
            self.status = 'death'
            self.frame_index = 0  # Start death animation
            self.death_time = pygame.time.get_ticks()
            self.trigger_death_particles(self.rect.center, self.monster_name)
            self.add_exp(self.exp)
            self.death_sound.play()

    def respawn(self):
        self.health = monster_data[self.monster_name]['health']
        self.rect.topleft = self.starting_pos
        self.hitbox = self.rect.inflate(0, -10)
        self.alive = True
        self.status = 'idle'
        self.frame_index = 0
        self.vulnerable = True
        self.can_attack = True
        self.image.set_alpha(255)

    def hit_reaction(self):
        if not self.vulnerable:
            self.direction *= -self.resistance

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.alive:
            self.hit_reaction()
            self.move(self.speed)
            self.animate()
            self.cooldowns()
            self.check_death()
        else:
            self.animate()  # So the death animation plays even while dead
            if current_time - self.death_time >= self.respawn_time:
                self.respawn()

    def enemy_update(self, player):
        if self.alive:
            self.get_status(player)
            self.actions(player)
