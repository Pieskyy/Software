import sys
import time
import shutil
import os


def clear_console(): # ( chatGPT https://chatgpt.com/c/684ea48f-fd48-800b-a4aa-bfea96e06e38) Screen Clear
     os.system('cls' if os.name == 'nt' else 'clear') 


def centered_input(prompt='>> '): # centers input statements
    return input(' ' * ((columns - len(prompt)) // 2) + prompt).lower() # same chatgpt log


enter = 0  # Set initial value for bar

columns, rows = shutil.get_terminal_size() # same ai log. for centering messages.



class Race:
    def __init__(self, name, strength, health_bonus):
        self.name = name
        self.strength = strength
        self.health_bonus = health_bonus

human = Race(
    "Human",
    strength=5,
    health_bonus=0
    )

elf = Race(
    "Elf",
    strength=3,
    health_bonus=-10
    )

orc = Race(
    "Orc",
    strength=9,
    health_bonus=20
    )

dwarf = Race(
    "Dwarf",
    strength=7,
    health_bonus=30
    )

worm = Race(
    "Worm",
    strength=6,
    health_bonus=-5
    )

grug = Race( # SECRET RACES
    "Grug",
    strength=40,
    health_bonus=200
    )

no = Race(
    "No",
    strength=0,
    health_bonus=-95
    )

races = { # Dictionary

    "human": human,
    "elf": elf,
    "orc": orc,
    "dwarf": dwarf,
    "worm": worm,
    "grug": grug,
    "no": no,
}


class Weapon:
    def __init__(self, name, base_damage):
        self.name = name
        self.base_damage = base_damage
        
axe = Weapon(
    "Axe",
    base_damage=400
    )

dimes_sword = Weapon(
    "Dime's Sword",
    base_damage=10
    )

sword_of_anguish = Weapon(
    "Sword of Anguish",
    base_damage=0.5
    )


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

    def take_damage(self, amount):
        actual_damage = max(0, int(amount * self.defense))  # apply defense multiplier
        self.health -= actual_damage
        if self.health < 0:
            self.health = 0
        if self.health == 0:
            print(f"{self.user} has died.".center(columns))
            if isinstance(self, Player):
                print("You died, idiot. Game over.".center(columns))
                sys.exit()
        return actual_damage

class Player(Character):
    def __init__(self, name, race):
        super().__init__(name, 100 + race.health_bonus, race, axe)
        self.weapon_damage = self.weapon.base_damage + race.strength
        self.inventory = [axe_item]
        self.equipped_equipment = None


    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item.name} added to inventory.".center(columns))

    def use_item(self, using):
        for item in self.inventory:

            if item.name.lower() == using.lower():
                if item.use_effect:
                    item.use_effect(self)

                    if item.type == "consumable":
                        self.inventory.remove(item)
                    return
                
                else:
                    print(f"{item.name} can't be used.".center(columns))
                    return
        print("Item not found in inventory.".center(columns))

    def equip_item(self, using):
        for item in self.inventory:
            if item.name.lower() == using.lower():

                if item.type == "equipment" and item.equip_effect:
                    self.equipped_equipment = item  # Track it
                    item.equip_effect(self)
                    print(f"{item.name} equipped!".center(columns))
                    return

            
                elif item.type == "weapon":
                    if using.lower() in weapon_registry:
                        self.weapon = weapon_registry[using.lower()]
                        self.weapon_damage = self.weapon.base_damage + self.race.strength
                        print(f"{item.name} equipped as weapon. Damage: {self.weapon_damage}".center(columns))
                        return
                    
                    else:
                        print(f"{item.name} is not a valid weapon object.".center(columns))
                        return
                    
                else:
                    print(f"{item.name} can't be equipped.".center(columns))
                    return
        print("Item not found in inventory.".center(columns))


    def print_inventory(self):
        while True:
            clear_console()
            print(f"{'No.':<4} {'Name':<25} {'Type':<12} {'Description'}".center(columns))
            print(('-' * 70).center(columns))
            for idx, item in enumerate(self.inventory, 1):
            # Mark equipped items
                if item.type == 'weapon' and self.weapon and self.weapon.name == item.name:
                    display_name = f"[{item.name}]"
                elif item.type == 'equipment' and self.equipped_equipment and self.equipped_equipment.name == item.name:
                    display_name = f"[{item.name}]"
                elif item.type == 'equipment':
                    display_name = item.name

                else:
                    display_name = item.name

                print(f"{idx:<4} {display_name:<25} {item.type:<12} {item.description}".center(columns))

            print(('-' * 70).center(columns))
            print('Choose an action: EQUIP (A), USE (B), BACK (C): '.center(columns))
            selection = centered_input()

            if selection == 'c':
                clear_console
                break  # exit inventory

            elif selection in ['a', 'b']:
                try:
                    print("Enter the item number:".center(columns))
                    item_number = centered_input()
                    item_number = int(item_number)
                    if 1 <= item_number <= len(self.inventory):
                        item = self.inventory[item_number - 1]
                    else:
                        print("Invalid item number.".center(columns))
                        continue
                except ValueError:
                    print("Please enter a valid number.".center(columns))
                    continue

                if selection == 'a':  # Equip
                    if item.type in ['weapon', 'equipment']:
                        self.equip_item(item.name)
                    else:
                        print(f"{item.name} cannot be equipped.").center(columns)
            
                elif selection == 'b':  # Use
                    if item.type == 'consumable':
                        self.use_item(item.name)
                    else:
                        print(f"{item.name} cannot be used.".center(columns))

            else:
                print("Invalid selection. Please choose A, B, or C.".center(columns))



class Dime(Character):
    def __init__(self):
        super().__init__("Dime", 100, human, dimes_sword)
        self.weapon_damage = self.weapon.base_damage + self.race.strength

class Enemy(Character):
    def __init__(self, name, health, damage, drop_items=None):
        super().__init__(name, health)
        self.damage = damage
        self.drop_items = drop_items or []


class Item:
    def __init__(self, name, use_effect=None, equip_effect=None, type='consumable', description='No Description'):
        self.name = name
        self.use_effect = use_effect
        self.equip_effect = equip_effect
        self.type = type
        self.description = description

axe_item = Item(
    "Axe",
    type='weapon',
    description='Your axe used to chop wood.'
)

dimes_sword_item = Item(
    "Dime's Sword",
    type='weapon',
    description="Dimes sword he tried to attack you with"
)

sword_of_anguish_item = Item(
    "Sword of Anguish",
    type='weapon',
    description='A stick. Literally a stick.'
)

weapon_registry = {
    "axe": axe,
    "dime's sword": dimes_sword,
    "sword of anguish": sword_of_anguish
}


def use_sap_of_life(player):
    heal_amount = 30
    player.health += heal_amount
    if player.health > player.max_health:
        player.health = player.max_health
    print(f"{player.user} used the Sap of Life and healed {heal_amount} health! Current health: {player.health}".center(columns))

def equip_bark_shield(player):
    player.defense = 0.5
    print(f"{player.user} equipped the Bark Shield. Less damage will be taken!".center(columns))

sap_of_life = Item(
    "Sap of Life",
    use_effect=use_sap_of_life,
    type='consumable',
    description='Mystical tree juice, capable of healing'
    )

bark_shield = Item(
    "Bark Shield",
    equip_effect=equip_bark_shield,
    type='equipment',
    description='Bark Ripped off the tree, deflects damage.'
    )

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
    drop_items=[sword_of_anguish]
    )
