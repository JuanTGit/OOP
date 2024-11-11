"""
	Create a table that takes in a dictionary of items in different categories...
	runes/ammunition
	weapons/armor
	other
	rares
"""
import random
# from player import juant
import player

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
            
            
    

drop_table = DropTable()
cox = DropTable()

cox.add_items('rares', {'Twisted bow': {'quantity': 1, 'value': 1600000000}, 'Edler maul': {'quantity': 1, 'value': 300000}, 'Kodai insigna': {'quantity': 250, 'value': 300000}})
cox.add_items('weapons', {'Dragon arrows': {'quantity': 250, 'value': 300000}, 'Rune arrow': {'quantity': 250, 'value': 300000}, 'Soul rune': {'quantity': 250, 'value': 300000}, 'Blood rune': {'quantity': 250, 'value': 300000}, 'Death rune': {'quantity': 250, 'value': 300000}})
cox.add_items('ammo', {'Dragon arrows': {'quantity': 250, 'value': 300000}, 'Rune arrow': {'quantity': 250, 'value': 300000}, 'Soul rune': {'quantity': 250, 'value': 300000}, 'Blood rune': {'quantity': 250, 'value': 300000}, 'Death rune': {'quantity': 250, 'value': 300000}})
cox.add_items('herbs', {'Dragon arrows': {'quantity': 250, 'value': 300000}, 'Rune arrow': {'quantity': 250, 'value': 300000}, 'Soul rune': {'quantity': 250, 'value': 300000}, 'Blood rune': {'quantity': 250, 'value': 300000}, 'Death rune': {'quantity': 250, 'value': 300000}})
cox.add_items('other', {'Dragon arrows': {'quantity': 250, 'value': 300000}, 'Rune arrow': {'quantity': 250, 'value': 300000}, 'Soul rune': {'quantity': 250, 'value': 300000}, 'Blood rune': {'quantity': 250, 'value': 300000}, 'Death rune': {'quantity': 250, 'value': 300000}})

cox.get_drop(player.juant)
cox.get_drop(player.sherleyl)
# cox.add_items('ammo', ['Dragon arrows', 'Rune arrow', 'Soul rune', 'Blood rune', 'Death rune'])
# cox.add_items('herbs', ['Rannar weed', 'Toadflax', 'Irit leaf', 'Torstol', 'Snapdragon'])
# cox.add_items('other', ['Teak plank', 'Mahogany plank', 'Dynamite', 'Dark relic'])
# cox.add_items('rares', ['Twisted Bow', 'Kodai insignia', 'Elder Maul', 'Dragon claws', 'Ancestral piece', 'Prayer scroll', 'DHC'])

# print(cox.table)



