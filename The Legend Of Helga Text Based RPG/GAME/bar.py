from settings import *

def enter_bar(player, dime, tree, enter):
    from fights import choose_path


    if enter == 1: # If you've already entered.
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
    print('Yelled across the bar from the Bartender\n')
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
    print('     "Bane, Cad Bane"\n\n      "Go sit in that booth there and wait for me"')  # totally not a taken name
    time.sleep(3)
    print('     *You and Dime walk to the booth at which Bane pointed at and wait*\n\n')
    time.sleep(0.81)
    print('     "Who is this Helga to you"')

    question(player, dime, tree)


def question(player, dime, tree):
    while True:
        stranger = input('''
        a) I dont know her, Dimes friend
        b) Our Friend
        c) My Mother
        d) Thats not of your concern
        ''').lower()
        time.sleep(3)

        if stranger == 'a':
            pet(player, dime, tree)

        elif stranger == 'b':
            friend(player, dime, tree)

        elif stranger == 'c':
            mother(player, dime, tree)

        elif stranger == 'd':
            grumpy(player, dime, tree)

        else:
            print('Invalid input. Try again.'.center(columns))


def pet(player, dime, tree):
    pet = input('''        '     "What are you some pet?"
        a) Yes
        b) No
           ''').lower()
    time.sleep(3)

    if pet == 'b':
        print('     "Whatever you say.')
        time.sleep(3)
        trowser(player, dime, tree)

    elif pet == 'a':
        print('     "Uhhhhh . . . ."')
        time.sleep(3)
        print('Will you still help us?')
        time.sleep(3)
        print('     "I Guess"')
        time.sleep(3)
        trowser(player, dime, tree)
    else:
        print('     "Weird way to answer a yes or no question"')
        time.sleep(3)
        trowser(player, dime, tree)


def friend(player, dime, tree):
    print('I Doubt she is friends with YOU.')
    time.sleep(3)
    trowser(player, dime, tree)


def mother(player, dime, tree):
    print('     "Oh Really? Shes YOUR mother? She had no kids idiot\n"')
    time.sleep(3)
    trowser(player, dime, tree)


def grumpy(player, dime, tree):
    print('     "Oh Mr Grumpy pants over here."')
    time.sleep(3)
    trowser(player, dime, tree)


def trowser(player, dime, tree):
    from fights import choose_path
    print('     "Helga was taken by a Humaniod Turtle called Trowser"')
    time.sleep(3)

    trowser = input('''
    a) Trowser?
    b) Ive heard of him. Where is he?
    ''').lower()
    time.sleep(3)

    if trowser == 'a':
        print('     "The Humanoid Turtle? I just said that, anyways, go through the Field of Foe"')
        time.sleep(3)
        return choose_path(player, dime, tree)

    elif trowser == 'b':
        print('        "I doubt you of all people have heard of him. He can be found in the Field of Foe"')
        time.sleep(3)
        return choose_path(player, dime, tree)
    else:
        print('     "Weird way to answer a yes or no question"')
        time.sleep(3)
        return trowser(player, dime, tree)
