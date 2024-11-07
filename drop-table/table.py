"""
	Create a table that takes in a dictionary of items in different categories...
	runes/ammunition
	weapons/armor
	other
	rares
"""

import random

class DropTable:
    table = {
        'ammo': [],      # 1 in 64 drop rate
        'weapons': [],   # 1 in 128 drop rate
        'other': [],     # 1 in 4 drop rate
        'rares': []      # 1 in 1500 drop rate
    }
    
    drop_rates = {
        'ammo': 64,
        'weapons': 128,
        'other': 4,
        'rares': 1500
    }

    def __init__(self):
        pass
    
    @classmethod
    def add_items(cls, category, item):
        if category in cls.table:
            cls.table[category].append(item)
        else:
            print(f"Category '{category}' does not exist.")
    
    def get_drop(self):
        drops = []
        for category, items in self.table.items():
            rate = self.drop_rates[category]
            if items and random.randint(1, rate) == 1:
                drops.append(random.choice(items))
        return drops

# Example usage:
# Create the drop table
drop_table = DropTable()

# Add items to each category
drop_table.add_items('ammo', 'Small Ammo Pack')
drop_table.add_items('weapons', 'Sword')
drop_table.add_items('other', 'Potion')
drop_table.add_items('rares', 'Legendary Sword')

# Simulate a drop
print("Generated drops:", drop_table.get_drop())