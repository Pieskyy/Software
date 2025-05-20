import pygame
import sys
from settings import *
from support import import_folder
from level import Level

# Character select screen
def character_select_screen(screen, clock):
    characters = ['sam', 'ninja', 'flame']
    selected_index = 0

    # Load down_0 images for each character
    images = []
    for char in characters:
        path = f'../SOFTWARE/Helga/graphics/player/{char}/down/down_0.png'
        img = pygame.image.load(path).convert_alpha()
        img = pygame.transform.scale(img, (64, 64))
        images.append(img)

    # Load title screen image as background for selection screen
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

        # Draw title screen background
        screen.blit(title_bg, (0, 0))

        for i, char in enumerate(characters):
            y = 150 + i * 120
            x_img = 100  # far left position for image
            x_text = x_img + 80  # text starts after image

            # Draw character image
            screen.blit(images[i], (x_img, y))

            # Draw character name
            color = (255, 255, 0) if i == selected_index else (255, 255, 255)
            text = font.render(char.capitalize(), True, color)
            screen.blit(text, (x_text, y + 16))

            # Draw bigger yellow selection rectangle around image + text
            if i == selected_index:
                rect_x = x_img - 15
                rect_y = y - 15
                rect_width = (x_text + text.get_width()) - rect_x + 15
                rect_height = 64 + 30  # image height + padding
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

        # Start background music immediately, plays during title, selection and game
        self.main_sound = pygame.mixer.Sound('../SOFTWARE/Helga/audio/main.ogg')
        self.main_sound.set_volume(0.5)
        self.main_sound.play(loops=-1)  # loop forever

        self.show_title_screen()  # Show title screen first
        self.selected_character = character_select_screen(self.screen, self.clock)  # Then character selection

        self.level = Level(self.selected_character)  # Pass selected character to Level

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
        # Music already playing from __init__, no need to play here
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

            self.screen.fill(WATER_COLOR)
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == '__main__':
    game = Game()
    game.run()
