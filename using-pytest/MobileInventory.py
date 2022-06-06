class InsufficientException(Exception):
	pass

class MobileInventory(object):
	def __init__(self, inventory=None):
		self.balance_inventory = inventory
		for element in self.balance_inventory:
			if not element:
				self.balance_inventory = {}
			else:
				if not isinstance(self.balance_inventory, dict):
					raise TypeError('Input inventory must be a dictionary')
				elif not set(map(type, self.balance_inventory.keys())) == {str}:
					raise ValueError('Mobile model name must be a string')
				elif not set(map(type, self.balance_inventory.values())) == {int}:
					raise ValueError('No. of mobiles must be a positive integer')
				else:
					for val in self.balance_inventory.values():
						if val < 0:
							raise ValueError('No. of mobiles must be a positive integer')

	def add_stock(self, new_stock):
		if not isinstance(new_stock, dict):
			raise TypeError('Input inventory must be a dictionary')
		elif not set(map(type, new_stock.keys())) == {str}:
			raise ValueError('Mobile model name must be a string')
		elif not set(map(type, new_stock.values())) == {int}:
			raise ValueError('No. of mobiles must be a positive integer')
		else:
			for val in new_stock.values():
				if val < 0:
					raise ValueError('No. of mobiles must be a positive integer')

		for key, value in new_stock.items():
			if key in self.balance_inventory:
				self.balance_inventory[key] += value
			else:
				self.balance_inventory[key] = value

	def sell_stock(self, requested_stock):
		if not isinstance(requested_stock, dict):
			raise TypeError('Input inventory must be a dictionary')
		elif not set(map(type, requested_stock.keys())) == {str}:
			raise ValueError('Mobile model name must be a string')
		elif not set(map(type, requested_stock.values())) == {int}:
			raise ValueError('No. of mobiles must be a positive integer')
		else:
			for val in requested_stock.values():
				if val < 0:
					raise ValueError('No. of mobiles must be a positive integer')

		for key, value in requested_stock.items():
			if not self.balance_inventory.get(key):
				raise InsufficientException('No Stock. New Model Request')
			elif self.balance_inventory.get(key) < value:
				raise InsufficientException('Insufficient Stock')
			else:
				self.balance_inventory[key] -= value

	def print_data(self):
		for key, value in self.balance_inventory.items():
			print(key, value)
