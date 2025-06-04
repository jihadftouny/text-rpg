import unittest
from engine.battle import roll, roll_stat

class TestDice(unittest.TestCase):
    def test_roll(self):
        for sides in [2, 4, 6, 8, 12, 20]:
            for _ in range(10):
                result = roll(sides)
                self.assertTrue(1 <= result <= sides)

    def test_roll_stat(self):
        for _ in range(10):
            stat = roll_stat()
            self.assertTrue(3 <= stat <= 18)

if __name__ == '__main__':
    unittest.main()
