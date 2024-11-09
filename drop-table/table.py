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
        'ammo': 64,
        'weapons': 128,
        'other': 4,
        'herbs': 32,
        'rares': 1500
    }

    def __init__(self):
        self.table = {
            'rares': {},      # 1 in 1500 drop rate
            'weapons': {},   # 1 in 128 drop rate
            'ammo': {},      # 1 in 64 drop rate
            'herbs': {},    # 1 in 32 drop rate
            'other': {}     # 1 in 4 drop rate
        }

    def add_items(self, category, item, quantity=1):
        if category in self.table:
            if item in self.table[category]:
                self.table[category][item] += quantity
            else:
                self.table[category][item] = quantity
        else:
            print(f"Category '{category}' does not exist.")
    
    def get_drop(self, player):
        for category, items in self.table.items():
            rate = self.drop_rates[category]
            if items and random.randint(1, rate) == 1 or category == 'other':
                drop = random.choice(list(items.keys()))
                player.add_items({drop: items[drop]})
                return
            
    

drop_table = DropTable()

cox = DropTable()
cox.add_items('ammo', 'Dragon arrows', quantity=250)
cox.add_items('herbs', 'Rannar weed', quantity=30)
cox.add_items('other', 'Teak plank', quantity=145)
cox.add_items('other', 'Mahogany plank', quantity=80)
cox.add_items('other', 'Dynamite', quantity=45)
cox.add_items('other', 'Dark relic', quantity=1)
cox.add_items('rares', 'Twisted Bow', quantity=1)
cox.add_items('rares', 'Dragon claws', quantity=1)
cox.get_drop(player.juant)
cox.get_drop(player.sherleyl)
# cox.add_items('ammo', ['Dragon arrows', 'Rune arrow', 'Soul rune', 'Blood rune', 'Death rune'])
# cox.add_items('herbs', ['Rannar weed', 'Toadflax', 'Irit leaf', 'Torstol', 'Snapdragon'])
# cox.add_items('other', ['Teak plank', 'Mahogany plank', 'Dynamite', 'Dark relic'])
# cox.add_items('rares', ['Twisted Bow', 'Kodai insignia', 'Elder Maul', 'Dragon claws', 'Ancestral piece', 'Prayer scroll', 'DHC'])

# print(cox.table)



