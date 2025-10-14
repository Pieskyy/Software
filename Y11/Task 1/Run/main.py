import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Black Jack")
clock = pygame.time.Clock()
button = 0

img = pygame.image.load('Software/Task 1/images/bjlogo.png') #Load images
pygame.display.set_icon(img)
image1 = pygame.image.load('Software/Task 1/images/blackjack_img1.png')
image2 = pygame.image.load('Software/Task 1/images/blackjack_2.png')
image3 = pygame.image.load('Software/Task 1/images/123.png')
image4 = pygame.image.load('Software/Task 1/images/demo.png')
image5 = pygame.image.load('Software/Task 1/images/demo2.png')
image6 = pygame.image.load('Software/Task 1/images/percy.png')

def get_scaled_font(size, font_name="Arial"):
    return pygame.font.SysFont(font_name, size)

def get_buttons(screen_width, screen_height):
    button_width = screen_width // 6
    button_height = screen_height // 12
    next_btn = pygame.Rect(screen_width - button_width - 20, screen_height - button_height - 20, button_width, button_height)
    back_btn = pygame.Rect(20, screen_height - button_height - 20, button_width, button_height)
    return next_btn, back_btn

def draw_button(screen, rect, text, font, hover=False):
    color = (255, 255, 255) if not hover else (200, 200, 200)
    pygame.draw.rect(screen, color, rect)
    label = font.render(text, True, (0, 0, 0))
    screen.blit(label, (rect.centerx - label.get_width() // 2, rect.centery - label.get_height() // 2))

def drawIntro(screen, button, screen_width, screen_height):
    screen.fill((0, 128, 0))
    title_font = get_scaled_font(screen_width // 25)
    body_font = get_scaled_font(screen_width // 45)

    image_y_offset = screen_height // 8
    text_y_start = screen_height // 2 + 40

    if button == 0:
        header = "Welcome to Card Counting in Blackjack!"
        body = [
            "This game teaches you how to count cards using probability.",
            "You'll learn how to predict outcomes using basic math skills.",
            "We'll use Blackjack as a fun and interactive way to explore it!"
        ]
        image = image1

    elif button == 1:
        header = "How to Play Blackjack"
        body = [
            "Your goal is to get as close to 21 as possible without going over.",
            "Terms:",
            "• Hit: Take another card",
            "• Stand: Keep your current hand",
            "• Bust: Go over 21 and lose",
            "You're playing against the dealer, not other players."
        ]
        image = image2

    elif button == 2:
        header = "What is Card Counting?"
        body = [
            "Card counting is using probability to make smarter decisions.",
            "The Hi-Lo system helps track the ratio of high to low cards.",
            "• 2-6 = -1",
            "• 7-9 = 0",
            "• 10, J, Q, K, A = +1",
            "A lower running count means more high cards remain."
        ]
        image = image3

    elif button == 3:
        header = "Probability in Action"
        body = [
            "You and the dealer play a few cards:",
            "Player: 3, 4 (-1 each), Dealer: 6, 7 (-1, 0)",
            "Player hits: 5, 9 (-1, 0), Dealer hits: 8 (0)",
            "Running total: -1 -1 -1 -1 +0 +0 +0 = -4",
            "A lower count means more 10s, J, Q, K, or Aces are likely next.",
            "A higher count means more 2, 3, 4, 5 or 6's are likely next.",
            "This lets you make smarter choices using probability!"
        ]
        image = image3

    
    elif button == 4:
        header = "Demo"
        body = [
            "You've Recieved a Queen and a king, the Dealer has recieved a 4, Jack and a Queen",
            "Technically by the Rules of Blackjack you have won. You have 20 and Dealer bust with 24",
            "But, What does this mean for the next round? What are the chances to get a hand like this again?",
            "Well, If your Queen and King = +1 each, likewise for the Dealers Jack and Queen",
            "and then the Dealers 4 = +3. THat means that next round you are more likley to get a lower card",
            "This is where Probabilitie comes in. ",
            ""
        ]
        image = image4
    
    elif button == 5:
        header = "Demo"
        body = [
            "With the count currently at +3, it's more likely that the next card will be low.",
            "This makes hitting a safer option. If it were negative, you'd be more likely to get a high card,",
            "which could cause you to bust. Since you're sitting on 12, it's already a risky position.",
            "Understanding the probability of the next card can help you make a safer decision about whether ",
            "to hit or stand."
        ]

        image = image5

    elif button == 6:
        header = "Formulas"
        body = [
            "P(≤6) = (20 / 50) × 100 - Total.               This is the Formula for cards below or equal to 6",  
            "P(≥10) = (20 / 50) × 100 - Total.              This is the Formula for cards hhigher then or equal to 10",
            "P(7, 8, 9) = (20 / 50) × 100 - Total.          This is formula for 7, 8 and 9"

        ]
           
        image = image6

    elif button == 7:
        from game import game_loop
        return

    title_surf = title_font.render(header, True, (255, 255, 255))   #title of each slide
    title_rect = title_surf.get_rect(center=(screen_width // 2, screen_height // 16))
    screen.blit(title_surf, title_rect)

    scaled_img = pygame.transform.scale(image, (screen_width // 2, screen_height // 3))#images
    img_rect = scaled_img.get_rect(center=(screen_width // 2, image_y_offset + scaled_img.get_height() // 2))
    screen.blit(scaled_img, img_rect)

    text_box_height = screen_height * 0.35 if button == 3 else screen_height * 0.3#text box
    text_box_rect = pygame.Rect(screen_width // 10, text_y_start, screen_width * 0.8, text_box_height)
    pygame.draw.rect(screen, (180, 180, 180), text_box_rect, border_radius=10)
    pygame.draw.rect(screen, (0, 0, 0), text_box_rect, 2, border_radius=10)

    padding = 15#body text
    for i, line in enumerate(body):
        line_surf = body_font.render(line, True, (20, 20, 20))
        screen.blit(line_surf, (text_box_rect.x + padding, text_box_rect.y + padding + i * (body_font.get_height() + 5)))

    next_btn, back_btn = get_buttons(screen_width, screen_height)#buttons
    mouse_pos = pygame.mouse.get_pos()
    draw_button(screen, next_btn, "Next", body_font, next_btn.collidepoint(mouse_pos))
    draw_button(screen, back_btn, "Back", body_font, back_btn.collidepoint(mouse_pos))

running = True#main loop
while running:
    screen_width, screen_height = screen.get_size()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            next_btn, back_btn = get_buttons(screen_width, screen_height)
            if next_btn.collidepoint(event.pos):
                button = min(button + 1, 7)
            elif back_btn.collidepoint(event.pos):
                button = max(button - 1, 0)

    drawIntro(screen, button, screen_width, screen_height)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()