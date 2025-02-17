class Quest:
	def __init__(self, reward, action, desc, before, after, req, fail_msg, pass_msg, room):
		"""Initialises a quest."""
		self.reward = reward #Of the form item
		self.action = action
		self.desc = desc
		self.before = before
		self.after = after
		self.req = req
		self.req_skill = 0
		self.req_will = 0
		self.fail_msg = fail_msg
		self.pass_msg = pass_msg
		self.room = room
		self.is_complete = False


	def get_info(self):
		"""TODO: Returns the quest's description."""
		#DONE FOR NOW
		return self.desc

	def is_complete(self):
		"""TODO: Returns whether or not the quest is complete."""
		#DONE FOR NOW
		return self.is_complete
		...

	def get_action(self):
		"""TODO: Returns a command that the user can input to attempt the quest."""
		#DONE FOR NOW
		return self.action
		...

	def get_room_desc(self):
		"""TODO: Returns a description for the room that the quest is currently in. Note that this is different depending on whether or not the quest has been completed."""
		#DONE FOR NOW
		if not self.is_complete:
			return self.before
		else:
			return self.after

	def attempt(self, player):
		if self.is_complete:
			print("You have already completed this quest.")
		else:
			if player.get_skill() >= self.req_skill and player.get_will() >= self.req_will:
				self.is_complete = True
				player.take(self.reward)
				print(self.pass_msg)
			else:
				print(self.fail_msg)
		return "If you're seeing this text this method is not supposed to return anything."


		"""TODO: Allows the player to attempt this quest.

		Check the cumulative skill or will power of the player and all their items. If this value is larger than the required skill or will threshold for this quest's completion, they succeed and are rewarded with an item (the room's description will also change because of this).

		Otherwise, nothing happens."""
		...

	def get_skill_and_will(self):
		pass

	def get_after(self):
		return self.after

	def get_before(self):
		return self.before
