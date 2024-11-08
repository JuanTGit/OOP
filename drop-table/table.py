"""
	Create a table that takes in a dictionary of items in different categories...
	runes/ammunition
	weapons/armor
	other
	rares
"""

import random

class Player:

    def __init__(self):
        self.inventory = {}

    def add_items(self, items, quantity=1):
        for item, detail in items.items():
            if item in self.inventory:
                self.inventory[item]['quantity'] += quantity
            else:
                self.inventory[item] = self.inventory.get(item, detail)

        print(self.inventory)

juant = Player()

juant.add_items({
    'bronze_sword': {
        'item_name': 'Bronze sword',
        'price': 100,
        'quantity': 1
    },
    'mithril_scimitar': {
        'item_name': 'Mithril scimitar',
        'price': 250,
        'quantity': 1
    }
})

juant.add_items({
    'bronze_sword': {
        'item_name': 'Mithril scimitar',
        'price': 250,
        'quantity': 1
    }
}, 5)

class DropTable:    
    drop_rates = {
        'ammo': 64,
        'weapons': 128,
        'other': 4,
        'rares': 1500
    }

    def __init__(self):
        self.table = {
            'rares': [],      # 1 in 1500 drop rate
            'weapons': [],   # 1 in 128 drop rate
            'ammo': [],      # 1 in 64 drop rate
            'herbs': [],    # 1 in 32 drop rate
            'other': []     # 1 in 4 drop rate
        }

    def add_items(self, category, item):
        if category in self.table:
            self.table[category].append(item)
        else:
            print(f"Category '{category}' does not exist.")
    
    def get_drop(self):
        drops = []
        for category, items in self.table.items():
            rate = self.drop_rates[category]
            if items and random.randint(1, rate) == 1 or category == 'other':
                drops.append(random.choice(items))
                return drops

drop_table = DropTable()

# drop_table.add_items('ammo', 'Small Ammo Pack')
# drop_table.add_items('weapons', 'Sword')
# drop_table.add_items('other', 'Potion')
# drop_table.add_items('rares', 'Legendary Sword')

# high_level_monster = DropTable()
# high_level_monster.add_items('ammo', ['Dragon arrows', 'Rune arrow', 'Soul rune', 'Blood rune', 'Death rune'])
# high_level_monster.add_items('herbs', ['Rannar weed', 'Toadflax', 'Irit leaf', 'Torstol', 'Snapdragon'])
# high_level_monster.add_items('other', ['Teak plank', 'Mahogany plank', 'Dynamite', 'Dark relic'])
# high_level_monster.add_items('rares', ['Twisted Bow', 'Kodai insignia', 'Elder Maul', 'Dragon claws', 'Ancestral piece', 'Prayer scroll', 'DHC'])


# print(drop_table.table)
# print(high_level_monster.table)