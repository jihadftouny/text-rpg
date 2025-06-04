import unittest
from engine.inventory import Inventory

class TestInventory(unittest.TestCase):
    def test_add_and_equip(self):
        inv = Inventory()
        sword = {'name': 'Sword', 'type': 'weapon'}
        armor = {'name': 'Chainmail', 'type': 'armor'}
        inv.add_item(sword)
        inv.add_item(armor)
        inv.equip_weapon(sword)
        inv.equip_armor(armor)
        self.assertEqual(inv.equipped_weapon, sword)
        self.assertEqual(inv.equipped_armor, armor)

if __name__ == '__main__':
    unittest.main()
