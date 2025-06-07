import sys
import time

# _______________________________ CLASSES _______________________________

class Race:
    def __init__(self, name, strength, health_bonus):
        self.name = name
        self.strength = strength
        self.health_bonus = health_bonus

class Weapon:
    def __init__(self, name, base_damage, description=""):
        self.name = name
        self.base_damage = base_damage
        self.description = description
        self.equip_effect = self.equip_weapon

    def equip_weapon(self, player):
        player.weapon = self
        player.weapon_damage = self.base_damage + player.race.strength
        player.equipped["weapon"] = self.name
        print(f"{player.user} equipped {self.name}!")

class Item:
    def __init__(self, name, description="", use_effect=None, equip_effect=None, type='consumable'):
        self.name = name
        self.description = description
        self.use_effect = use_effect
        self.equip_effect = equip_effect
        self.type = type

# ____________________________ ITEM EFFECTS ____________________________

def use_sap_of_life(player):
    heal_amount = 30
    player.health += heal_amount
    if player.health > player.max_health:
        player.health = player.max_health
    print(f"{player.user} used the Sap of Life and healed {heal_amount} health! Current health: {player.health}")

def equip_bark_shield(player):
    player.defense = 0.5
    player.equipped["shield"] = "Bark Shield"
    print(f"{player.user} equipped the Bark Shield. Less damage will be taken!")

# _____________________________ CHARACTERS _____________________________

class Character:
    def __init__(self, name, health, race=None, weapon=None):
        self.user = name
        self.race = race
        self.max_health = health
        self.health = health
        self.weapon = weapon
        self.weapon_damage = (weapon.base_damage + race.strength) if weapon and race else 0
        self.defense = 1.0
        self.inventory = []
        self.equipped = {"weapon": weapon.name if weapon else None, "shield": None}

    def take_damage(self, amount):
        actual_damage = int(amount * self.defense)
        self.health -= actual_damage
        if self.health < 0:
            self.health = 0
        print(f"{self.user} took {actual_damage} damage. Health now: {self.health}")
        if self.health == 0:
            print(f"{self.user} has died.")
            if isinstance(self, Player):
                print("You died, idiot. Game over.")
                sys.exit()

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"> {item.name} added to inventory.")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                if item.use_effect:
                    item.use_effect(self)
                    self.inventory.remove(item)
                    return
                else:
                    print(f"{item.name} can't be used.")
                    return
        print("Item not found in inventory.")

    def equip_item(self, item_name):
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                if item.equip_effect:
                    item.equip_effect(self)
                    return
                else:
                    print(f"{item.name} can't be equipped.")
                    return
        print("Item not found in inventory.")

    def show_inventory(self):
        print("\n--- INVENTORY ---")
        if not self.inventory:
            print("Inventory is empty.")
            return
        for i, item in enumerate(self.inventory):
            display_name = item.name
            if item.name == self.equipped.get("weapon") or item.name == self.equipped.get("shield"):
                display_name = f"[{item.name}]"
            print(f"{i+1}. {display_name} - {item.description}")
        print("------------------")

class Player(Character):
    def __init__(self, name, race):
        super().__init__(name, 100 + race.health_bonus, race, axe)
        self.weapon_damage = self.weapon.base_damage + race.strength
        self.inventory.append(axe)
        self.equipped["weapon"] = axe.name

class Dime(Character):
    def __init__(self):
        super().__init__("Dime", 100, human, dimes_sword)
        self.weapon_damage = self.weapon.base_damage + self.race.strength

class Enemy(Character):
    def __init__(self, name, health, damage, drop_items=None):
        super().__init__(name, health)
        self.damage = damage
        self.drop_items = drop_items or []

# ____________________________ ITEMS SETUP ____________________________

sap_of_life = Item("Sap of Life", description="Heals 30 health", use_effect=use_sap_of_life)
bark_shield = Item("Bark Shield", description="Reduces incoming damage by 50%", equip_effect=equip_bark_shield, type='equipment')


# ____________________________ WEAPONS SETUP ____________________________

axe = Weapon("Axe", base_damage=4, description="Basic axe, does 4 damage.")
dimes_sword = Weapon("Dime's Sword", base_damage=5, description="Slightly better than an axe.")
sword_of_anquish = Weapon("Sword of Anquish", base_damage=1, description="It's a stick . . .")


# ____________________________ RACES SETUP ____________________________

human = Race("Human", strength=5, health_bonus=0)
elf = Race("Elf", strength=3, health_bonus=-10)
orc = Race("Orc", strength=9, health_bonus=20)
dwarf = Race("Dwarf", strength=7, health_bonus=30)
worm = Race("Worm", strength=6, health_bonus=-5)
grug = Race("Grug", strength=40, health_bonus=200)
no = Race("No", strength=0, health_bonus=-95)

races = {
    "human": human,
    "elf": elf,
    "orc": orc,
    "dwarf": dwarf,
    "worm": worm,
    "grug": grug,
    "no": no,
}

# ____________________________ ENEMIES SETUP ____________________________

tree = Enemy("Tree", health=200, damage=10, drop_items=[bark_shield, sap_of_life])
barry = Enemy("Barry", health=5, damage=10, drop_items=[sword_of_anquish])



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






print('______________________________________SELECTION_SCREEN___________________________________')


print('\n'*15)


name = input('What do you wish to be called?: ' + ('\n' * 10)) #Name


print('\n' * 10)


#Races
print('\n\n                                               POSSIBLE RACES')
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


player = Player(name, chosen_race)
dime = Dime()

print('\n' * 30) #Screen Clear



#Hint-like screen
print('"TEXT" Refers to other characters. if without "", it is your Character.\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
time.sleep(5)



print('\n' * 30)#Show of Stats so far

time.sleep(2)#Back story lore ish idk
print('You are in a forest. chopping wood for a fire when suddenly you hear . . .\n\n')
time.sleep(2)
print('     *Bushes rustling in the distance, getting louder and louder as it approaches you*')
time.sleep(2)
print('     *You see a figure jump out of the bushes, wielding a sword and charging at you*\n')



time.sleep(2)#First Interaction with other characters.
print('"YOU BEAST ILL GET YOU"\n')
time.sleep(3)
print('"Wait . . ."\n')
time.sleep(2)
print('"Youre no monster. . . ."\n')
time.sleep(3)
print('\n"So uhhh . . . anyways, Im Dime, and you are?"\n')
time.sleep(2)
print('I am ', name )
time.sleep(3)




print('\n\n\n\n')#Show of Stats so far
dime = Dime()
player = Player(name, chosen_race)
print(f"Player created with name: {player.user} and health: {player.health} and race: {player.race.name} ")
print(f"Fellow created with name: {dime.user} and health: {dime.health} and race: {dime.race.name}")
time.sleep(4)
print('\n'*6)




print('               The Story Continues . . . ')#Story Continuation
print('\n' * 6)



time.sleep(3)
print('"Thats a lovely name. ', name, ' I love it!"\n')
time.sleep(2)
print('"Anyways . . . ', name, 'I need your help. And i need it now."')
time.sleep(2)


input('\n"Are you up for the Challenge?"\n')
time.sleep(2)#No Matter whats said, its a yes so storyc an continue
print('"Sounds like a Yes to me!, Sweet!!"\n')
time.sleep(2)



#Main point of story. To save Helga.
print('"Im getting side tracked here, there are more important measures at stake"')
time.sleep(1)
print('"Its . . . "')
time.sleep(2)
print('"Its . . My friend Helga, shes been uhh . . . "')
time.sleep(1)
print('"Kidnapped."\n')
time.sleep(1)





input('"Are you still able to help me?"\n ')
time.sleep(2) #same as before, makes dime seem like he doesnt care and does need this health
print('"Still sounds like a Yes to me!')
time.sleep(3)



#Semi-clear screen so it can make this like seem more important
print('\n'*6)
print('               Where Should we go first ', name,'?')
print('\n\n\n')



time.sleep(1)



#path choosing, defined so it can be called back on to come back to.
def choose_path(player, dime, tree):
    player_health = player.health

    while True:




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
            time.sleep(1)#                                                              |
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
                              '  c) Befriend it\n\n').lower()#                          |
                time.sleep(1)#                                                          |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|///___________________________________FIGHT 1 A____________________________________\\\|
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
                if fight == 'a':#                                                       |
#|                                                                                      |
                    print('You get your weapon ready and engage in battle... against a tree?\n\n')
                    time.sleep(1)#                                                      |
                    print('   You attack the Tree and it smacks you back')# 
#|                                                                                      | 
#|                                                                                      |    
#|                                                                                      |
#|                   PLayer and Enemy (Tree) take                                       |
                    player.take_damage(tree.damage)#                                    |
                    tree.health -= player.weapon_damage#                                |
#|                                                                                      |
#|                   if Tree health goes into Negatives (e.g, -15), its registered as 0 |
                    if tree.health < 0:#                                                |
                        tree.health = 0#                                                |
#|                                                                                      |    
#|                   Prints Tree and player Health so player can know whos at what      |
                    print(f"{player.user}'s health: {player.health}")#                  |
                    print(f"{tree.user}'s health: {tree.health}")#                      |
                    time.sleep(1)#                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|///_______________________________FIGHT 1 B________________________________________\\\|
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
#|                                                                                      |
                elif fight == 'b':#                                                     |
                    print('You decide to retreat...')#                                  |
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

        elif choice == 'c':
            print('You step into the tavern, the smell of ale and stories thick in the air...')
            break

        else:
            print("That’s not a valid choice. Try again.")

    return player_health

player_health = choose_path(player, dime, tree)
print(f"\nYou finished choosing a path. Your health is {player_health}. Game continues here...")
