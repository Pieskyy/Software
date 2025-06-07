import sys
import time

#________________________________CLASSES____________________________________



class Race:
    def __init__(self, name, strength, health_bonus):
        self.name = name
        self.strength = strength
        self.health_bonus = health_bonus
    


class Weapon:
    def __init__(self, name, base_damage):
        self.name = name
        self.base_damage = base_damage




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

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item.name} added to inventory.")

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




class Player(Character):
    def __init__(self, name, race):
        super().__init__(name, 100 + race.health_bonus, race, axe)
        self.weapon_damage = self.weapon.base_damage + race.strength




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
    def __init__(self, name, use_effect=None, equip_effect=None, type='consumable'):
        self.name = name
        self.use_effect = use_effect
        self.equip_effect = equip_effect
        self.type = type

    def use_sap_of_life(player):
        heal_amount = 30
        player.health += heal_amount
        if player.health > player.max_health:
            player.health = player.max_health
            print(f"{player.user} used the Sap of Life and healed {heal_amount} health! Current health: {player.health}")

    def equip_bark_shield(player):
        player.defense = 0.5
        print(f"{player.user} equipped the Bark Shield. less damage will be taken!")


#__________________________________ITEMS_____________________________________

def use_sap_of_life(player):
    heal_amount = 30
    player.health += heal_amount
    if player.health > player.max_health:
        player.health = player.max_health
    print(f"{player.user} used the Sap of Life and healed {heal_amount} health! Current health: {player.health}")



def equip_bark_shield(player):
    player.defense = 0.5
    print(f"{player.user} equipped the Bark Shield. Less damage will be taken!")



sap_of_life = Item("Sap of Life", use_effect=use_sap_of_life, type='consumable')
bark_shield = Item("Bark Shield", equip_effect=equip_bark_shield, type='equipment')



#_________________________________ENEMIES_____________________________________





tree = Enemy("Tree", health=200, damage=10, drop_items=["Bark Shield", "Sap of Life"])
barry = Enemy("Barry", health=15, damage=2, drop_items=["Stick of Anquish"])



#_________________________________WEAPONS______________________________________





axe = Weapon("Axe", base_damage=4)
dimes_sword = Weapon("Dime's Sword", base_damage=5)




#_________________________________RACES_________________________________________





human = Race("Human", strength=5, health_bonus=0)
elf = Race("Elf", strength=3,  health_bonus=-10)
orc = Race("Orc", strength=9, health_bonus=20)
dwarf = Race("Dwarf", strength=7, health_bonus=30)
worm = Race("worm", strength=6, health_bonus=-5)
grug = Race("grug", strength=40, health_bonus=200)
no = Race("no", strength=0, health_bonus=-95)




races = { #Dictionarie of Races
    "human": human,
    "elf": elf,
    "orc": orc,
    "dwarf": dwarf,
    "worm":worm,
    "grug":grug,
    "no":no,
}






