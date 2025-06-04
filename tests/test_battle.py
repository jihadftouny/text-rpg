import unittest
from engine.battle import roll

class TestBattle(unittest.TestCase):
    def test_attack_roll(self):
        for _ in range(10):
            result = roll(20)
            self.assertTrue(1 <= result <= 20)

if __name__ == '__main__':
    unittest.main()
