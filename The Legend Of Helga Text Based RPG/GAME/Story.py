from settings import *












#________________________________________GAME_START_____________________________________
print('\n' * 30)#Screen Clear






#Title Screen
print(""" 
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
""")
time.sleep(5)
print('\n' * 30) #Screen Clear

#end Title Screen




print('______________________________________SELECTION_SCREEN___________________________________')
print('\n'*15)


name = input('What do you wish to be called?: ' + ('\n' * 10)) #Name
print('\n' * 10)







print('\n' * 30) #Screen Clear
print('______________________________________SELECTION_SCREEN___________________________________')







#Races
print('\n\n\n                                               POSSIBLE RACES')
print('Human:\n   Strength: 5\n   Health: 100\n')
print('Elf:\n   Strength: 3\n   Health: 90\n')
print('Orc:\n   Strength: 9\n   Health: 120\n')
print('Dwarf:\n   Strength: 7\n   Health: 130\n')
print('Worm:\n   Strength: 6\n   Health: 95\n\n\n')



race_input = ""
while race_input.lower() not in races:
    race_input = input('So what race do you wish to be?: ').strip().lower()
    if race_input not in races:
        print("Invalid race. Please choose from: Human, Elf, Orc, Dwarf, Worm")

chosen_race = races[race_input]
time.sleep(2)



print('\n' * 30)#Show of Stats so far
dime = Dime()
player = Player(name, chosen_race)
print(f"Player created with name: {player.user} and health: {player.health} and race: {player.race.name} ")
print('\n'*15)



time.sleep(3)


def choose_path(player, dime, tree):

    print('\n' * 30) #Screen Clear





#___________________________________HINT LIKE SCREEN____________________________________________



print('"TEXT" Refers to other characters. if without "", it is your Character.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
print(' Thanks Mathew for helping with printing inventory <3')
time.sleep(5)
print('\n' * 30) #Screen Clear



#_______________________________________________________________________________________________













#_________________________________________Story Start___________________________________________





#Back story lore ish idk
print('You are in a forest. chopping wood for a fire when suddenly you hear . . .\n\n')




time.sleep(2)
print('    *Bushes rustling in the distance, getting louder and louder as it approaches you*')




time.sleep(2)
print('    *You see a figure jump out of the bushes, wielding a sword and charging at you*\n')




time.sleep(1.5)#First Interaction with other characters.
print('"YOU BEAST ILL GET YOU"\n')



time.sleep(2)
print('"Wait . . ."\n')




time.sleep(2)
print('"Youre no monster. . . ."\n')




time.sleep(2)
print('\n"So uhhh . . . anyways, Im Dime, and you are?"\n')



time.sleep(2)
print('I am ', name )
time.sleep(4)







print('\n' * 20)


#new character
print(f"Fellow created with name: {dime.user} and health: {dime.health} and race: {dime.race.name}")
print('\n'*13)
time.sleep(5)



print('\n' * 25)






print('               The Story Continues . . . ')#Story Continuation
print('\n' * 6)







time.sleep(4)
print('"Thats a lovely name. ', name, ' I love it!"\n')



time.sleep(1)
print('"Anyways . . . ', 'I need your help. And i need it now."')
time.sleep(2)



input('\n"Are you up for the Challenge?"\n')
time.sleep(2)#No Matter whats said, its a yes so storyc an continue


print('"Sounds like a Yes to me!, Sweet!!"\n')
time.sleep(2)



#Main point of story. To save Helga.
print('"Im getting side tracked here, there are more important measures at stake"')
time.sleep(2)


print('"Its . . . "')
time.sleep(2)


print('"Its . . My friend Helga, shes been uhh . . . "')
time.sleep(2)


print('"Kidnapped."\n')
time.sleep(2)





input('"Are you still able to help me?"\n ')
time.sleep(2) #same as before, makes dime seem like he doesnt care and does need this health


print('"Still sounds like a Yes to me!')
time.sleep(4)



#Semi-clear screen so it can make this like seem more important
print('\n'*6)
print('               Where Should we go first ', name,'?')
print('\n\n\n')



time.sleep(3)















#______________________________________FIRST SELECTION_____________________________________









#path choosing, defined so it can be called back on to come back to.
def choose_path(player, dime, tree):
    player_health = player.health

    while True:


        print('\n' * 30)
        print('______________________________________________ WHERE TO ______________________________________________')
        print('\n'*10)

#__________________________________FIRST PLACE DECISION__________________________________
#|       / = Location Option                                                            |
#|       // = Fight Selection                                                           |
#|       /// = Fight Answer                                                             |
#|                                                                                      |
#|                                                                                      |
#|                        #3 options to go to.                                          |      
        choice = input('\nWhere will you go?\n'#                                        |
                       'a) Through the Forest?\n'#                                      |
                       'b) To the Field of Foe?\n'#                                     |
                       'c) The Tavern of Many?\n\n').lower()#                           |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|___________________________________FIRST PLACE________________________________________|
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|/______________________________________OPTION A______________________________________\|
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
        if choice == 'a':#                                                              |
#|                                                                                      |
            print('You venture into the forest, you hear whispers...')#                 |
#|                                                                                      |
            time.sleep(2)#                                                              |
#|                                                                                      |
            input('“So, what makes you want to go through the forest?”\n')#             |
#|                                                                                      |
            time.sleep(2)#                                                              |
#|                                                                                      |
            print('“Uh huh . . . Okay . . . Whatever you say, Brochacho.”')#            |
#|                                                                                      |
            time.sleep(1)#                                                              |
#|                                                                                      |
            print('*bsh bhs bsh*')#                                                     |
#|                                                                                      |
            time.sleep(1)#                                                              |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|//________________________________FIRST FIGHT CHOICE________________________________\\|
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
            while True:  #                                                              |                                                                       
                fight = input('\nYou see a Walking Tree. You can either:\n'#            |
                              '  a) Fight it\n'#                                        |
                              '  b) Go back\n'#                                         |
                              '  c) Befriend it\n'
                              '  d) Check your Inventory\n\n').lower()#                          |
                time.sleep(1)#                                                          |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|///___________________________________FIGHT 1 A____________________________________\\\|
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
                if fight == 'a':
                    print('You get your weapon ready and engage in battle... against a tree?\n\n')
                    time.sleep(1)
                    print('   You attack the Tree and it smacks you back')
    
    
                    #Health exchange
                    player.take_damage(tree.damage)
                    tree.health -= player.weapon_damage

                    #Set tree health to 0 if it goes negative
                    if tree.health < 0:
                        tree.health = 0

                    #Show health updates
                    print(f"{player.user}'s health: {player.health}")
                    print(f"{tree.user}'s health: {tree.health}")
                    time.sleep(1)

                    #If the Tree is dead
                    if tree.health == 0:
                        print("\n\n *THUD*. The tree drops.")
                        print("It dropped some items.")
        
       
                    for item in tree.drop_items:
                        player.add_to_inventory(item)

                    
                    while True:
                        print("\nYou keep walking through the forest.")
                        print("What do you want to do?")
                        print("  a) Go back")
                        print("  b) Check inventory")
                        choice = input("").lower()

                        if choice in ['a', 'go back']:
                            print("You head back the way you came...")
                            return
                        elif choice in ['b', 'check inventory']:
                            player.print_inventory()

                        else:
                            print("Invalid option. Try again.")
#|                                                                                      |                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|///_______________________________FIGHT 1 B________________________________________\\\|
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
                elif fight == 'b':#                                                     |
                    print('You decide to retreat... Bok Bok!')#                         |
#|                                                                                      |
#|                   Goes back to Choose_path (Good thing we defined that!)             |
                    return choose_path(player, dime, tree) #                            |
#|                                                                                      |
#|                                                                                      |                
#|                                                                                      |
#|///_______________________________FIGHT 1 C________________________________________\\\|
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
                elif fight == 'c':#                                                     |
#|                                                                                      |
                    print('You try to befriend the tree... and it attacks you!')#       |
#|                    I thought it would be funny to add this.                          |
#|                                                                                      |
                    player.take_damage(20)#                                             |
#|                    Higher then Enemy(TREE) normal damage because it was 'Unexpected' |
#|                                                                                      |
                    print(f'Your Health is now: {player.health}')#                      |
                    time.sleep(1)#                                                      |
                    print('The tree still stands there, rustling ominously...')#        |
                    time.sleep(2)#                                                      |
#|                                                                                      |
#|                                                                                      |
#|///_____________________________FIGHT 1 D__________________________________________\\\|
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
                elif fight == 'd':#                                                     |
                    player.print_inventory()#                                           |
                    time.sleep(2)#                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|///____________________________FIGHT 1 ELSE________________________________________\\\|
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|             If something other then a, b or c!                                       |
                else:#                                                                  |
                    print("That’s not a valid option. Try again.")#                     |
            break#                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|/____________________________________OPTION B________________________________________\|        
#|                                                                                      |
#|                                                                                      |
#|                                                                                      | 
        elif choice == 'b':#                                                            |
#|                     Choice B                                                         |
#|                                                                                      |
            print('\n' *8)#                                                             |
            time.sleep(2)#                                                              |
#|                                                                                      |            
            print('     *Squish, Squash*')#                                             |
            time.sleep(1)#                                                              |
#|                                                                                      |
            print('"The Grass sure is wet here"')#                                      |
            time.sleep(1)#                                                              |
#|                                                                                      |
            print('Yeah, I guess')#                                                     |
            time.sleep(.5)#                                                             |
#|                                                                                      |
            print('"LOOK OVER THERE"')#                                                 |
            time.sleep(2)#                                                              |
#|                                                                                      |
            print('\n\n\n     You and Dime look into the Distance and see your first challenge in the field of Foe')
            time.sleep(1)#                                                              |
#|                                                                                      |
            print('     2 doors, The Left Door, and The Right Door.')#                  |
            time.sleep(2)#                                                              |
#|                                                                                      |
            print('     The only other thing you can see is a sign.')#                  |
            time.sleep(2)#                                                              |
#|                                                                                      |
            print('     You must be closer to read the sign)')#                         |
            time.sleep(4)#                                                              |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
            print('\n' * 30)#screen clear#                                              |
#|                                                                                      |            
#|                                                                                      |
#|______________________________________DOORS___________________________________________|
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |             
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

""")


#|                                                                                      |
#|                                                                                      |
#|___________________________________END DOOR___________________________________________|
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
            time.sleep(5)
            print('\n' *5)
#|                                                                                      |
            print('Upon getting closer, you can read the sign.')
            time.sleep(3)
#|                                                                                      |
            print('        "Answer my riddle three, and leave your fate up to me\n        Behind the one of the doors is a Foe, and behind the other you wont know."')
            time.sleep(2)
#|                                                                                      |
            print('"The sign says only one contains an enemy, that means the other one wont.')
            time.sleep(1)
#|                                                                                      |
            print('     "Your First Ridd-"')
            time.sleep(1)
#|                                                                                      |
            print('"Shut up, now as i was saying. it says only one contains an enemy\n I say that gives us good odds to enter one"')
            time.sleep(2)
#|                                                                                      |
            print('I guess youre right Dime.')
            time.sleep(2)
#|                                                                                      |
            door = input('                             What Door do you open?\na) The Left door\nb) The Right door\n').lower()
            
            
            
            if door == 'a':
                time.sleep(2)
                print('     "Hmm the Left door, Without my riddles? . . .  Ouch."')
                time.sleep(3)
                print('     "The left door contains a battle!" ')
                fight1 = input('\nYou see a . . . short guy named Barry wielding a stick? You can either:\n'
                              '  a) Fight him\n'
                              '  b) Go back\n')
                
                if fight1 == 'a':
                    print('     You get youre {player.weapon} ready to against Barry and the "Stick of Anquish" \n\n')
                    time.sleep(2)
                    print('   You attack the Barry and he begins to cry and starts throwing his stick around like a little kid and it nicks you')
                    time.sleep(1)
                    print('   You do {player.weapon_damage} to Barry, and he does {barry.damage} back.')

                    player.take_damage(barry.damage)
                    barry.health -= player.weapon_damage
                    if barry.health < 0:
                        barry.health = 0

                    time.sleep(2)
    
                    print(f"you have {player.health} health left")
                    print(f"{barry.user} has {barry.health} left")
                    time.sleep(3)



            elif door == 'b':
                time.sleep(2)
                print('     "The Right door, Lets hope you made the RIGHT choice!"')
                time.sleep(3)
                print('     "The Right door is SAFE!, you may continue your venture!"')




            else:
                time.sleep(2)
                print(' . . . ')
                time.sleep(1)
                print(' . . . ')
                time.sleep(1)
                print('     "Uhhh dude, theres 2 doors. pick one"')
                time.sleep(2)
            break
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|///______________________________________CHOICE C__________________________________\\\|


        elif choice == 'c':

            print('          *swish swoosh*\n')
            time.sleep(1)
            print('          You step into the tavern, the smell of ale and stories thick in the air...\n')
            time.sleep(2)
            print('          You hear \n')
            print('          "NO WEAPONS"\n')
            print(           'Yelled across the bar from the Bartender\n')
            time.sleep(1.5)
            print('          You Put your weapons at the door and continue walking in with Dime. \n')
            time.sleep(1.5)
            print('          You sit down at the bar and order a drink\n')
            time.sleep(2)
            print('          "Eyy What are you here for?"\n')
            time.sleep(1)
            print('          "something you need? You arent our usual folk"\n')
            print('          - Someone sitting next to you on stool\n')
            time.sleep(1.3)
            print('I uhh . . .  We are . . .\n ')
            time.sleep(1)
            print('"Someone we know was kidnapped. we need infomation.\n')
            time.sleep(1.5)
            print('Yeah, what he said\n')
            time.sleep(1.3)
            print('          *The stranger chewing on a tooth pick*\n')
            time.sleep(1)
            print('          "I Think i can be of service"\n')
            time.sleep(1)
            print('          *Tips his cowboy like hat down to you"')
            time.sleep(1.5)
            print('\n         "First im going to need some names."')
            time.sleep(2)
            print('\n"Im Dime and he is ', player.user,', we are looking some by the name Helga"')
            time.sleep(1)
            print('     *Still chewing tooth pick but moves it to other side*\n')
            time.sleep(1)
            print('     "That rings a bell, Helga. I might be able to help"')
            time.sleep(1)
            print('Thanks, We never got you name.')
            time.sleep(1)
            print('     "Bane, Cad Bane"\n\n      "Go sit in that booth there and wait for me"')#totally not a taken name
            time.sleep(1)
            print('     *You and Dime walk to the booth at which Bane pointed at and wait*\n\n')
            time.sleep(1)
            print('     "Who is this Helga to you"')

            while True:
                stranger = input('''
                a) I dont know her, Dimes friend
                b) Our Friend
                c) My Mother
                d) Thats not of your concern
                ''').lower()
                time.sleep(1)

                if stranger == 'a':
                    pet  = input('''        '     "What are you some pet?"
                    a) Yes
                    b) No
                       ''')
                    time.sleep(1)

                    if pet == 'b':
                        print('     "Whatever you say.')
                        time.sleep(1)
                        print('     "Helga was taken by a Humaniod Turtle called Trowser')
                        time.sleep(1)
                        trowser = input('''
                        a) trowser?
                        b) Ive heard of him. Where is he?
                            ''')
                        time.sleep(1)
                        if trowser == 'a':
                            print('     "The Humanoid Turle? i just said that, anyways, go through the fielf of foe"')
                            return choose_path

                        elif trowser == 'b':
                            print('        "I doubt you of all people have hear of him. He can be found in the Field of Foe"')



                    elif pet == 'a':
                        print('     "Uhhhhh . . . ."')
                        time.sleep(1)
                        print('Will you still help us?')
                        time.sleep(.5)
                        print('     "I Guess"')
                        time.sleep(1)
                        print('     "Helga was taken by a Humaniod Turtle called Trowser')
                        time.sleep(1)
                        trowser = input('''
                        a) trowser?
                        b) Ive heard of him. Where is he?
                                ''')
                        time.sleep(1)
                        if trowser == 'a':
                            print('     "The Humanoid Turle? i just said that, anyways, go through the fielf of foe"')
                            return 

                        elif trowser == 'b':
                            print('        "I doubt you of all people have hear of him. He can be found in the Field of Foe"')

                        else:
                            print('     "Wierd way to answer a yes or no question')
                            time.sleep(1)
                            print('     "Helga was taken by a Humaniod Turtle called Trowser')
                            time.sleep(1)
                            trowser = input('''
                        a) trowser?
                        b) Ive heard of him. Where is he?
                            ''')
                            time.sleep(1)
                            if trowser == 'a':
                                print('     "The Humanoid Turle? i just said that, anyways, go through the fielf of foe"')
                                return choose_path


                elif stranger == 'b':
                    print('     "Really? Shes friends with you? I dont buy it" ')
                    time.sleep(1)
                    print('     "Helga was taken by a Humaniod Turtle called Trowser')
                    time.sleep(1)
                    trowser = input('''
                    a) trowser?
                    b) Ive heard of him. Where is he?
                        ''')
                    time.sleep(1)
                    if trowser == 'a':
                        print('     "The Humanoid Turle? i just said that, anyways, go through the fielf of foe"')
                        return choose_path

                    elif trowser == 'b':
                        print('        "I doubt you of all people have hear of him. He can be found in the Field of Foe"')


                elif stranger == 'c':
                    print('     "Oh Really? Shes YOUR mother? She had no kids idiot"')
                    time.sleep(1)
                    print('     "Helga was taken by a Humaniod Turtle called Trowser')
                    time.sleep(1)
                    trowser = input('''
                    a) trowser?
                    b) Ive heard of him. Where is he?
                        ''')
                    time.sleep(1)
                    if trowser == 'a':
                        print('     "The Humanoid Turle? i just said that, anyways, go through the fielf of foe"')
                        return choose_path

                    elif trowser == 'b':
                        print('        "I doubt you of all people have hear of him. He can be found in the Field of Foe"')


                elif stranger == 'd':
                    print('     "Oh Mr Grumpy pants over here."')
                    time.sleep(1)
                    print('     "Helga was taken by a Humaniod Turtle called Trowser')
                    time.sleep(1)
                    trowser = input('''
                    a) trowser?
                    b) Ive heard of him. Where is he?
                        ''')
                    time.sleep(1)
                    if trowser == 'a':
                        print('     "The Humanoid Turle? i just said that, anyways, go through the fielf of foe"')
                        return choose_path

                    elif trowser == 'b':
                        print('        "I doubt you of all people have hear of him. He can be found in the Field of Foe"')


                else:
                    print('Not an Option')
                    time.sleep(2)

            

            
        else:
            print("That’s not a valid choice. Try again.")

    return player_health

player_health = choose_path(player, dime, tree)
print(f"\nYou finished choosing a path. Your health is {player_health}. Game continues here...")
