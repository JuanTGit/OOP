class Player:

    def __init__(self, name):
        self.name = name
        self.raid_counter = 0
        self.inventory = {}

    def add_item(self, items):
        self.raid_counter += 1
        if len(self.inventory) >= 28:
            print('Your inventory is full.')
        drop = items['name']
        if drop in self.inventory:
            self.inventory[drop]['quantity'] += int(items['quantity'])
            self.inventory[drop]['value'] += int(items['value'])
        else:
            self.inventory[drop] = {
                'quantity': int(items['quantity']),
                'value': int(items['value'])
            }

    def calculate_inventory(self):
        total = 0
        if self.inventory:
            for value in self.inventory.values():
                total += value['value']
        return total
        
    def drop_item(self, item):
        print(self.inventory)
        if item in self.inventory:
            del self.inventory[item]
        else:
            return 'Item not in inventory'
        print(f'{item} removed from inventory')
        print(self.inventory)

juant = Player('Juan T')
sherleyl = Player('Sherley L')


