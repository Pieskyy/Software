import pygame

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
            "Hey you! can you help me?",
            "Thanks, Helga has gone missing.",
            "i fear shes been captured",
            "can you help me find her??",
            "Before we get her, we have to train you up.",
            " can you kill 5 bamboos for me?"
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
