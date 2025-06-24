from settings import *
from forest import forest
from doors import field_of_foe
from bar import enter_bar


def choose_path(player, dime, tree):
    
    while True:
        clear_console()
        print('______________________________________________ WHERE TO ______________________________________________\n\n\n'.center(columns))
        print('Where will you go?\n'.center(columns))

        print('a) Through the Forest?'.center(columns))
        print('b) To the Field of Foe?'.center(columns))
        print('c) The Tavern of Many?'.center(columns))


        choice = centered_input().lower()
        time.sleep(3)
        clear_console()

        if choice == 'a':
            forest(player, tree)
           
        elif choice == 'b':
           field_of_foe(player, dime, barry)

        elif choice == 'c': 
            enter_bar(player, dime, tree, harry)

        else:
            print('Not an Option'.center(columns))
            time.sleep(3)