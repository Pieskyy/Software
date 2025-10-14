import pygame
import sys
from settings import *
from level import Level
from character import NPC, Textbox

def character_selection(screen, clock): #character selection options.
    characters = ['sam', 'ninja', 'flame', 'Skelly', 'Porky']
    selected_index = 0

    images = []
    for char in characters:
        path = f'../SOFTWARE/Helga/graphics/player/{char}/down/down_0.png'#grab from file with the name from characters
        img = pygame.image.load(path).convert_alpha()
        images.append(img)

    title_bg = pygame.image.load('../SOFTWARE/Helga/graphics/selection_screen.png').convert()
    title_bg = pygame.transform.scale(title_bg, (WIDTH, HEIGHT))

    font = pygame.font.Font(None, 50)
    selecting = True

    while selecting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_w, pygame.K_UP]:
                    selected_index = (selected_index - 1) % len(characters)
                elif event.key in [pygame.K_s, pygame.K_DOWN]:
                    selected_index = (selected_index + 1) % len(characters)
                elif event.key == pygame.K_RETURN:
                    selecting = False

        screen.blit(title_bg, (0, 0))

        for i, char in enumerate(characters):
            y = 100 + i * 120
            x_img = 100
            x_text = x_img + 80

            screen.blit(images[i], (x_img, y))
            color = (255, 255, 0) if i == selected_index else (255, 255, 255)
            text = font.render(char.capitalize(), True, color)
            screen.blit(text, (x_text, y + 16))

            if i == selected_index:
                rect_x = x_img - 15
                rect_y = y - 15
                rect_width = (x_text + text.get_width()) - rect_x + 15
                rect_height = 64 + 30
                pygame.draw.rect(screen, (255, 255, 0), (rect_x, rect_y, rect_width, rect_height), 4)
        pygame.display.flip()
        clock.tick(FPS)

    return characters[selected_index]


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('The Legend of Helga')
        self.clock = pygame.time.Clock()

        self.font = pygame.font.Font(None, 30)

        self.main_sound = pygame.mixer.Sound('../SOFTWARE/Helga/audio/main.ogg')
        self.main_sound.set_volume(0.5)
        self.main_sound.play(loops=-1)

        self.show_title_screen()
        self.selected_character = character_selection(self.screen, self.clock)
        self.level = Level(self.selected_character)

        self.npc = NPC((300, 200), '../SOFTWARE/Helga/graphics/npc/npcclear.png')
        self.textbox = Textbox(100, 40, 50, 100, self.font)

        self.dialogue_active = False
        self.current_text = ""

    def show_title_screen(self):
        title_image = pygame.image.load('../SOFTWARE/Helga/graphics/title_screen.png').convert()
        title_image = pygame.transform.scale(title_image, (WIDTH, HEIGHT))
        font = pygame.font.Font(None, 50)
        play_text = font.render("Press any key to start", True, 'white')
        play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGHT - 60))

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

            self.screen.blit(title_image, (0, 0))
            self.screen.blit(play_text, play_rect)
            pygame.display.update()
            self.clock.tick(FPS)

    def run(self):
        player_rect = pygame.Rect(100, 100, 1, 1)
        player_speed = 5

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()

            if not self.dialogue_active and not self.level.show_upgrade:
                if keys[pygame.K_LEFT]:
                    player_rect.x -= player_speed
                if keys[pygame.K_RIGHT]:
                    player_rect.x += player_speed
                if keys[pygame.K_UP]:
                    player_rect.y -= player_speed
                if keys[pygame.K_DOWN]:
                    player_rect.y += player_speed

                if keys[pygame.K_SPACE]:
                    if player_rect.colliderect(self.npc.rect) and not self.dialogue_active:
                        self.current_text = self.npc.interact()
                        self.textbox.set_text(self.current_text)
                        self.dialogue_active = True

            self.screen.fill(WATER_COLOR)
            self.level.run()

            self.screen.blit(self.npc.image, self.npc.rect)

            if self.dialogue_active:
                self.textbox.draw(self.screen)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
