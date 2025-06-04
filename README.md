# Text RPG Skeleton
# ==================
# 
# FEATURES SPECIFICATION:
# - Text-based RPG with 5 stages, each containing 8 user interactions
# - Interaction types catalog:
#     * Scenery description
#     * NPC interaction (variations: vendor, quest-giver, help-seeker, etc.)
#     * Battle encounter (enemies with D&D stats + skills + loot drops)
#     * Treasure discovery
#     * Rest (short or long)
# - Manual stage layout: for each stage, define the exact sequence of interaction types
# - AI-powered narrative: use OpenAI (or other API) to dynamically generate text for each interaction
# - Player setup:
#     * Randomized D&D-style stats (STR, DEX, CON, INT, WIS, CHA)
#     * Dice system (d2, d4, d6, d8, d12, d20) for all checks (attacks, skills, saving throws)
#     * Class selection at game start (3 classes, each with unique skills and loot pools)
# - Inventory & equipment:
#     * Weapons (one-handed, two-handed)
#     * Armor (full set as single item)
#     * Accessories (rings, amulets, augmentations)
#     * Potions & consumables
# - Battle mechanics:
#     * Attack & defense resolution via dice rolls (compare d20 rolls + modifiers)
#     * Enemy AI can use skills and roll dice
#     * Loot drops on enemy defeat


# Project Overview
# This Python-based, AI-powered text RPG guides players through five handcrafted stages, each containing eight unique interactions—ranging from scenery descriptions and NPC dialogues to battles, treasures, and rests.
# Narrative text for each interaction is dynamically generated via the OpenAI API (or another language model).
# 
# Key Features
# - Five Stages × Eight Slots: Manually define the sequence of interaction types for each stage.
# - Interaction Types Catalog:
#     * Scenery descriptions
#     * NPC interactions (vendor, quest-giver, help-seeker, etc.)
#     * Battle encounters (D&D-style stats, skills, loot drops)
#     * Treasure discoveries
#     * Rests (short, long)
# - Player Setup:
#     * Randomized D&D stats (STR, DEX, CON, INT, WIS, CHA)
#     * Dice-roller supporting d2, d4, d6, d8, d12, d20
#     * Class selection (three starter classes with unique skills & loot pools)
# - Inventory & Equipment:
#     * Weapons (one- or two-handed)
#     * Armor sets
#     * Accessories (rings, amulets, augmentations)
#     * Consumables (potions)
# - Battle Mechanics:
#     * Attack/defense resolution via dice rolls + modifiers
#     * Enemy AI with skill usage and loot drops
# - AI Narrative:
#     * Prompt-based text generation for each interaction