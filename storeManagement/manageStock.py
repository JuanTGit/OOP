class inventory:

	def __init__(self):
		self.inventory = {}
		self.perishable = {}
		self.thresholds = {}
		self.restock_quanities = {}

	def add_item(self, item_name, quantity):
		if item_name in self.inventory:
			self.inventory[item_name] += quantity
		else:
			self.inventory[item_name] = quantity

	def remove_item(self, item_name):
		if item_name in self.inventory:
			del self.inventory[item_name]

	def check_stock(self, item_name):
		if item_name in self.inventory:
			return self.inventory[item_name]
		else:
			return 'Item not found'
		
	def restock_item(self, item_name, quantity):
		if item_name in self.inventory:
			self.inventory[item_name] += quantity
		else:
			return f"{item_name} not found in inventory."

	def sell_item(self, item_name, quantity):
		if item_name in self.inventory:
			if self.inventory[item_name] >= quantity:
				self.inventory[item_name] -= quantity
				low_stock_alert = self.set_low_stock_threshold(item_name)
				if low_stock_alert:
					self.restock_item_if_needed(item_name)
					return f"Sold {quantity} of {item_name}. {low_stock_alert} Restocked {self.restock_quantities[item_name]} units."
				return f"Sold {quantity} of {item_name}"
			else:
				return f"Insufficient stock"
		else:
			return f"{item_name} not found in inventory."
		
	def set_low_stock_threshold(self, item_name):
		if item_name not in self.inventory:
			return
		
		quantity = self.inventory[item_name]
		threshold = self.thresholds.get(item_name, None)

		if threshold is not None and quantity < threshold:
			return f"Low stock alert! {item_name} has {quantity} remaining."
		return
		
	def set_threshold(self, item_name, threshold):
		self.thresholds[item_name] = threshold

	
	def add_item_with_expiration(self, item_name: str, quantity: int, expiration_date):
		self.perishable[item_name] = {'quantity': quantity, 'expiration_date': expiration_date}

	def remove_expired_items(self, current_date):
		items_to_delete = []
		for item, value in self.perishable.items():
			if value['expiration_date'] < current_date:
				items_to_delete.append(item)

		for item in items_to_delete:
			del self.perishable[item]
			if item in self.inventory:
				del self.inventory[item]
			print(f'{item} has expired.')
			
	def set_restock_quantity(self, item_name, quantity):
		self.restock_quanities[item_name] = quantity
	
	def restock_item_if_needed(self, item_name):
		if item_name in self.inventory and item_name in self.restock_quanities:
			self.inventory[item_name] += self.restock_quanities[item_name]
			if item_name in self.perishable:
				self.perishable[item_name]['quantity'] += self.restock_quanities[item_name]
			


heb = inventory()

# heb.add_item('chips', 5)
# heb.add_item('soda', 4)

heb.add_item_with_expiration('milk', 3, '2024-10-15')
heb.remove_expired_items('2024-10-16')
