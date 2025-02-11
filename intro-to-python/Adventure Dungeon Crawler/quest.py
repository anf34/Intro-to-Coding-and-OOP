class Quest:
	def __init__(self, reward, action, desc, before, after, req, fail_msg, pass_msg, room):
		"""TODO: Initialises a quest."""
		...

	def get_info(self):
		"""TODO: Returns the quest's description."""
		...

	def is_complete(self):
		"""TODO: Returns whether or not the quest is complete."""
		...

	def get_action(self):
		"""TODO: Returns a command that the user can input to attempt the quest."""
		...

	def get_room_desc(self):
		"""TODO: Returns a description for the room that the quest is currently in. Note that this is different depending on whether or not the quest has been completed."""
		...

	def attempt(self, player):
		"""TODO: Allows the player to attempt this quest.

		Check the cumulative skill or will power of the player and all their items. If this value is larger than the required skill or will threshold for this quest's completion, they succeed and are rewarded with an item (the room's description will also change because of this).

		Otherwise, nothing happens."""
		...
