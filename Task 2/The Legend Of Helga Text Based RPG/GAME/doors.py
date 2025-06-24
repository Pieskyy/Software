from settings import *
import time

def trowser_picture():
    clear_console()
    print(r'''
                ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                                       
            ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                                        
     ░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░   ░  ░ ░░░░ ░░░  ░░░░ ░░░░ ░░░   ░  ░ ░░░  ░░     
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                                   
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░                                                  
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ ░ ░▒▒░░░░  ░░░░░░░░░░░░░░  ░░░░░░░░░░░░░    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒░▒▓██████▓▓██▓█░                            ░         
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▒░░░░░░░▒████▓▓▓▓▓▓▓▓▓▓▓▓██▒▓░ ░░                                 
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▒▒▓░░░░░░▒█▓▓█▓▒▓▓▓▓▒▓▓▓▓▓▓████ ░▓▓█░              ░                
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▒░░█▒░░░░░▒▓▒▒▒▒▒▒▒▓▒▒▒▒▒▒▒▒▒▒▓▒░░▓░▒▓░░░░░░░░░░░░ ░░░░░░░░░░░░░░    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▒░░▒█░░░░░▒▓▒▓▓▓▓▓▓▒▓▓▓▓▒▓▓▒▓▓████▒░░▓▒                              
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▓░░░▒██▒▒▒▒▓█▓▓▓█████▓▓▓▓▓▓▓▓▓▓█▒░░░▒█▒                            ░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▒░░░░▒██████▓▓▓▓▓▓▓▓▓▓▓▓█████▓░░░░░▒▓░       ░     ░░        ░    ░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓░░░▒█▓▒▒▒▒█▒▒▒▒▒▓▓▓▒▒▒▒▓▒▒▒▒▓█▒░░▒▓▒░░░░ ░░ ░░░   ░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▓▓▓█▓▓▓▓▓▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▓▓▓█▓▓▓█░░░░░               ░░░ ░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▓██▓▒▓▓▓▓▓██▓▓▓▓██▓▓▓▓▓▓▓██▓█▒░░░░░░░░░░         ░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▓█▓▓█▒▒▓▒▒▒▓▒▒▓▓▓▒▒▓▓▒░▓▓▓▓▒█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██▓▓█  ▒▓███▓▓▓▓███▓░  ▓▓▓▓█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓██▓▓▓▓▓▓▓▒░████████▒▒▓▓▓▓▓▓███▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█▒░░░░░▒▓█████▒░░░░░░▒█████▓▒░░░░░▒█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▓▒░░░░░░░░░░░░░▓▒░░░░▒▓▒░░░░░░░░░░░░░▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▓░░░░░░░░░░░░░░▒░░░░░░░░░░░░░░░▒░░░░░▒█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█▓░░░░░▓▒░░░░░░░░░░░░░░░░░░░░░░░▒█░░░░▒█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░ ░░░░░░░░░░▓▓░░░░███▓░░░░░░░░░░░░░░░░░░░░▒███▒░░░▒█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░ ░░░░░░░░░░░▓▒░░░██▓▓░▓▒░░░░░▒██▒░░░░░▒▒▒▓▓▓█▒░░▒▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░ ░░ ░░ ░░░ ░░ ░░░░░░░░░░░░░░▒█▓░░░▒▓▓█▓▓░▒██▓▓▓▓▓▓██▓▒█▓█▓▓▒░░░▒█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░ ░░         ░  ░░░░░░░░░░░░░░░▒██▒░▒█▓▓▓█░▓▓▓▓▓▓▓▓▓▓▒▒▓▓█▓░░░▓█▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒█░░░▓▒▒▓▓▒▒▒▒▒▓▓▒▓▓▓▒▓█▒░░░█▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░ ░░ ░░░░░░░░░░░░░░░░░░▓█░░░▒▓▒▓░░▓▒▓▓▓▓░░▒▓█░░░▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░ ░  ░            ░░░░░░░░░░░░░░░░▒█░░░▓█▒░▒██████▓░▒█░░░▒█▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░      ░░  ░░ ░░░░░░░░░░░░░░░░░░▒█▒░▒▓▒░░░░░░░░░░▒▓▒░██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
     ░░░░░░░░░░░░░░  ░░░░░░░░░░░░░░░░░▒█░░░░░░░░░░░░░░░░░░░▒█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                ░       ░░░░░░░░░░░░░░▓▒░░░░░░░░░░░░░░░░░░░░█▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                   ░░░▒█▓▒░░░▒▒▓█▓▓█▓▒▒░░░▒▓█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
                                       ░░▒▓▓▒▒░░░░░░░░▒▒▓▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
    ░░░░░░░░░░░░░░   ░░░░░░░░░░░░░   ░░░░░░░░░ ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  
                                                   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░           
                                                       ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░               
     ░      ░░░░      ░░░ ░░   ░░░   ░░░ ░░   ░░░   ░  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  ░░ ░░ ░░      
     ░░░░  ░    ░░         ░░   ░         ░░   ░    ░  ░  ░░░░░░░░░░░░░░░░░░  ░░   ░     ░   ░      
''')
    time.sleep(5)
    clear_console()
def door_picture(): # Door Ascii
    clear_console()
    print(r"""
   _________________________                                                           _________________________
  /                         \                                                         /                          |
 /     Left                  |                                                       /            Right           |                                                       
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
_________________________________________________________________________________________________________________
          """)
    time.sleep(5)
    clear_console()


def barry_battle(player, barry): # Controls the first battle, the one with barry!
    if barry.health == 0:
        return True

    while True:
        print("You can either:".center(columns))
        print("a) Fight Barry".center(columns))
        print("b) Go back".center(columns))
        print("c) Check Inventory".center(columns))
        choice = centered_input()
        time.sleep(1)

        if choice == 'a':
            print("You attack Barry with your axe!".center(columns))
            time.sleep(2)
            print("barry throws his stick at you\n".center(columns))
            time.sleep(2)
            player.take_damage(barry.damage)
            barry.health -= player.weapon_damage
            if barry.health < 0:
                barry.health = 0

            print(f"{player.user}'s health: {player.health}".center(columns))
            print(f"Barry's health: {barry.health}".center(columns))
            time.sleep(2)
            clear_console()

            if barry.health == 0:
                print("YOU KILLED BARRY YOU MONSTER".center(columns))
                for item in barry.drop_items:
                    player.add_to_inventory(item)
                return True

        elif choice == 'b':
            return False

        elif choice == 'c':
            player.print_inventory()

        else:
            print("Invalid option.".center(columns))
            clear_console()


def harry_battle(player, harry): # Second Battle
    if harry.health == 0:
        return True

    while True:
        print('You are now about to fight "harry"\n'.center(columns))
        time.sleep(2)
        print("You can either:".center(columns))
        print("a) Fight Harry".center(columns))
        print("b) Go back".center(columns))
        print("c) Check Inventory".center(columns))
        choice = centered_input()
        time.sleep(1)

        if choice == 'a':
            print('"harry harry harry" - you hear this guy chanting. trying to boost himself up'.center(columns))
            time.sleep(2)
            player.take_damage(harry.damage)
            harry.health -= player.weapon_damage
            if harry.health < 0:
                harry.health = 0

            print(f"{player.user}'s health: {player.health}".center(columns))
            print(f"Harry's health: {harry.health}".center(columns))
            time.sleep(2)
            clear_console()

            if harry.health == 0:
                print("Harry is defeated!".center(columns))
                for item in harry.drop_items:
                    player.add_to_inventory(item)
                return True

        elif choice == 'b':
            return False

        elif choice == 'c':
            player.print_inventory()

        else:
            print("Invalid option.".center(columns))
            clear_console()


def larry_battle(player, larry): # 3rd
    if larry.health == 0:
        return True

    while True:
        print('"You See Larry. JEEZ 3 of em"\n'.center(columns))
        time.sleep(2)
        print("You can either:".center(columns))
        print("a) Fight Larry".center(columns))
        print("b) Go back".center(columns))
        print("c) Check Inventory".center(columns))
        choice3 = centered_input()
        time.sleep(1)

        if choice3 == 'a':
            print("You battle Larry, who swings wildly!".center(columns))
            time.sleep(2)
            player.take_damage(larry.damage)
            larry.health -= player.weapon_damage
            if larry.health < 0:
                larry.health = 0

            print(f"{player.user}'s health: {player.health}".center(columns))
            print(f"Larry's health: {larry.health}".center(columns))
            time.sleep(2)
            clear_console()

            if larry.health == 0:
                print("Larry collapses, defeated.".center(columns))
                for item in larry.drop_items:
                    player.add_to_inventory(item)
                return True

        elif choice3 == 'b':
            return False

        elif choice3 == 'c':
            player.print_inventory()

        else:
            print("Invalid option.".center(columns))
            clear_console()


def garry_battle(player, garry): # 4th
    if garry.health == 0:
        return True

    while True:
        print('"Oh my god! Where is Trowser . . ."\n'.center(columns))
        time.sleep(2)
        print("You can either:".center(columns))
        print("a) Fight Garry".center(columns))
        print("b) Go back".center(columns))
        print("c) Check Inventory".center(columns))
        choice4 = centered_input()
        time.sleep(1)

        if choice4 == 'a':
            print("You lunge at Garry for a showdown!".center(columns))
            time.sleep(2)
            player.take_damage(garry.damage)
            garry.health -= player.weapon_damage
            if garry.health < 0:
                garry.health = 0

            print(f"{player.user}'s health: {player.health}".center(columns))
            print(f"Garry's health: {garry.health}".center(columns))
            time.sleep(2)
            clear_console()

            if garry.health == 0:
                print("Garry is vanquished. one enemy to go,.".center(columns))
                for item in garry.drop_items:
                    player.add_to_inventory(item)
                return True

        elif choice4 == 'b':
            return False

        elif choice4 == 'c':
            player.print_inventory()

        else:
            print("Invalid option.".center(columns))
            clear_console()

def trowser_battle(player, trowser): # Controls the last battle
    if trowser.health == 0:
        return True
    
    trowser_picture()

    while True:
        print('"You Have made it. You Are now able to save Helga"\n'.center(columns))
        time.sleep(3)
        print("You can either:".center(columns))
        print("a) Fight trowser".center(columns))
        print("b) Go back".center(columns))
        print("c) Check Inventory".center(columns))
        choice5 = centered_input()
        time.sleep(1)

        if choice5 == 'a':
            print("You attack trowser with your axe!".center(columns))
            time.sleep(2)
            print("Trowsers jumps at you\n".center(columns))
            time.sleep(2)
            player.take_damage(trowser.damage)
            trowser.health -= player.weapon_damage
            if trowser.health < 0:
                trowser.health = 0

            print(f"{player.user}'s health: {player.health}".center(columns))
            print(f"trowser's health: {trowser.health}".center(columns))
            time.sleep(2)
            clear_console()

            if trowser.health == 0:
                print("YOU KILLED TROWSER!!!".center(columns))
                time.sleep(3)
                print('"H- Hello is that you Dime ??" - Helga'.center(columns))
                print('"HELGAAAAAAAAAA"'.center(columns))
                time.sleep(2)
                clear_console()
                print('This was -'.center(columns))
                time.sleep(3)
                clear_console()
                print(r'''
████████╗██╗  ██╗███████╗      
╚══██╔══╝██║  ██║██╔════╝      
   ██║   ███████║█████╗          
   ██║   ██╔══██║██╔══╝           
   ██║   ██║  ██║███████╗        
   ╚═╝   ╚═╝  ╚═╝╚══════╝         

 ██╗     ███████╗ ██████╗ ███████╗███╗   ██╗██████╗      
 ██║     ██╔════╝██╔════╝ ██╔════╝████╗  ██║██╔══██╗  
 ██║     █████╗  ██║  ███╗█████╗  ██╔██╗ ██║██║  ██║
 ██║     ██╔══╝  ██║   ██║██╔══╝  ██║╚██╗██║██║  ██║
 ███████╗███████╗╚██████╔╝███████╗██║ ╚████║██████╔╝
 ╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ 
                      
  ██████╗ ███████╗
 ██╔═══██╗██╔════╝  
 ██║   ██║█████╗   
 ██║   ██║██╔══╝   
 ╚██████╔╝██╗      
  ╚═════╝ ╚═╝   
                      
██╗  ██╗███████╗██╗      █████╗   █████╗ 
██║  ██║██╔════╝██║     ██╔═══╝   ██╔══██╗
███████║█████╗  ██║     ██║  ███╗ ███████║
██╔══██║██╔══╝  ██║     ██║   ██║ ██╔══██║
██║  ██║███████╗███████╗╚██████╔╝ ██║  ██║
╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝  ╚═╝  ╚═╝
''')
                time.sleep(5)
                clear_console()
                print('Congrats on Beating "The Legand of Helga". I hope you enjoyed it <3'.center(columns))
                time.sleep(5)
                exit()

        elif choice5 == 'b':
            return False

        elif choice5 == 'c':
            player.print_inventory()

        else:
            print("Invalid option.".center(columns))
            clear_console()


def field_of_foe(player, dime, barry, harry, larry, garry, trowser): # where all is collated and to be called in choice.py
    from choice import choose_path

    if not hasattr(player, 'entered_field_of_foe'): # to check what battle you are up to
        player.entered_field_of_foe = False
    
    if not player.entered_field_of_foe:
        print("You and Dime enter the Field of Foe...".center(columns))
        time.sleep(3)
        door_picture()
        print("You read the mysterious sign...".center(columns))
        time.sleep(3)

        while True:
            print("What door do you open?".center(columns))
            print("a) The left door".center(columns))
            print("b) The right door".center(columns))
            door = centered_input()

            if door == 'a':
                print('The left door contains a battle!'.center(columns))
                time.sleep(2)
                clear_console()
                break


            elif door == 'b':
                print("You open the right door and see no enemy.".center(columns))
                time.sleep(2)
                print("You then glance left and realize...".center(columns))
                time.sleep(2)
                print("These doors aren't actually separated.".center(columns))
                time.sleep(2)
                print("A small man named Barry is waiting for you regardless.".center(columns))
                time.sleep(3)
                clear_console()
                break

            else:
                print("Invalid choice. Pick left or right.".center(columns))
                clear_console()
        
        # Mark that intro was completed
        player.entered_field_of_foe = True

    # Now proceed to battles based on progress
    while player.field_of_foe_stage < 5:
        if player.field_of_foe_stage == 0:
            success = barry_battle(player, barry)
            if success:
                player.field_of_foe_stage += 1
                print("A path opens forward...".center(columns))
                time.sleep(2)
            else:
                choose_path(player, dime, tree, barry, harry, larry, garry, trowser)
                return

        elif player.field_of_foe_stage == 1:
            success = harry_battle(player, harry)
            if success:
                player.field_of_foe_stage += 1
                print("Another foe awaits...".center(columns))
                time.sleep(2)
            else:
                choose_path(player, dime, tree, barry, harry, larry, garry, trowser)
                return

        elif player.field_of_foe_stage == 2:
            success = larry_battle(player, larry)
            if success:
                player.field_of_foe_stage += 1
                print("Almost there... few remains.".center(columns))
                time.sleep(2)
            else:
                choose_path(player, dime, tree, barry, harry, larry, garry, trowser)
                return
            
        elif player.field_of_foe_stage == 3:
            success = larry_battle(player, garry)
            if success:
                player.field_of_foe_stage += 1
                print("You’ve defeated them all! Atleast, all but one!.".center(columns))
                time.sleep(2)
            else:
                choose_path(player, dime, tree, barry, harry, larry, garry, trowser)
                return

        elif player.field_of_foe_stage == 4:
            success = trowser_battle(player, trowser)
            if success:
                player.field_of_foe_stage += 1
                print("You have defeated Trowser! Congratualations, You have completed the game.".center(columns))
                time.sleep(2)
                return
            else:
                choose_path(player, dime, tree, barry, harry, larry, garry, trowser)
                return
