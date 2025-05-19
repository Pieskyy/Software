import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        pygame.display.set_caption('Zelda')
        self.clock = pygame.time.Clock()

        self.level = Level()

        # sound
        self.main_sound = pygame.mixer.Sound('../SOFTWARE/Helga/audio/main.ogg')
        self.main_sound.set_volume(0.5)

    def show_title_screen(self):
        title_image = pygame.image.load('../SOFTWARE/Helga/graphics/title_screen.png').convert()
        title_image = pygame.transform.scale(title_image, (WIDTH, HEIGTH))
        font = pygame.font.Font(None, 50)
        play_text = font.render("Press any key to start", True, 'white')
        play_rect = play_text.get_rect(center=(WIDTH // 2, HEIGTH - 60))

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
        self.show_title_screen()         # <-- Show the title screen first
        self.main_sound.play(loops=-1)   # Start music AFTER title screen

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
