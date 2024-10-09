# Problem: Video Game Inventory System
# You are tasked with designing a game inventory system for a role-playing game (RPG). 
# Players can collect items such as weapons, armor, potions, and other equipment. 
# The system should allow the player to manage their inventory efficiently.

"""
Classes:
	Item:
		name
		weight
		value

		methods:
			use

		subclasses:
			weapons:
				damage
				durability

				methods:
					use
			armor:
				defense
				durability

				methods:
					use
			potion:
				healing_amount

				methods:
					use
	
	Inventory:
		items
		max_weight

		methods:
			add_item
			remove_items
			get_total_weight
			display_items
"""

class Item:
	def __init__(self, name, weight, value):
		self.name = name
		self.weight = weight
		self.value = value

	def use(self):
		print(f'You have used {self.name}.')
	
class Weapon(Item):
	def __init__(self, name, weight, value, damage, durability=10):
		super().__init__(name, weight, value)
		self.damage = damage
		self.durability = durability

	def use(self):
		if self.durability > 0:
			self.durability -= 1
		elif self.durability == 0:
			return f'{self.name} has broken'
		
class Armor(Item):
	def __init__(self, name, weight, value, defense, durability=10):
		super().__init__(name, weight, value)
		self.defense = defense
		self.durability = durability
	
	def use(self):
		if self.durability > 0:
			self.durability -= 1
		elif self.durability == 0:
			return f'{self.name} has broken'
		

class Potion(Item):
	def __init__(self, name, weight, value, healing_amount=50):
		super().__init__(name, weight, value)
		self.healing_amount = healing_amount
	
	def use(self):
		print(f'{self.name} has been used.')


class Inventory:
	def __init__(self):
		self.items = {}
		self.max_weight = 100
		self.current_weight = 0

	def add_item(self, item):
		if self.current_weight + item.weight > self.max_weight:
			return f"{item.name} is too heavy to fit in your inventory"
		elif item.name in self.items:
			self.items[item.name]['quantity'] += 1
		else:
			self.items[item.name] = {'item': item, 'quantity': 1}
		
		self.current_weight += item.weight
		print(f"{item.name} added to inventory")

	def remove_items(self, item, quantity):
		if item.name not in self.items:
			return f"{item.name} not found in inventory."
		elif quantity >= self.items[item.name]['quantity']:
			del self.items[item.name]
			print(f'{item.name} has been removed from your inventory.')
		else:
			self.items[item.name]['quantity'] -= quantity
			print(f'{quantity} removed from {item.name}')

	def get_total_weight(self):
		available_weight = self.max_weight - self.current_weight
		print(f"Current Weight: {self.current_weight}. Available Weight: {available_weight}")
		
	def display_items(self):
		for item, value in self.items.items():
			print(f"Item: {item} - Quantity: {value['quantity']}")


inventory = Inventory()
bronze_scimitar = Weapon('Bronze Scimitar', 10, 100, 5)
platebody = Armor('Steel Platebody', 12, 25, 10)
saradomin_brew = Potion('Saradomin Brew', 1, 5, 64)
abyssal_whip = Weapon('Abyssal Whip', 15, 200, 20, 30)

inventory.add_item(bronze_scimitar)
inventory.add_item(platebody)
inventory.add_item(saradomin_brew)
inventory.add_item(abyssal_whip)

inventory.display_items()