class Player:

    def __init__(self, name):
        self.name = name
        self.raid_counter = 0
        self.inventory = {}

    def add_item(self, items):
        self.raid_counter += 1
        if len(self.inventory) >= 28:
            print('Your inventory is full.')
        for item, values in items.items():
            if item in self.inventory:
                self.inventory[item]['quantity'] += values['quantity']
                self.inventory[item]['value'] += values['value']
            else:
                self.inventory[item] = values

        # print(self.inventory)

    def calculate_inventory(self):
        total = 0
        if self.inventory:
            for value in self.inventory.values():
                total += value['value']
        return total
        
    def remove_items(self):
        pass

juant = Player('Juan T')
sherleyl = Player('Sherley L')




# juant.add_items({
#     'bronze_sword': {
#         'item_name': 'Bronze sword',
#         'price': 100,
#         'quantity': 1
#     },
#     'mithril_scimitar': {
#         'item_name': 'Mithril scimitar',
#         'price': 250,
#         'quantity': 1
#     }
# })

# juant.add_items({
#     'bronze_sword': {
#         'item_name': 'Mithril scimitar',
#         'price': 250,
#         'quantity': 1
#     }
# }, 5)