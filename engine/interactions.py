import random
import json
from pathlib import Path

def load_catalog(filename):
    path = Path(__file__).parent.parent / 'data' / filename
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

SCENERY = load_catalog('scenery.json')
NPCS = load_catalog('npcs.json')
ENEMIES = load_catalog('enemies.json')
ITEMS = load_catalog('items.json')

CATALOGS = {
    'Scenery': SCENERY,
    'NPC Interaction': NPCS,
    'Battle': ENEMIES,
    'Treasure': ITEMS,
    'Rest': ["A safe campfire for a short rest.", "A cozy inn for a long rest.", "A quiet grove to meditate.", "A hidden alcove to sleep."]
}

def pick_from_catalog(interaction_type):
    catalog = CATALOGS.get(interaction_type, [])
    if not catalog:
        return None
    return random.choice(catalog)
