from settings import *


# Get terminal dimensions
columns, rows = shutil.get_terminal_size()

# Clear screen 
os.system('cls' if os.name == 'nt' else 'clear') # ( chatGPT https://chatgpt.com/c/684ea48f-fd48-800b-a4aa-bfea96e06e38)

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
name = input(' ' * ((columns - 3) // 2) + '>> ') # ChatGPT help

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


print('______________________________________SELECTION_SCREEN___________________________________'.center(columns))

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

    race_input = input(' ' * ((columns - 3) // 2) + '>> ')              # Get input from user
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


# Back story lore ish idk
print('You are in a forest. Chopping wood. When suddenly you hear . . .\n\n'.center(columns))

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
os.system('cls' if os.name == 'nt' else 'clear')

#new character
print(f'Partner created with name: {dime.user} and health: {dime.health} and race: {dime.race.name}'.center(columns))
time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')



print('The Story Continues . . . '.center(columns))  # Story Continuation
time.sleep(4)
os.system('cls' if os.name == 'nt' else 'clear')


print(f'"Thats a lovely name. {name}, I love it!"\n'.center(columns))

time.sleep(3)
print('"Anyways . . . I need your help. And i need it now."\n'.center(columns))
time.sleep(3)

print('"Are you up for the Challenge?"\n'.center(columns))
first_no = input(' ' * ((columns - 3) // 2) + '>> ')
time.sleep(3)   # No Matter whats said, its a yes so storyc an continue

if first_no.lower() in ['no', 'nah', 'nope', 'nuhuh', 'nuh huh', 'nuh uh', 'nop', 'nup']:
    print('Too bad\n'.center(columns))
    time.sleep(2)
    

print('"Sounds like a Yes to me!"\n'.center(columns))
time.sleep(3)



# Main point of story. To save Helga.
print('"Im getting side tracked here, there are more important measures at stake"\n'.center(columns))
time.sleep(3)

print('"Its . . . "'.center(columns))
time.sleep(3)

print('"Its . . My friend Helga, shes been uhh . . . "\n'.center(columns))
time.sleep(3)

print('"Kidnapped."\n'.center(columns))
time.sleep(3)

print('"Are you still able to help me?"\n '.center(columns))
second_no = input(' ' * ((columns - 3) // 2) + '>> ').lower()
time.sleep(3) # same as before

if first_no.lower() in ['no', 'nah', 'nope', 'nuhuh', 'nuh huh', 'nuh uh', 'nop', 'nup']:
    print('Too bad\n'.center(columns))
    time.sleep(2)

print('\n')
time.sleep(2)
print('"Still sounds like a Yes to me!'.center(columns))
time.sleep(6)

os.system('cls' if os.name == 'nt' else 'clear')
print(f'Where Should we go first {name}?'.center(columns))
time.sleep(4)
os.system('cls' if os.name == 'nt' else 'clear')


enter = 0  # Set initial value for Bar

#path choosing, defined so it can be called back on to come back to.
def choose_path(player, dime, tree):
    player_health = player.health
    global enter

    while True:
        print('______________________________________________ WHERE TO ______________________________________________'.center(columns))
        print('\n' * 3)
        print('Where will you go?'.center(columns))
        print('\n')
              
        print('a) Through the Forest?'.center(columns))
        print('b) To the Field of Foe?'.center(columns))
        print('c) The Tavern of Many?'.center(columns))


        choice = input(' ' * ((columns - 3) // 2) + '>> ').lower()
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')

        if choice == 'a':

            #if you have already killed tree
            if tree.health == 0:
                print('"You have already killed teh beast that is here"\n')
                time.sleep(3)
                print('"Go Back. We have to save Helga"\n')
                time.sleep(3)
                print('     Feeling like an idiot, you turn around and go back')
                time.sleep(3)
                return choose_path(player, dime, tree)
            

            print('You venture into the forest, you hear whispers...\n')
            time.sleep(3)

            print('“So, what makes you want to go through the forest?”\n')
            input(' ' * ((columns - 3) // 2) + '>> ')
            time.sleep(3)

            print('\n“Uh huh . . . Okay . . . Whatever you say, Brochacho.”\n')
            time.sleep(3)

            print('*bsh bhs bsh*')
            time.sleep(3)

            while True:                                                                    
                print('''
You see a Walking Tree. You can either:
                      

    a) Fight it
    b) Go back
    c) Befriend it
    d) Check your Inventory
                      
                      
                    ''')
                time.sleep(3)  
                fight = input('>> ').lower()

                if fight == 'a':
                    print('You get your weapon ready and engage in battle... against a tree?\n\n')
                    time.sleep(3)
                    print('   You attack the Tree and it smacks you back')
    
                    # Health exchange
                    player.take_damage(tree.damage)
                    tree.health -= player.weapon_damage

                     #if tree has lets say -20, its displayed as 0
                    if tree.health < 0:
                        tree.health = 0


                    # Show health updates
                    print(f"{player.user}'s health: {player.health}")
                    print(f"{tree.user}'s health: {tree.health}")
                    time.sleep(3)

                    
                     
                    # If the Tree is dead
                    if tree.health == 0:
                        print("\n\n     *THUD*. The tree drops.")
                        print("     It dropped some items.")
        
                    for item in tree.drop_items:
                        player.add_to_inventory(item)

                    
                    while True:
                        print(''' 
                              
You keep walking through the forest.
                              
What do you want to do?
    a) Go back
    b) Check inventory
                              ''')
                              
                        choice = input(">> ").lower()

                        if choice in ['a', 'go back']:
                            print("You head back the way you came...\n")
                            return choose_path(player, dime, tree)
                        elif choice in ['b', 'check inventory']:
                            player.print_inventory()

                        else:
                            print("Invalid option. Try again.\n")



                elif fight == 'b':
                    print('You decide to retreat... Bok Bok!') # Chicken
                    return choose_path(player, dime, tree)


                elif fight == 'c':
                    print('You try to befriend the tree... and it attacks you!\n')
                    time.sleep(3)
                    player.take_damage(20) #     Higher then Enemy(TREE) normal damage because it was 'Unexpected'

                    print(f'Your Health is now: {player.health}')
                    time.sleep(3)
                    print('The tree still stands there, rustling ominously...')
                    time.sleep(3)

                elif fight == 'd':
                    player.print_inventory()
                    time.sleep(3)

                else:
                    print("That’s not a valid option. Try again.")



        # NEW CHOICE
        elif choice == 'b':
            time.sleep(3)
            
            print('     *Squish, Squash*\n')
            time.sleep(3)

            print('"The Grass sure is wet here"\n')
            time.sleep(3)

            print('Yeah, I guess\n')
            time.sleep(.5)

            print('"LOOK OVER THERE"\n')
            time.sleep(3)

            print('     You and Dime look into the Distance and see your first challenge in the field of Foe\n')
            time.sleep(3)

            print('     2 doors, The Left Door, and The Right Door.\n')
            time.sleep(3)

            print('     The only other thing you can see is a sign.\n')
            time.sleep(3)

            print('     You must be closer to read the sign)\n')
            time.sleep(4)


            print('\n' * 50)# screen clear 
            print("""
    _________________________                                                           _________________________
   /                         \                                                         /                         |
  /     left                 |                                                       /            Right           |                                                       
 +----------------------------+                                                      +----------------------------+
 |                            |                                                      |                            |
 |                            |                                                      |                            |
 |                            |                                                      |                            |
 |                            |                                                      |                            |
 |                            |                                                      |                            |
 |                           (|                                                      |                           (|
 |                            |            _________________                         |                            |
 |                            |            |               |                         |                            |
 |                            |            |               |                         |                            |
 |                            |            |               |                         |                            |
 |                            |            |_______________|                         |                            |
 |                            |                    |                                 |                            |
 |                            |                    |                                 |                            |
 +----------------------------+                    |                                 +----------------------------+
___________________________________________________________________________________________________________________
""")

            time.sleep(5)
            print('\n' *5)

            print('Upon getting closer, you can read the sign.\n\n')
            time.sleep(3)

            print('        "Answer my riddle three, and leave your fate up to me\n        Behind the one of the doors is a Foe, and behind the other you wont know."\n\n')
            time.sleep(4)

            print('"The sign says only one contains an enemy, that means the other one wont\n')
            time.sleep(3)

            print('     "Your First Ridd-"\n')
            time.sleep(3)

            print('"Shut up, now as i was saying. it says only one contains an enemy\n\n I say that gives us good odds to enter one"\n')
            time.sleep(3)

            print('I guess youre right Dime.\n')
            time.sleep(3)

            print('''
What Door do you open?
    a) The Left door
    b) The Right door
                  
                  ''')
            
            door = input('>> ')
            
            if door == 'a':
                time.sleep(3)
                print('     "Hmm the Left door, Without my riddles? . . .  Ouch."\n')
                time.sleep(3)
                print('     "The left door contains a battle!" ')
                print('''
You see a . . . short guy named Barry wielding a stick?

You can either:
    a) Fight him
    b) Go back
                      ''')
                
                fight1 = input

                if fight1 == 'a':
                    print('\n\n     You get youre weapon ready to against Barry and the "Stick of Anquish" \n\n')
                    time.sleep(3)

                    print('   You attack the Barry and he begins to cry and starts throwing his stick around like a little kid and it nicks you')
                    time.sleep(3)

                    print('   You do ', player.weapon_damage, ' to Barry, and he does ', barry.damage, ' back.')

                    player.take_damage(barry.damage)
                    barry.health -= player.weapon_damage
                    if barry.health < 0:
                        barry.health = 0

                    time.sleep(3)
    
                    print(f"you have {player.health} health left")
                    print(f"{barry.user} has {barry.health} left")
                    time.sleep(3)



            elif door == 'b':
                time.sleep(3)
                print('     "The Right door, Lets hope you made the RIGHT choice!"')

                time.sleep(3)
                print('     "The Right door is SAFE!, you may continue your venture!"')


            else:
                time.sleep(3)
                print(' . . . ')
                time.sleep(3)
                print(' . . . ')
                time.sleep(3)
                print('     "Uhhh dude, theres 2 doors. pick one"')
                time.sleep(3)
            break


            

        elif choice == 'c': 

            if enter == 1: # if youve already entered bar do . . .
                print('          *swish swoosh*\n')
                time.sleep(3)

                print('         "You Again? I Already told you, Trowser is in the Field of Foe"\n\n')
                time.sleep(3)

                print('"Dude we have already been here, why did you come back"\n')
                time.sleep(3)

                print('     You exit the bar')
                time.sleep(3)
                return choose_path(player, dime, tree)
            
            enter += 1
            
            
            print('          *swish swoosh*\n')
            time.sleep(3)
            
            print('          You step into the tavern, the smell of ale and stories thick in the air...\n')
            time.sleep(3)

            print('          You hear \n')
            print('          "NO WEAPONS"\n')
            print(           'Yelled across the bar from the Bartender\n')
            time.sleep(3)

            print('          You Put your weapons at the door and continue walking in with Dime. \n')
            time.sleep(3)

            print('          You sit down at the bar and order a drink\n')
            time.sleep(3)

            print('          "Eyy What are you here for?"\n')
            time.sleep(3)

            print('          "something you need? You arent our usual folk"\n')
            print('          - Someone sitting next to you on stool\n')
            time.sleep(3)

            print('I uhh . . .  We are . . .\n ')
            time.sleep(3)

            print('"Someone we know was kidnapped. we need infomation."\n')
            time.sleep(3)

            print('Yeah, what he said\n')
            time.sleep(3)

            print('          *The stranger chewing on a tooth pick*\n')
            time.sleep(3)

            print('          "I Think i can be of service"\n')
            time.sleep(3)

            print('          *Tips his cowboy like hat down to you"')
            time.sleep(3)

            print('\n         "First im going to need some names."')
            time.sleep(2.5)

            print('\n"Im Dime and he is ', player.user,', we are looking some by the name Helga"')
            time.sleep(3)

            print('     *Still chewing tooth pick but moves it to other side*\n')
            time.sleep(3)

            print('     "That rings a bell, Helga. I might be able to help"')
            time.sleep(3)

            print('Thanks, We never got you name.')
            time.sleep(3)

            print('     "Bane, Cad Bane"\n\n      "Go sit in that booth there and wait for me"')#totally not a taken name
            time.sleep(3)
            print('     *You and Dime walk to the booth at which Bane pointed at and wait*\n\n')
            time.sleep(.81)
            print('     "Who is this Helga to you"')

            while True:

                stranger = input('''
                a) I dont know her, Dimes friend
                b) Our Friend
                c) My Mother
                d) Thats not of your concern
                ''').lower()
                time.sleep(3)

                if stranger == 'a':

                    pet  = input('''        '     "What are you some pet?"
                    a) Yes
                    b) No
                       ''')
                    time.sleep(3)


                    if pet == 'b':

                        print('     "Whatever you say.')
                        time.sleep(3)

                        print('     "Helga was taken by a Humaniod Turtle called Trowser')
                        time.sleep(3)

                        trowser = input('''
                        a) Trowser?
                        b) Ive heard of him. Where is he?
                            ''')
                        
                        time.sleep(3)

                        if trowser == 'a':
                            print('     "The Humanoid Turle? i just said that, anyways, go through the fielf of foe"')
                            time.sleep(3)
                            return choose_path(player, dime, tree)
                        

                        elif trowser == 'b':
                            print('        "I doubt you of all people have heard of him. He can be found in the Field of Foe"')
                            time.sleep(3)
                            choose_path(player, dime, tree)



                    elif pet == 'a':

                        print('     "Uhhhhh . . . ."')
                        time.sleep(3)

                        print('Will you still help us?')
                        time.sleep(3)

                        print('     "I Guess"')
                        time.sleep(3)

                        print('     "Helga was taken by a Humaniod Turtle called Trowser')
                        time.sleep(3)
                        
                        trowser = input('''
                        a) Trowser?
                        b) Ive heard of him. Where is he?
                                ''')
                        
                        time.sleep(3)
                        if trowser == 'a':
                            print('     "The Humanoid Turle? i just said that, anyways, go through the fielf of foe"')
                            time.sleep(3)
                            return  choose_path(player, dime, tree)

                        elif trowser == 'b':
                            print('        "I doubt you of all people have heard of him. He can be found in the Field of Foe"')
                            time.sleep(3)
                            return choose_path(player, dime, tree)

                        else:
                            print('     "Wierd way to answer a yes or no question')
                            time.sleep(3)
                            print('     "Helga was taken by a Humaniod Turtle called Trowser')
                            time.sleep(3)
                            trowser = input('''
                        a) Trowser?
                        b) Ive heard of him. Where is he?
                            ''')
                            time.sleep(3)
                            if trowser == 'a':
                                print('     "The Humanoid Turle? i just said that, anyways, go through the fielf of foe"')
                                time.sleep(3)
                                return choose_path(player, dime, tree) 


                elif stranger == 'b':
                    print('     "Really? Shes friends with you? I dont buy it" ')
                    time.sleep(3)

                    print('     "Helga was taken by a Humaniod Turtle called Trowser')
                    time.sleep(3)

                    trowser = input('''
                    a) Trowser?
                    b) Ive heard of him. Where is he?
                        ''')
                    
                    time.sleep(3)

                    if trowser == 'a':
                        print('     "The Humanoid Turle? i just said that, anyways, go through the fielf of foe"')
                        time.sleep(3)
                        return choose_path(player, dime, tree)

                    elif trowser == 'b':
                        print('        "I doubt you of all people have heard of him. He can be found in the Field of Foe"')
                        time.sleep(3)
                        return choose_path(player, dime, tree)

                elif stranger == 'c':
                    print('     "Oh Really? Shes YOUR mother? She had no kids idiot\n"')
                    time.sleep(3)

                    print('     "Helga was taken by a Humaniod Turtle called Trowser')
                    time.sleep(3)

                    trowser = input('''
                    a) Trowser?
                    b) Ive heard of him. Where is he?
                        ''')
                    time.sleep(3)
                    if trowser == 'a':
                        print('     "The Humanoid Turle? i just said that, anyways, go through the fielf of foe"')
                        time.sleep(3)
                        return choose_path(player, dime, tree)

                    elif trowser == 'b':
                        print('        "I doubt you of all people have heard of him. He can be found in the Field of Foe"')
                        time.sleep(3)
                        return choose_path(player, dime, tree)


                elif stranger == 'd':
                    print('     "Oh Mr Grumpy pants over here."')
                    time.sleep(3)

                    print('     "Helga was taken by a Humaniod Turtle called Trowser')
                    time.sleep(3)
                    
                    trowser = input('''
                    a) Trowser?
                    b) Ive heard of him. Where is he?
                        ''')
                    time.sleep(3)

                    if trowser == 'a':
                        print('     "The Humanoid Turle? i just said that, anyways, go through the fielf of foe"')
                        time.sleep(3)
                        return choose_path(player, dime, tree)

                    elif trowser == 'b':
                        print('        "I doubt you of all people have heard of him. He can be found in the Field of Foe"')
                        time.sleep(3)
                        return choose_path(player, dime, tree)


                else:
                    print('Not an Option')
                    time.sleep(3)

            

            
        else:
            print("That’s not a valid choice. Try again.")

    return player_health

player_health = choose_path(player, dime, tree)
print(f"\nYou finished choosing a path. Your health is {player_health}. Game continues here...")
