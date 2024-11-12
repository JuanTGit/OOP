"""
	Create a table that takes in a dictionary of items in different categories...
	runes/ammunition
	weapons/armor
	other
	rares
"""
import random
# from player import juant
from player import Player
from scraper import item_details
from flask import Flask

app = Flask(__name__)

# print(item_details)
class DropTable:    
    drop_rates = {
        'rares': 1500,
        'weapons': 128,
        'ammo': 64,
        'herbs': 32,
        'other': 4
    }

    def __init__(self):
        self.table = {
            'rares': {},      # 1 in 1500 drop rate
            'weapons': {},   # 1 in 128 drop rate
            'ammo': {},      # 1 in 64 drop rate
            'herbs': {},    # 1 in 32 drop rate
            'other': {}     # 1 in 4 drop rate
        }

    def add_item(self, category, item, quantity=1):
        if category in self.table:
            if item in self.table[category]:
                self.table[category][item] += quantity
            else:
                self.table[category][item] = quantity
        else:
            print(f"Category '{category}' does not exist.")

    def add_items(self, category, dictItems):
        if category in self.table:
            for k, v in dictItems.items():
                self.table[category][k] = v
    
    def get_drop(self, player):
        for category, items in self.table.items():
            rate = self.drop_rates[category]
            if items and random.randint(1, rate) == 1 or category == 'other':
                drop = random.choice(list(items.keys()))
                drop_copy = items[drop].copy()
                player.add_item({drop: drop_copy})
                return (f"Raid's Completed: {player.raid_counter}", sorted(player.inventory.items(), key=lambda item: item[1]['value'], reverse=True), f'Total Value: {player.calculate_inventory():,} gp')
            

for table, items in item_details.items():
    print(table)

randomizer = random.random()
rarity = 8/127

didDrop = randomizer < rarity

# print(f"{didDrop}, randomizer: {randomizer} rarity: {rarity}")
