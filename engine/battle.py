import random

def roll(d_sides):
    return random.randint(1, d_sides)

def roll_stat():
    rolls = [roll(6) for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)

def roll_all_stats(stats):
    return {stat: roll_stat() for stat in stats}
