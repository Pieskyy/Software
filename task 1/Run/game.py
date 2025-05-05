import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack Game")

card_images = {}
card_width, card_height = 115, 155
suits = ['d', 'h', 's', 'c']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

for rank in ranks:
    for suit in suits:
        image = pygame.image.load(f'Github/task 1/cards/{rank}{suit}.png')
        card_images[f'{rank}{suit}'] = pygame.transform.scale(image, (card_width, card_height))

back = pygame.image.load('Github/task 1/cards/back.png')
back = pygame.transform.scale(back, (card_width, card_height))

total_value = 0  #actual total
round_total = 0.0 #total of each ropund
count = ""

def total(card_list):#updates round_total
    global round_total
    for card in card_list:
        rank = card[:-1]
        if rank in ['2', '3', '4', '5', '6']:
            round_total -= 1
        elif rank in ['10', 'J', 'Q', 'K', 'A']:
            round_total += 1


def hand_value(hand):#gets actual value of hand
    value = 0
    aces = 0
    for card in hand:
        rank = card[:-1]
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            aces += 1
            value += 11
        else:
            value += int(rank)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def reset(): #resets everything for a new round
    global deck, player_hand, dealer_hand, bust, result, show_dealer, dealer_standing, round_total, count
    deck = [f'{rank}{suit}' for rank in ranks for suit in suits]
    random.shuffle(deck)
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    bust = False
    result = ""
    show_dealer = False
    dealer_standing = False
    round_total = 0  #reset round total
    total(player_hand)
    total([dealer_hand[0]])
    count = f"Total: {total_value + round_total}"  #total + round total

def hand_draw(hand, start_x, start_y, show_dealer_second_card=True):#hand images
    total_width = len(hand) * (card_width + 10)
    start_x = (WIDTH - total_width) // 2
    for i, card in enumerate(hand):
        x = start_x + i * (card_width + 10)
        if i == 1 and not show_dealer_second_card:
            screen.blit(back, (x, start_y))
        else:
            screen.blit(card_images[card], (x, start_y))

def button(x, y, width, height, text):#button
    pygame.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    font = pygame.font.SysFont('Arial', 36)
    text_surf = font.render(text, True, (0, 0, 0))
    screen.blit(text_surf, (x + (width - text_surf.get_width()) // 2, y + (height - text_surf.get_height()) // 2))

def clicked(x, y, width, height, mouse_pos):#clicked
    return x <= mouse_pos[0] <= x + width and y <= mouse_pos[1] <= y + height

def draw_quiz_screen():#quiz
    global feedback, feedback_time

    box_width, box_height = 500, 300
    box_x = (WIDTH - box_width) // 2
    box_y = (HEIGHT - box_height) // 2
    pygame.draw.rect(screen, (255, 255, 255), (box_x, box_y, box_width, box_height))

    font = pygame.font.SysFont('Arial', 28)
    header = font.render(f"The total is {total_value}", True, (0, 0, 0))
    screen.blit(header, (box_x + (box_width - header.get_width()) // 2, box_y + 30))

    question = font.render("What is the next card more likely to be?:", True, (0, 0, 0))
    screen.blit(question, (box_x + (box_width - question.get_width()) // 2, box_y + 80))

    button_w, button_h = 120, 50
    spacing = 30
    start_x = box_x + (box_width - (3 * button_w + 2 * spacing)) // 2
    start_y = box_y + 150

    buttons = {
        "less": pygame.Rect(start_x, start_y, button_w, button_h),
        "equal": pygame.Rect(start_x + button_w + spacing, start_y, button_w, button_h),
        "more": pygame.Rect(start_x + 2 * (button_w + spacing), start_y, button_w, button_h)
    }

    pygame.draw.rect(screen, (200, 200, 200), buttons["less"])
    pygame.draw.rect(screen, (200, 200, 200), buttons["equal"])
    pygame.draw.rect(screen, (200, 200, 200), buttons["more"])

    font_small = pygame.font.SysFont('Arial', 24)
    screen.blit(font_small.render("    ≤6", True, (0, 0, 0)), buttons["less"].move(25, 10))
    screen.blit(font_small.render("any card", True, (0, 0, 0)), buttons["equal"].move(20, 10))
    screen.blit(font_small.render("   ≥10", True, (0, 0, 0)), buttons["more"].move(25, 10))

    if feedback:
        if pygame.time.get_ticks() - feedback_time < 2000:  #Show for 2 seconds
            font_feedback = pygame.font.SysFont('Arial', 32)
            text = font_feedback.render(feedback, True, (255, 0, 0))
            screen.blit(text, ((WIDTH - text.get_width()) // 2, HEIGHT // 2 + 100))
        else:
            feedback = "" 

    return buttons


def game():#game function
    global bust, result, show_dealer, dealer_standing, total_value, count, feedback, feedback_time
    reset()
    font = pygame.font.SysFont('Arial', 36)
    state = "game"
    quiz_buttons = {}

    feedback = ""
    feedback_time = 0

    while True:
        screen.fill((0, 128, 0))
        mouse_pos = pygame.mouse.get_pos()

        if state == "game":
            hand_draw(player_hand, WIDTH // 2 - card_width - 20, HEIGHT // 2.25 + 50)
            hand_draw(dealer_hand, WIDTH // 2 + 20, HEIGHT // 3 - 50, show_dealer_second_card=show_dealer)

            count_surface = font.render(count, True, (255, 255, 255))
            screen.blit(count_surface, (10, 0))

            if result:
                result_surface = font.render(result, True, (255, 255, 255))
                screen.blit(result_surface, (WIDTH // 2 - result_surface.get_width() // 2, HEIGHT // 2 - 200))
                button(WIDTH // 2 - 100, HEIGHT - 560, 200, 50, "Play Again")
            else:
                button(WIDTH // 4 - 175, HEIGHT - 560, 200, 50, "Hit")
                button(WIDTH // 1 - 225, HEIGHT - 560, 200, 50, "Stand")

        elif state == "quiz":
            quiz_buttons = draw_quiz_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if state == "game":
                    if clicked(WIDTH // 4 - 175, HEIGHT - 560, 200, 50, mouse_pos) and not result: #hit
                        new_card = deck.pop()
                        player_hand.append(new_card)
                        total([new_card])
                        count = f"Total: {total_value + round_total}" #update total display
                        if hand_value(player_hand) > 21:
                            bust = True
                            result = "You Bust!"
                            show_dealer = True
                            total([dealer_hand[1]])
                            count = f"Total: {total_value + round_total}"

                    if clicked(WIDTH // 1 - 225, HEIGHT - 560, 200, 50, mouse_pos) and not result: #stand
                        show_dealer = True
                        dealer_standing = True
                        total([dealer_hand[1]])
                        while hand_value(dealer_hand) < 17:
                            new_card = deck.pop()
                            dealer_hand.append(new_card)
                            total([new_card])
                        dealer_value = hand_value(dealer_hand)
                        player_value = hand_value(player_hand)
                        if dealer_value > 21:
                            result = "Dealer Busts!"
                        elif player_value > dealer_value:
                            result = "You Win!"
                        elif player_value < dealer_value:
                            result = "You Lose!"
                        else:
                            result = "It's a Draw!"
                        count = f"Total: {total_value + round_total}"

                    if result and clicked(WIDTH // 2 - 100, HEIGHT - 560, 200, 50, mouse_pos):
                        total_value += round_total  #add round score to full total before quiz
                        state = "quiz"

                elif state == "quiz":   #if in quiz mode
                    if quiz_buttons["less"].collidepoint(mouse_pos):
                        if total_value > 0:  #positive total, 6 or below
                            reset()
                            state = "game"
                        else:
                            feedback = "WRONG"#says wrong
                            feedback_time = pygame.time.get_ticks()

                    elif quiz_buttons["equal"].collidepoint(mouse_pos):
                        if total_value == 0:  #could be all
                            reset()
                            state = "game"
                        else:
                            feedback = "WRONG"
                            feedback_time = pygame.time.get_ticks()
                    elif quiz_buttons["more"].collidepoint(mouse_pos):
                        if total_value < 0:  #negative total, should be 10+
                            reset()
                            state = "game"
                        else:
                            feedback = "WRONG"
                            feedback_time = pygame.time.get_ticks()

        pygame.display.update()

game()
