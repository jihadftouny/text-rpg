# Entry point for the game
import random
from engine.interactions import pick_from_catalog, CATALOGS
from engine.battle import roll, roll_all_stats
from engine.classes import CLASSES
from engine.inventory import Inventory
from engine.ai_narrator import get_ai_description

STATS = ["STR", "DEX", "CON", "INT", "WIS", "CHA"]
STAGE_INTERACTIONS = [
    ["Scenery", "NPC Interaction", "Scenery", "Battle", "Scenery", "Rest", "Treasure", "Battle"],
    ["Battle", "Scenery", "NPC Interaction", "Rest", "Treasure", "Battle", "Scenery", "Rest"],
    ["NPC Interaction", "Scenery", "Battle", "Treasure", "Rest", "Battle", "Scenery", "NPC Interaction"],
    ["Rest", "Battle", "Scenery", "Treasure", "NPC Interaction", "Battle", "Scenery", "Rest"],
    ["Treasure", "Battle", "Rest", "Scenery", "NPC Interaction", "Battle", "Rest", "Scenery"],
]

NUM_STAGES = len(STAGE_INTERACTIONS)


def character_creation():
    name = input("Enter your character's name: ")
    print("Choose your class:")
    for idx, c in enumerate(CLASSES.keys(), 1):
        print(f"  {idx}. {c}")
    while True:
        choice = input("Enter class number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(CLASSES):
            char_class = list(CLASSES.keys())[int(choice)-1]
            break
        print("Invalid choice. Try again.")
    while True:
        stats = roll_all_stats(STATS)
        print(f"\n{name} the {char_class}")
        for stat, value in stats.items():
            print(f"  {stat}: {value}")
        reroll = input("Re-roll stats? (y/n): ").strip().lower()
        if reroll == 'n':
            break
    print("Character creation complete!\n")
    return {"name": name, "class": char_class, "stats": stats, "inventory": Inventory()}


def handle_interaction(slot_num, interaction_type):
    print(f"Interaction {slot_num}: {interaction_type}")
    raw_data = pick_from_catalog(interaction_type)
    print(f"  [Catalog pick] {raw_data}")
    # To use AI: print(get_ai_description(interaction_type, raw_data))
    input("Press Enter to continue...")


def run_stage(stage_num, interaction_sequence):
    print(f"--- Stage {stage_num} ---")
    for i, interaction in enumerate(interaction_sequence, 1):
        handle_interaction(i, interaction)
    print(f"Stage {stage_num} complete!\n")


def run_game():
    print("Welcome to the Text RPG!\n")
    player = character_creation()
    for stage in range(1, NUM_STAGES + 1):
        run_stage(stage, STAGE_INTERACTIONS[stage - 1])
    print("Congratulations! You have completed all stages.")

if __name__ == "__main__":
    run_game()
