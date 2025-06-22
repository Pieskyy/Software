from settings import *
import shutil
import time
import os

def start():
        columns, rows = shutil.get_terminal_size()


        # Clear screen 
        clear_console()# ( chatGPT https://chatgpt.com/c/684ea48f-fd48-800b-a4aa-bfea96e06e38)

        # ASCII Art as string
        ascii_art = """
████████╗██╗  ██╗███████╗     ██╗     ███████╗ ██████╗ ███████╗███╗   ██╗██████╗      ██████╗ ███████╗
╚══██╔══╝██║  ██║██╔════╝     ██║     ██╔════╝██╔════╝ ██╔════╝████╗  ██║██╔══██╗    ██╔═══██╗██╔════╝
   ██║   ███████║█████╗       ██║     █████╗  ██║  ███╗█████╗  ██╔██╗ ██║██║  ██║    ██║   ██║█████╗  
   ██║   ██╔══██║██╔══╝       ██║     ██╔══╝  ██║   ██║██╔══╝  ██║╚██╗██║██║  ██║    ██║   ██║██╔══╝  
     ██║   ██║  ██║███████╗     ███████╗███████╗╚██████╔╝███████╗██║ ╚████║██████╔╝    ╚██████╔╝██╗      
     ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝      ╚═════╝ ╚═╝      

██╗  ██╗███████╗██╗      █████╗   █████╗ 
██║  ██║██╔════╝██║     ██╔═══╝   ██╔══██╗
███████║█████╗  ██║     ██║  ███╗ ███████║
██╔══██║██╔══╝  ██║     ██║   ██║ ██╔══██║
██║  ██║███████╗███████╗╚██████╔╝ ██║  ██║
╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝  ╚═╝  ╚═╝

        """


        # Split lines and calculate vertical centering
        ascii_lines = ascii_art.strip('\n').split('\n')
        vertical_padding = (rows - len(ascii_lines)) // 2 # ( ChatGPT aswell)


        # Print empty lines to vertically center
        print('\n' * vertical_padding)

        # Print each line centered horizontally
        for line in ascii_lines:
            print(line.center(columns))

        # Pause before transitioning
        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')# clean screar

        # Print selection screen title at top (not vertically centered)
        print('______________________________________SELECTION_SCREEN______________________________________'.center(columns))
        print('\n' * 3)  # Some spacing under the heading



        print('What do you wish to be called?: \n'.center(columns) )  # Input a word of sorts, Becomes name.
        name = centered_input # ChatGPT help

        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        print('\n' * 3)
        print('Possible Races:'.center(columns))
        # 'Viewable' Races, Theres 2 hidden ones. Grug as Tribute and No for annoying people.

        race_selection ='''   
        Human:
            Strength: 5
            Health: 100
            
        Elf:
            Strength: 3
            Health: 90
            
        Orc:
            Strength: 9
            Health: 120
            
        Dwarf:
            Strength: 7
            Health: 130
            
        Worm:
            Strength: 6
            Health: 95

            '''

        race_select = race_selection.strip('\n').split('\n')

        # Print each line centered horizontally
        for line in race_select:
            print(line.center(columns))
        
        # List of races from dictionary in settings
        valid_races = list(races.keys())

        while True:     # loop
            print('So what race do you wish to be?\n'.center(columns))

            race_input = centered_input              # Get input from user
            race_input = race_input.lower()  # Make input lowercase
            
            if race_input in valid_races:          # Check if input is valid
                break                             # Exit the loop if valid
            else:
                print('Invalid race. Please choose from: Human, Elf, Orc, Dwarf, Worm'.center(columns))

        chosen_race = races[race_input]
        time.sleep(3)

        dime = Dime()   # so you can do thinks like player.user etc later on
        player = Player(name, chosen_race)

        os.system('cls' if os.name == 'nt' else 'clear')
        print(f'Player created with name: {player.user} and race: {player.race.name} and health: {player.health} '.center(columns))
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        # Hint like screen
        print('"TEXT" Refers to other characters. if without "", it is your Character. \n\n\n\n\n'.center(columns))
        print('(FOR BEST EXPIRENCE PLAY IN FULL SCREEN)\n\n\n\n\n'.center(columns))
        print('Thanks Mathew for helping with printing inventory <3'.center(columns))

        time.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')

        return player, dime
