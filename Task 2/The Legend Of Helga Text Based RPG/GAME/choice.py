from settings import *
from forest import forest
from doors import field_of_foe
from bar import enter_bar
import time


tree = Enemy(
    "Tree",
    health=200,
    damage=10,
    drop_items=[bark_shield,
    sap_of_life]
    )

barry = Enemy(
    "Barry",
    health=15,
    damage=2,
    drop_items=[barrys_tears]
    )

harry = Enemy(
    "Harry",
    health=30,
    damage=4,
    drop_items=[sandals, bucket_hat]
    )

larry = Enemy(
    "Larry",
    health=45,
    damage=6,
    drop_items=[brown_stained_pants]
    )

garry = Enemy(
    "Garry",
    health=60,
    damage=10,
    drop_items=[chopping_board_chest_plate]
    )

trowser = Enemy(
    "Trowser",
    health=200,
    damage=20,
    )
def choose_path(player, dime, tree, barry=None, harry=None, larry=None, garry=None, trowser=None, progress_stage=0):
    while True:
        clear_console()
        print('______________________________________________ WHERE TO ______________________________________________\n\n\n'.center(columns))
        print('Where will you go?\n'.center(columns))
        print('a) Through the Forest?'.center(columns))
        print('b) To the Field of Foe?'.center(columns))
        print('c) The Tavern of Many?'.center(columns))

        choice = centered_input().lower()
        time.sleep(2)
        clear_console()

        if choice == 'a':
            forest(player, tree)

        elif choice == 'b':
            field_of_foe(player, dime, barry, harry, larry, garry, trowser)

        elif choice == 'c': 
            enter_bar(player, dime, tree)

        else:
            print('Not an Option'.center(columns))
            time.sleep(2)
