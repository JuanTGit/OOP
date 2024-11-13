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
        self.probability_table = {}
        

        for table, items in self.table.items():
            cumulative_drop_rate = 0
            for item in items:
                cumulative_drop_rate += item['rarity']
            self.probability_table[table] = cumulative_drop_rate

    
    def get_drop(self):
        table_roll = random.random()
        cumulative_table_prob = 0

        selected_table = None
        for table, chance in self.probability_table.items():
            cumulative_table_prob += chance
            if table_roll <= cumulative_table_prob:
                selected_table = table
                break
        
        if selected_table is None:
            selected_table = "Other"

        items = self.table[selected_table]
        cumulative_rarity = 0
        item_roll = random.random()
        
        for item in items:
            cumulative_rarity += item['rarity']
            if item_roll <= cumulative_rarity:
                return item
        
        return random.choice(items)
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