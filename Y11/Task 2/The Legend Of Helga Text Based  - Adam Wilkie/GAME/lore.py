from settings import *
import os, time, shutil
from start import *


def lore(player, dime): # lroe at start of game
    columns, _ = shutil.get_terminal_size()
    name = player.user # Back story lore ish idk
    
    print('You are in a forest. Chopping wood. When suddenly you hear . . .\n\n\n'.center(columns))
    time.sleep(4)

    print('*Bushes rustle in the distance*\n'.center(columns))
    time.sleep(3)

    print('*It gets louder as it approaches you*\n'.center(columns))
    time.sleep(3)

    print('*A figure jump out of the bush, wielding a sword.*\n'.center(columns))
    time.sleep(3) # First Interaction with other characters.

    print('"YOU BEAST ILL GET YOU"\n'.center(columns))
    time.sleep(3)

    print('"Wait . . ."\n'.center(columns))
    time.sleep(3)

    print('"Youre no monster. . . ."\n'.center(columns))
    time.sleep(3)

    print('"So uhhh . . . anyways, Im Dime, and you are?"\n'.center(columns))
    time.sleep(3.5)

    print(f'I am {name}'.center(columns))
    time.sleep(4)

    clear_console()

    print(f'Partner created with name: {dime.user} and health: {dime.health} and race: {dime.race.name}'.center(columns))#new character
    time.sleep(5)
    clear_console()



    print('The Story Continues . . . '.center(columns))  # Story Continuation
    time.sleep(4)
    clear_console()

    print(f'"Thats a lovely name. {name}, I love it!"\n'.center(columns))
    time.sleep(3)

    print('"Anyways . . . I need your help. And i need it now."\n'.center(columns))
    time.sleep(3)

    print('"Are you up for the Challenge?"\n'.center(columns))
    time.sleep(2)
    first_no = centered_input()
    time.sleep(3)   # No Matter whats said, its a yes so storyc an continue

    if first_no.lower() in ['no', 'nah', 'nope', 'nuhuh', 'nuh huh', 'nuh uh', 'nop', 'nup']:
        print('Too bad'.center(columns))
        time.sleep(2)
    print('\n')    
    print('"Sounds like a Yes to me!"\n'.center(columns))
    time.sleep(3)



    # Main point of story. To save Helga.
    print('"Im getting side tracked here, there are more important measures at stake"\n'.center(columns))
    time.sleep(3)

    print('"Its . . . "\n'.center(columns))
    time.sleep(3)

    print('"Its . . My friend Helga, shes been uhh . . . "\n'.center(columns))
    time.sleep(3)

    print('"Kidnapped."\n'.center(columns))
    time.sleep(3)

    print('"Are you still able to help me?"\n '.center(columns))
    second_no = centered_input().lower()
    time.sleep(3) # same as before

    if first_no.lower() in ['no', 'nah', 'nope', 'nuhuh', 'nuh huh', 'nuh uh', 'nop', 'nup']:
        print('\n')
        print('Too bad\n'.center(columns))
        time.sleep(2)

    print('\n')

    print('"Still sounds like a Yes to me!'.center(columns))
    time.sleep(6)

    clear_console()
    print(f'Where Should we go first {name}?'.center(columns))
    time.sleep(4)