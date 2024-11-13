"""
	Create a table that takes in a dictionary of items in different categories...
	runes/ammunition
	weapons/armor
	other
	rares
"""
import random
from player import Player
from scraper import item_details

class DropTable:

    def __init__(self, table):
        self.table = table
    
    def get_drop(self):
        
        for table, items in self.table.items():
            print(f"======================={table}=======================")

            total_probability = sum(item['rarity'] for item in items)
            print(total_probability)

            # for item in items:
            #     print(item['rarity'])
            # for item in items:
            #     item['rarity'] = int(item['rarity'])
            

new_table = DropTable(item_details)

new_table.get_drop()



randomizer = random.random()
rarity = 8/127

didDrop = randomizer < rarity

# print(f"{didDrop}, randomizer: {randomizer} rarity: {rarity}")


# if __name__ == '__main__':
#     app.run(debug=True)