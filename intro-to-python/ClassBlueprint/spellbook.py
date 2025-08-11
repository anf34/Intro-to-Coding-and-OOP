class Spellbook:
	def __init__(self, material, capacity):
		self.validate_input(material, capacity)
		self.material = material
		self.capacity = capacity

	def validate_input(self, material, capacity):
		self.validate_material(material)
		self.validate_capacity(capacity)

	def get_material(self):
		return self.material

	def get_capacity(self):
		return self.capacity

	def set_material(self, material):
		self.validate_material(material)
		self.material = material

	def set_capacity(self, capacity):
		self.validate_capacity(capacity)
		self.capacity = capacity

	def validate_material(self, material):
		if not (material and isinstance(material, str)):
			raise TypeError('Material must be of type str and non empty.')

	def validate_capacity(self, capacity):
		if not isinstance(capacity, int)):
			raise TypeError('Capacity must be of type int and non empty.')

	def add_spell(self):
		pass

	def cast_spell(self):
		pass

	def cast_strongest(self):
		pass

	def cast_all(self):
		pass

	def recharge_all(self):
		pass

