import sys
import time #imported here to make story.py cleaner!


#______________________________CLASSES____________________________________





#______________________________Races________________________________________



#Races
class Race:
    def __init__(self, name, strength, health_bonus):
        self.name = name
        self.strength = strength
        self.health_bonus = health_bonus





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




#_________________________________WEAPONS_________________________________________






class Weapon:
    def __init__(self, name, base_damage):
        self.name = name
        self.base_damage = base_damage
        


axe = Weapon("Axe", base_damage=4)
dimes_sword = Weapon("Dime's Sword", base_damage=5)
sword_of_anguish = Weapon("Sword of Anguish", base_damage=14)









#_________________________________Character Stuffz_________________________________




#Character, Player, enemy, etc inherit from this




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
        actual_damage = int(amount * self.defense)
        self.health -= actual_damage
        if self.health < 0:
            self.health = 0
        if self.health == 0:
            print(f"{self.user} has died.")
            if isinstance(self, Player):
                print("You died, idiot. Game over.")
                sys.exit()







class Player(Character):
    def __init__(self, name, race):
        super().__init__(name, 100 + race.health_bonus, race, axe)
        self.weapon_damage = self.weapon.base_damage + race.strength
        self.inventory = [axe]

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item.name} added to inventory.")

    def use_item(self, using):
        for item in self.inventory:
            if item.name.lower() == using.lower():
                if item.use_effect:
                    item.use_effect(self)
                    if item.type == "consumable":
                        self.inventory.remove(item)
                    return
                else:
                    print(f"{item.name} can't be used.")
                    return
        print("Item not found in inventory.")

    def equip_item(self, using):
        for item in self.inventory:
            if item.name.lower() == using.lower():
                if item.type == "equipment" and item.equip_effect:
                    item.equip_effect(self)
                    print(f"{item.name} equipped!")
                    return
                elif item.type == "weapon":
                    if using.lower() in weapon_registry:
                        self.weapon = weapon_registry[using.lower()]
                        self.weapon_damage = self.weapon.base_damage + self.race.strength
                        print(f"{item.name} equipped as weapon. Damage: {self.weapon_damage}")
                        return
                    else:
                        print(f"{item.name} is not a valid weapon object.")
                        return
                else:
                    print(f"{item.name} can't be equipped.")
                    return
        print("Item not found in inventory.")

    
    def print_inventory(self):
        print(f"{'Name':<10} {'Type':<10} {'Description':<10}")
        print('-' * 30)
        for item in self.inventory:
            print(f"{item.name:<10} {item.type:<10} {item.description:<20}")






class Dime(Character):
    def __init__(self):
        super().__init__("Dime", 100, human, dimes_sword)
        self.weapon_damage = self.weapon.base_damage + self.race.strength






class Enemy(Character):
    def __init__(self, name, health, damage, drop_items=None):
        super().__init__(name, health)
        self.damage = damage
        self.drop_items = drop_items or []






#__________________________________ITEMS_____________________________________





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
    description='A well-balanced axe. Solid for beginners.'
)

dimes_sword_item = Item(
    "Dime's Sword",
    type='weapon',
    description="A legendary sword wielded by Dime. It's light but deadly."
)

sword_of_anguish_item = Item(
    "Sword of Anguish",
    type='weapon',
    description='Forged in torment. Increases base damage significantly.'
)


weapon_registry = {
    "axe": axe,
    "dime's sword": dimes_sword,
    "sword of anguish": sword_of_anguish
}






#______________________________ITEM EFFECTS_________________________________






def use_sap_of_life(player):
    heal_amount = 30
    player.health += heal_amount
    if player.health > player.max_health:
        player.health = player.max_health
    print(f"{player.user} used the Sap of Life and healed {heal_amount} health! Current health: {player.health}")





def equip_bark_shield(player):
    player.defense = 0.5
    print(f"{player.user} equipped the Bark Shield. Less damage will be taken!")




#_______________________________ACTUAL ITEMS_______________________________________






sap_of_life = Item("Sap of Life", use_effect=use_sap_of_life, type='consumable')


bark_shield = Item("Bark Shield", equip_effect=equip_bark_shield, type='equipment')






#_______________________________ENEMIES______________________________________






tree = Enemy("Tree", health=200, damage=10, drop_items=[bark_shield, sap_of_life])


barry = Enemy("Barry", health=15, damage=2, drop_items=[])




