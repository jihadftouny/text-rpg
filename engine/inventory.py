# Inventory module for player and enemy

class Inventory:
    def __init__(self):
        self.weapons = []
        self.armor = []
        self.accessories = []
        self.potions = []
        self.equipped_weapon = None
        self.equipped_armor = None

    def add_item(self, item):
        if item['type'] == 'weapon':
            self.weapons.append(item)
        elif item['type'] == 'armor':
            self.armor.append(item)
        elif item['type'] == 'accessory':
            self.accessories.append(item)
        elif item['type'] == 'potion':
            self.potions.append(item)

    def equip_weapon(self, weapon):
        if weapon in self.weapons:
            self.equipped_weapon = weapon

    def equip_armor(self, armor):
        if armor in self.armor:
            self.equipped_armor = armor

    def view_inventory(self):
        return {
            'weapons': self.weapons,
            'armor': self.armor,
            'accessories': self.accessories,
            'potions': self.potions,
            'equipped_weapon': self.equipped_weapon,
            'equipped_armor': self.equipped_armor
        }
