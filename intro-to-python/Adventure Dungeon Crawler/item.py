class Item:
	def __init__(self, name, short, skill_bonus, will_bonus):
		#"""TODO: Initialises an item."""
		self.validate_input(name, short, skill_bonus, will_bonus)
		self.name = name
		self.short = short
		self.skill_bonus = skill_bonus
		self.will_bonus = will_bonus
		self.obtained = False

	def validate_input(self, name, short, skill_bonus, will_bonus):
		if not (name and isinstance(name, str)):
			raise TypeError("name must be of type str and non-empty.")
			if not (short and isinstance(short, str)):
				raise TypeError("short must be of type str and non-empty.")
				if not isinstance(skill_bonus, int):
					raise TypeError("skill_bonus must be of type int and non-empty.")
		if not isinstance(will_bonus, int):
			raise TypeError("will_bonus must be of type int and non-empty.")

	def get_name(self):
		return self.name

	def set_name(self, name):
		self.validate_name(name)
		self.name = name

	def get_short(self):
		return self.short

	def set_short(self, short):
		self.validate_short(short)
		self.short = short

	def get_skill_bonus(self):
		return self.skill_bonus

	def set_skill_bonus(self, skill_bonus):
		self.validate_skill_bonus(skill_bonus)
		self.skill_bonus = skill_bonus

	def get_will_bonus(self):
		return self.will_bonus

	def set_will_bonus(self, will_bonus):
		self.validate_will_bonus(will_bonus)
		self.will_bonus = will_bonus

	def set_obtained(self, obtained):
		self.obtained = obtained

	def get_obtained(self):
		return self.obtained

	def item_obtain(self):
		self.obtained = True


	def get_info(self):
		#"""TODO: Prints information about the item."""
		info = f"{self.name}\nGrants a bonus of {self.skill_bonus} to SKILL.\nGrants a bonus of {self.will_bonus} to WILL."
		return info
