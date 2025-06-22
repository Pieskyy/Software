from settings import *

def door_picture():
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
___________________________________________________________________________________________________________________
""")
    time.sleep(5)
    clear_console()

def barry_battle(player, barry):
    if barry.health == 0:
        print('YOU KILLED HIM')
        return

    while True:
        print('You can either:'.center(columns))
        print('a) Fight him'.center(columns))
        print('b) Go back'.center(columns))
        fight1 = centered_input()
        time.sleep(2)

        if fight1 == 'a':
            print('\n\n')
            print('You get your weapon ready to fight Barry and his "Stick of Anguish" \n\n'.center(columns))
            time.sleep(3)

            print('   You attack Barry and he begins to cry and flails his stick like a toddler... it still nicks you.'.center(columns))
            time.sleep(3)
            actual_damage = player.take_damage(barry.damage)
            barry.health -= player.weapon_damage
            print(f"You do {player.weapon_damage} to Barry, and he does {actual_damage} back (reduced from {barry.damage}).".center(columns))


            player.take_damage(barry.damage)
            barry.health -= player.weapon_damage
            if barry.health < 0:
                barry.health = 0

            time.sleep(2)
            print(f"{player.user}'s health: {player.health}".center(columns))
            print(f"{barry.user}'s health: {barry.health}".center(columns))
            time.sleep(3)

            if barry.health == 0:
                print('Barry is down for good. Poor fella.'.center(columns))
                break

        elif fight1 == 'b':
            print("You decide not to fight the tiny stick-wielding gremlin today.".center(columns))
            break

        else:
            print("That’s not a valid option.".center(columns))

def left_door(player, barry):
    print('     "Hmm the Left door, Without my riddles? . . .  Ouch."\n'.center(columns))
    time.sleep(3)
    print('     "The left door contains a battle!" '.center(columns))
    time.sleep(2)
    print('You see a . . . short guy named Barry wielding a stick?'.center(columns))
    time.sleep(3)

    barry_battle(player, barry)

def right_door():
    print('     "The Right door, Let\'s hope you made the RIGHT choice!"'.center(columns))
    time.sleep(3)
    print('     "The Right door is SAFE! You may continue your venture!"'.center(columns))
    time.sleep(3)

def field_of_foe(player, dime, barry):
    time.sleep(3)
    print('     *Squish, Squash*\n'.center(columns))
    time.sleep(3)

    print('"The Grass sure is wet here"\n'.center(columns))
    time.sleep(3)

    print('Yeah, I guess\n'.center(columns))
    time.sleep(1)

    print('"LOOK OVER THERE"\n'.center(columns))
    time.sleep(3)

    print('     You and Dime look into the distance and see your first challenge in the Field of Foe\n'.center(columns))
    time.sleep(3)

    print('     Two doors: The Left Door, and The Right Door.\n'.center(columns))
    time.sleep(3)

    print('     The only other thing you can see is a sign.\n'.center(columns))
    time.sleep(4)

    door_picture()

    print('Upon getting closer, you can read the sign.\n\n'.center(columns))
    time.sleep(3)

    print('"Answer my riddle three, and leave your fate up to me"'.center(columns))
    time.sleep(2)
    print('"Behind one of the doors is a Foe, and behind the other... you won’t know."'.center(columns))
    time.sleep(4)

    print('"Only one door has an enemy. That gives us good odds."'.center(columns))
    time.sleep(3)

    print('I guess you’re right, Dime.\n'.center(columns))
    time.sleep(3)

    while True:
        print('What door do you open?'.center(columns))
        print('a) The left door'.center(columns))
        print('b) The right door'.center(columns))

        door = centered_input()

        if door == 'a':
            left_door(player, barry)
            break
        elif door == 'b':
            right_door()
            break
        else:
            print(' . . . ')
            time.sleep(3)
            print(' . . . ')
            time.sleep(3)
            print('     "Uhhh dude, there’s 2 doors. Pick one"')
            time.sleep(3)
