from settings import *


def choose_path(player, dime, tree):
#path choosing, defined so it can be called back on to come back to.
    player_health = player.health
    global enter
    os.system('cls' if os.name == 'nt' else 'clear')

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
                print('"You have already killed teh beast that is here"\n'.center(columns))
                time.sleep(3)
                print('"Go Back. We have to save Helga"\n'.center(columns))
                time.sleep(3)
                print('     Feeling like an idiot, you turn around and go back'.center(columns))
                time.sleep(3)
                return choose_path(player, dime, tree)
            

            print('You venture into the forest, you hear whispers...\n'.center(columns))
            time.sleep(3)

            print('“So, what makes you want to go through the forest?”\n'.center(columns))
            input(' ' * ((columns - 3) // 2) + '>> ')
            time.sleep(3)

            print('“Uh huh . . . Okay . . . Whatever you say, Brochacho.”\n'.center(columns))
            time.sleep(3)

            print('*bsh bhs bsh*'.center(columns))
            time.sleep(3)

            tree_ascii = '''


                                                         .
                                              .         ;  
                 .              .              ;%     ;;   
                   ,           ,                :;%  %;   
                    :         ;                   :;%;'     .,   
           ,.        %;     %;            ;        %;'    ,;
             ;       ;%;  %%;        ,     %;    ;%;    ,%'
              %;       %;%;      ,  ;       %;  ;%;   ,%;' 
               ;%;      %;        ;%;        % ;%;  ,%;'
                `%;.     ;%;     %;'         `;%%;.%;'
                 `:;%.    ;%%. %@;        %; ;@%;%'
                    `:%;.  :;bd%;          %;@%;'
                      `@%:.  :;%.         ;@@%;'   
                        `@%.  `;@%.      ;@@%;         
                          `@%%. `@%%    ;@@%;        
                            ;@%. :@%%  %@@%;       
                          %@bd%%%bd%%:;     
                      ((o))((o));
                      @@%@@%%%::;
                                   (MOUTH :p);  . '         
                                %@@@o%;:(.,'         
                         `.. %@@@o%::;         
                           `)@@@o%::;         
                            %@@(o)::;        
                           .%@@@@%::;         
                           ;%@@@@%::;.          
                    ;%@@@@%%:;;;. 
                ...;%@@@@@%%:;;;;,..  
'''
            #Split lines and calculate vertical centering
            tree_lines = tree_ascii.strip('\n').split('\n')
            vertical_padding = (rows - len(tree_lines)) // 2 # ( ChatGPT aswell)


            # Print empty lines to vertically center
            print('\n' * vertical_padding)

            # Print each line centered horizontally
            for line in tree_lines:
                print(line.center(columns))

            # Pause before transitioning
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')# clean screar


            while True:                                                                    
                print('You see a Walking Tree. You can either:'.center(columns))
                print('a) Fight it'.center(columns))
                print('b) Go back'.center(columns))
                print('c) Befriend it'.center(columns))
                print('d) Check your Inventory'.center(columns))

                time.sleep(3)  
                fight = input(' ' * ((columns - 3) // 2) + '>> ').lower()
                time.sleep(3)

                if fight == 'a':
                    print('You get your weapon ready and engage in battle... against a tree?\n\n'.center(columns))
                    time.sleep(3)
                    print('   You attack the Tree and it smacks you back'.center(columns))
    
                    # Health exchange
                    player.take_damage(tree.damage)
                    tree.health -= player.weapon_damage

                     #if tree has lets say -20, its displayed as 0
                    if tree.health < 0:
                        tree.health = 0


                    # Show health updates
                    print(f"{player.user}'s health: {player.health}".center(columns))
                    print(f"{tree.user}'s health: {tree.health}".center(columns))
                    time.sleep(3)

                    
                     
                    # If the Tree is dead
                    if tree.health == 0:
                        print('\n\n     *THUD*. The tree drops.'.center(columns))
                        print("     It dropped some items.".center(columns))
        
                    for item in tree.drop_items:
                        player.add_to_inventory(item)

                    
                    while True:
                        print('You keep walking through the forest.'.center(columns))
                              
                        print('What do you want to do?'.center(columns))
                        print('a) Go back'.center(columns))
                        print('b) Check inventory'.center(columns))
                              
                        choice = input(' ' * ((columns - 3) // 2) + '>> ').lower()

                        if choice in ['a', 'go back']:
                            print("You head back the way you came...\n".center(columns))
                            return choose_path(player, dime, tree)
                        elif choice in ['b', 'check inventory']:
                            player.print_inventory()

                        else:
                            print("Invalid option. Try again.\n".center(columns))



                elif fight == 'b':
                    print('You decide to retreat... Bok Bok!'.center(columns)) # Chicken
                    return choose_path(player, dime, tree)


                elif fight == 'c':
                    print('You try to befriend the tree... and it attacks you!\n'.center(columns))
                    time.sleep(3)
                    player.take_damage(20) #     Higher then Enemy(TREE) normal damage because it was 'Unexpected'

                    print(f'Your Health is now: {player.health}'.center(columns))
                    time.sleep(3)
                    print('The tree still stands there, rustling ominously...'.center(columns))
                    time.sleep(3)

                elif fight == 'd':
                    player.print_inventory()
                    time.sleep(3)

                else:
                    print("That’s not a valid option. Try again.".center(columns))



        # NEW CHOICE
        elif choice == 'b':
            time.sleep(3)
            
            print('     *Squish, Squash*\n'.center(columns))
            time.sleep(3)

            print('"The Grass sure is wet here"\n'.center(columns))
            time.sleep(3)

            print('Yeah, I guess\n'.center(columns))
            time.sleep(.5)

            print('"LOOK OVER THERE"\n'.center(columns))
            time.sleep(3)

            print('     You and Dime look into the Distance and see your first challenge in the field of Foe\n'.center(columns))
            time.sleep(3)

            print('     2 doors, The Left Door, and The Right Door.\n'.center(columns))
            time.sleep(3)

            print('     The only other thing you can see is a sign.\n'.center(columns))
            time.sleep(4)

            os.system('cls' if os.name == 'nt' else 'clear') 
            print(r"""
   _________________________                                                           _________________________
  /                         \                                                         /                          |
 /     left                  |                                                       /            Right          |                                                       
 +----------------------------+                                                      +----------------------------+
 |                            |                                                      |                            |
 |                            |                                                      |                            |
 |                            |                                                      |                            |
 |                            |                                                      |                            |
 |                            |                                                      |                            |
 |                           (|            _________________                         |                           (|
 |                            |            |      This     |                         |                            |
 |                            |            |       is      |                         |                            |
 |                            |            |       a       |                         |                            |
 |                            |            |      sign     |                         |                            |
 |                            |            |_______________|                         |                            |
 |                            |                    |                                 |                            |
 |                            |                    |                                 |                            |
 +----------------------------+                    |                                 +----------------------------+
___________________________________________________________________________________________________________________

                    """)
            time.sleep(5)
            os.system('cls' if os.name == 'nt' else 'clear')

            print('Upon getting closer, you can read the sign.\n\n'.center(columns))
            time.sleep(3)

            print('"Answer my riddle three, and leave your fate up to me"'.center(columns))
            time.sleep(2)
            print('"Behind the one of the doors is a Foe, and behind the other you wont know."'.center(columns))
            time.sleep(4)

            print('"The sign says only one contains an enemy, that means the other one wont"\n'.center(columns))
            time.sleep(3)

            print('     "Your First Ridd-"\n'.center(columns))
            time.sleep(3)

            print('"Shut up, now as i was saying. it says only one contains an enemy"'.center(columns))
            print('"I say that gives us good odds to enter one"\n'.center(columns))
            time.sleep(3)

            print('I guess youre right Dime.\n'.center(columns))
            time.sleep(3)

            print('What door do you open?'.center(columns))
            print('a) The left door'.center(columns))
            print('b) The right door'.center(columns))
                
            door = input(' ' * ((columns - 3) // 2) + '>> ').lower()
                
            if door == 'a':
                time.sleep(3)
                print('     "Hmm the Left door, Without my riddles? . . .  Ouch."\n'.center(columns))
                time.sleep(3)
                print('     "The left door contains a battle!" '.center(columns))
                time.sleep(2)
                print('You see a . . . short guy named Barry wielding a stick?'.center(columns))
                time.sleep(3)
                print('You can either:'.center(columns))
                print('a) Fight him'.center(columns))
                print('b) Go back'.center(columns))

                while True:
                    if barry.health == 0:
                        print('YOU KILLED HIM')

                    fight1 = input(' ' * ((columns - 3) // 2) + '>> ').lower()
                    time.sleep(3)
                    if fight1 == 'a':
                        print('\n\n')
                        print('You get youre weapon ready to against Barry and the "Stick of Anquish" \n\n'.center(columns))
                        time.sleep(3)

                        print('   You attack the Barry and he begins to cry and starts throwing his stick around like a little kid and it nicks you'.center(columns))
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
