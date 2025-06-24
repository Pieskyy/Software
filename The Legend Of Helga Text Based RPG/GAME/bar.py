from settings import *

def swoosh(): # cowboy door for tavern. This functions holds the ascii art of said door
    clear_console()
    swoosh_ascii = '''       
          =========#%%%%*                                                 :#%%%%#+========          
          =========#%%##*                                                 :#%%%%#=========                   
          =========#%%%%*                :==+++++#++****=.                :%%%%%#=========          
          =========*%%%%*****+=======+++++++++++*#***********+===---=***#*=%%%%%#+========          
          =========*%%%%**+**********************#************************=%%%%%#=========          
          -=--=====#%%%%**+***%%%%%%%%%%%%%%%%***#***#%%%%%%%%%%%%%%%***=+=%%%%%#=========          
          =-=======*%%%%#*+***%%%%%%%%%%%%%%%%***#***#%%%%%%%%%%%%%%%#**++=%%%%%*=========          
          -=--=====#%%%%#*****%%%%%%%%%%%%%%%%***%****%%%%%%%%%%%%%%%###%*=%%%%%#=========          
          ---=-====#%%%%#*****%%%%%%%%%%%%%%%%***#***#%%%%%%%%%%%%%%%**#%#+%%%%%*=========          
          --=-=====*%%%%#*****%%%%%%%%%%%%%%%%***#***#%%%%%%%%%%%%%%%###%#+%%%%%#=========          
          -----====#%%%%#********#############***%*********#############%%+%%%%%*=========          
          -----====#%%%%#*******##############*+*%******##############%%%%+%%%%%*=========          
          -----====*%%%%#**************#*********%*************#*****###%%+%%%%%*=========          
          ------===#%%%%#********##*##########***%****#*################%%+%%%%%*=========          
          -----=-==*%%%%#******##############****%****##################%%+%%%%%*=======-=          
          -----====*%%%%#****#%%%%%%%%%%%%%%%%***%***#%%%%%%%%%%%%%%%%%%%%+%%%%%*========-          
          ------===*%%%%#****#%%%%%%%%%%%%%%%%***%***#%%%%%%%%%%%%%%%%%%%%+%%%%%*========-          
          ------===*%%%%%****#%%%%%%%%%%%%%%%%***%##*#%%%%%%%%%%%%%%%##%%%+%%%%%*====-=-=-          
          -------==*%%%%#*#*##%%%%%%%%%%%%%%%%#*#%####%%%%%%%%%%%%%%%%#%%%+%%%%%*=====----          
          ------===*%%%%%****#********########*##%####*******#########*#+#+%%%%%*===--=---          
          -------==*%%%%%***#################*###%####################*#*#+%%%%%*===------          
          :-:----==*%%%%%*#**#*################*#%###########********##%%%+%%%%%*==-------          
          ::-----==*%%%%%***********=-:.      :::::::      ..:=*****##%%%%+%%%%%*===------          
          :::----==*%%%%%+++*=-::                                 .:-=****=%%%%%*==------:          
          ::::---==*%%%%#                                                 :%%%%%#==---:-::          
                 :-:----==*%%%%#    Like a bar door used in cowboy movies:p      :%%%%%#==---::::                                                                                                              
        '''
    swoosh_lines = swoosh_ascii.strip('\n').split('\n')
    vertical_padding = (rows - len(swoosh_lines)) // 2
    print('\n' * vertical_padding)
    for line in swoosh_lines:
        print(line.center(columns))
    time.sleep(5)
    clear_console()

def enter_bar(player, dime, tree): # Holds output of first entering bar and checks to make sure its you first, if 2nd or more, prints other stuff
    from choice import choose_path
    clear_console()
    global enter

    swoosh()

    if enter == 1: # If you've already entered.
        print('*swish swoosh*\n'.center(columns))
        time.sleep(3)

        print('"You Again? I Already told you, Trowser is in the Field of Foe" - Cad Bane\n'.center(columns))
        time.sleep(3)

        print('"Dude we have already been here, why did you come back"\n'.center(columns))
        time.sleep(3)

        print('     You exit the bar'.center(columns))
        time.sleep(3)

        return choose_path(player, dime, tree)
    

    enter += 1

    print('*swish swoosh*\n'.center(columns))
    time.sleep(3)

    print('You step into the tavern, the smell of ale and stories thick in the air...\n'.center(columns))
    time.sleep(3)

    print('*You hear* \n'.center(columns))
    time.sleep(1)

    print('"NO WEAPONS"\n'.center(columns))
    time.sleep(1)

    print('Yelled across the bar from the Bartender\n'.center(columns))
    time.sleep(1)

    print('You Put your weapons at the door and continue walking in with Dime. \n'.center(columns))
    time.sleep(3)

    print('You sit down at the bar and order a drink\n'.center(columns))
    time.sleep(3)

    print('"Eyy What are you here for? - stranger"\n'.center(columns))
    time.sleep(3)

    print('"something you need? You arent our usual folk" - stranger\n'.center(columns))
    time.sleep(3)

    print('I uhh . . .  We are . . .\n '.center(columns))
    time.sleep(3)

    print('"Someone we know was kidnapped. we need infomation."\n'.center(columns))
    time.sleep(3)

    print('Yeah, what he said\n'.center(columns))
    time.sleep(3)

    print('*The stranger chewing on a tooth pick*\n.'.center(columns))
    time.sleep(3)

    print('"I Think i can be of service" - stranger \n'.center(columns))
    time.sleep(3)

    print('*Tips his cowboy hat down to you*\n'.center(columns))
    time.sleep(3)

    print('"First im going to need some names." - stranger\n'.center(columns))
    time.sleep(2.5)

    print(f'"Im Dime and he is {player.user} we are looking some by the name Helga"\n'.center(columns))
    time.sleep(3)

    print('*Still chewing tooth pick but moves it to other side*\n'.center(columns))
    time.sleep(3)

    print('"That rings a bell, Helga. I might be able to help" - stranger\n'.center(columns))
    time.sleep(3)

    print('Thanks, We never got you name.\n'.center(columns))
    time.sleep(3)

    print('"Bane, Cad Bane" - stranger\n'.center(columns))
    time.sleep(3)

    print('"Go sit in that booth there and wait for me" - Cad Bane\n'.center(columns))  # totally not a taken name
    time.sleep(3)

    print('*You and Dime walk to the booth at which Bane pointed at and wait*\n'.center(columns))
    time.sleep(3)

    clear_console()
    print('"Who is this Helga to you" - Cad Bane\n'.center(columns))

    question(player, dime, tree)

def question(player, dime, tree): # THe questions that are asked
    while True:
        print('a) I dont know her, Dimes friend'.center(columns))
        print('b) Our Friend'.center(columns))
        print('c) My Mother'.center(columns))
        print('d) Thats not of your concern'.center(columns))\
        
        stranger = centered_input()
              
        time.sleep(3)
        clear_console()

        if stranger == 'a': # if answer == so and so, do this function
            pet(player, dime, tree)

        elif stranger == 'b':
            friend(player, dime, tree)

        elif stranger == 'c':
            mother(player, dime, tree)

        elif stranger == 'd':
            grumpy(player, dime, tree)

        else:
            print('Invalid input. Try again.'.center(columns))


def pet(player, dime, tree): # question 1
    print('What are you some pet?" - Cad Bane'.center(columns))
    print('a) Yes'.center(columns))
    print('b) No'.center(columns))
    
    pet = centered_input()
    print('\n')
    time.sleep(3)

    if pet == 'b':
        print('"Whatever you say. - Cad Ban\n'.center(columns))
        time.sleep(3)
        trowser(player, dime, tree)

    elif pet == 'a':
        print('"Uhhhhh . . . ." - Cad Bane\n'.center(columns))
        time.sleep(3)
        print('Will you still help us?\n'.center(columns))
        time.sleep(3)
        print('"I Guess" - Cad Bane\n'.center(columns))
        time.sleep(3)
        trowser(player, dime, tree)
    else:
        print('"Weird way to answer a yes or no question" - Cad Bane\n'.center(columns))
        time.sleep(3)
        trowser(player, dime, tree)


def friend(player, dime, tree): # question 2
    print('"I Doubt she is friends with YOU." - Cad Bane\n'.center(columns))
    time.sleep(3)
    trowser(player, dime, tree)


def mother(player, dime, tree): # question 3
    print('"Oh Really? Shes YOUR mother? She had no kids idiot\n" - Cad Bane'.center(columns))
    time.sleep(3)
    trowser(player, dime, tree)


def grumpy(player, dime, tree): # question 4
    print('"Oh Mr Grumpy pants over here." - Cad Bane\n'.center(columns))
    time.sleep(3)
    trowser(player, dime, tree)


def trowser(player, dime, tree): # where the boss is locatated 
    from choice import choose_path
    clear_console()
    print('"Helga was taken by a Humaniod Turtle called Trowser" - Cad Bane'.center(columns))
    time.sleep(3)

    
    print('a) Trowser?'.center(columns))
    print('b) Ive heard of him. Where is he?'.center(columns))
    whereabouts = centered_input()
    time.sleep(3)
    print('\n')

    if whereabouts == 'a':
        print('"The Humanoid Turtle? I just said that, anyways, go through the Field of Foe" - Cad Bane\n'.center(columns))
        time.sleep(3)
        return choose_path(player, dime, tree)

    elif whereabouts == 'b':
        print('"I doubt you of all people have heard of him. He can be found in the Field of Foe" - Cad Bane\n'.center(columns))
        time.sleep(3)
        return choose_path(player, dime, tree)
    else:
        print('"Weird way to answer a yes or no question - Cad Bane\n"'.center(columns))
        time.sleep(3)
        return trowser(player, dime, tree)
