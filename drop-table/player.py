class Player:

    def __init__(self, name):
        self.name = name
        self.inventory = {}

    def add_items(self, items, quantity=1):
        if len(self.inventory) >= 28:
            print('Your inventory is full.')
        for item, detail in items.items():
            if item in self.inventory:
                self.inventory[item]['quantity'] += quantity
            else:
                self.inventory[item] = quantity

        print(f'{self.name} inventory: {self.inventory}')

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