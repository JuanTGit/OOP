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
		self.items[item.name] = {'item': item, 'quantity': 1}
		


inventory = Inventory()
bronze_scimitar = Weapon('Bronze Scimitar', 10, 100, 5)

inventory.add_item(bronze_scimitar)

print(inventory.items)