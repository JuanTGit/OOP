class Player:

    def __init__(self, name):
        self.name = name
        self.raid_counter = 0
        self.inventory = {}
        self.last_item = []

    def add_item(self, items):
        self.raid_counter += 1
        self.last_item = [items['name'], int(items['quantity']), int(items['value'])]
        
        # print(self.inventory)

        drop = items['name']
        if drop in self.inventory:
            self.inventory[drop]['quantity'] += int(items['quantity'])
            self.inventory[drop]['value'] += int(items['value'])
        else:
            self.inventory[drop] = {
                'quantity': int(items['quantity']),
                'value': int(items['value']),
                'image': items['image']
            }

    def calculate_inventory(self):
        total = 0
        if self.inventory:
            for value in self.inventory.values():
                total += value['value']
        return total
    
    def drop_item(self):
        inv_last_item = self.inventory[self.last_item[0]]
        if self.last_item[1] <= inv_last_item['quantity']:
            inv_last_item['quantity'] -= self.last_item[1]
            inv_last_item['value'] -= self.last_item[2]
            return {'name': self.last_item[0], 'quantity': inv_last_item['quantity'], 'value': inv_last_item['value']}
        else:
            return "You don't have that item!"
        
    def drop_items(self, item):
        if item in self.inventory:
            del self.inventory[item]
        else:
            return 'Item not in inventory'

juant = Player('Juan T')
sherleyl = Player('Sherley L')
