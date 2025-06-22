from settings import *

def tree_picture():
    clear_console()
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
    tree_lines = tree_ascii.strip('\n').split('\n')
    vertical_padding = (rows - len(tree_lines)) // 2
    print('\n' * vertical_padding)
    for line in tree_lines:
        print(line.center(columns))
    time.sleep(5)
    clear_console()

def tree_battle(player, tree):
    while True:
        print('You see a Walking Tree. You can either:'.center(columns))
        print('a) Fight it'.center(columns))
        print('b) Go back'.center(columns))
        print('c) Befriend it'.center(columns))
        print('d) Check your Inventory'.center(columns))
        time.sleep(3)

        fight = centered_input()

        if fight == 'a':
            print('You get your weapon ready and engage in battle... against a tree?\n\n'.center(columns))
            time.sleep(3)
            print('   You attack the Tree and it smacks you back'.center(columns))
            player.take_damage(tree.damage)
            tree.health -= player.weapon_damage
            if tree.health < 0:
                tree.health = 0

            print(f"{player.user}'s health: {player.health}".center(columns))
            print(f"{tree.user}'s health: {tree.health}".center(columns))
            time.sleep(3)

            if tree.health == 0:
                print('*THUD*. The tree drops.'.center(columns))
                print("     It dropped some items.".center(columns))
                for item in tree.drop_items:
                    player.add_to_inventory(item)

                while True:
                    print('You keep walking through the forest.'.center(columns))
                    print('What do you want to do?'.center(columns))
                    print('a) Go back'.center(columns))
                    print('b) Check inventory'.center(columns))

                    choice = centered_input()

                    if choice in ['a', 'go back']:
                        print("You head back the way you came...\n".center(columns))
                        return  # Go back to main path loop
                    elif choice in ['b', 'check inventory']:
                        player.print_inventory()
                    else:
                        print("Invalid option. Try again.\n".center(columns))

        elif fight == 'b':
            print('You decide to retreat... Bok Bok!'.center(columns))
            return  # Go back to main path loop

        elif fight == 'c':
            print('You try to befriend the tree... and it attacks you!\n'.center(columns))
            time.sleep(3)
            player.take_damage(20)
            print(f'Your Health is now: {player.health}'.center(columns))
            time.sleep(3)
            print('The tree still stands there, rustling ominously...'.center(columns))
            time.sleep(3)

        elif fight == 'd':
            player.print_inventory()
            time.sleep(3)
        else:
            print("That’s not a valid option. Try again.".center(columns))

def forest(player, tree):
    if tree.health == 0:
        print('"You have already killed the beast that is here"\n'.center(columns))
        time.sleep(3)
        print('"Go Back. We have to save Helga"\n'.center(columns))
        time.sleep(3)
        print('     Feeling like an idiot, you turn around and go back'.center(columns))
        time.sleep(3)
        return

    print('You venture into the forest, you hear whispers...\n'.center(columns))
    time.sleep(3)

    print('“So, what makes you want to go through the forest?”\n'.center(columns))
    centered_input()
    time.sleep(3)

    print('“Uh huh . . . Okay . . . Whatever you say, Brochacho.”\n'.center(columns))
    time.sleep(3)

    print('*bsh bhs bsh*'.center(columns))
    time.sleep(3)

    tree_picture()
    tree_battle(player, tree)
