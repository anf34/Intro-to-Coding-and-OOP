class Room:
	def __init__(self, name):
		"""TODO: Initialises a room. Do not change the function signature (line 2)."""
		...

	def get_name(self):
		"""TODO: Returns the room's name."""
		...

	def get_short_desc(self):
		"""TODO: Returns a string containing a short description of the room. This description changes based on whether or not a relevant quest has been completed in this room.

		If there are no quests that are relevant to this room, this should return: 'There is nothing in this room.' """
		...

	def get_quest_action(self):
		"""TODO: If a quest can be completed in this room, returns a command that the user can input to attempt the quest."""
		...

	def set_quest(self, q):
		"""TODO: Sets a new quest for this room."""
		...

	def get_quest(self):
		"""TODO: Returns a Quest object that can be completed in this room."""
		...
		
	def set_path(self, dir, dest):
		"""TODO: Creates an path leading from this room to another."""
		...

	def draw(self):
		"""TODO: Creates a drawing depicting the exits in each room."""
		...

	def move(self, dir):
		"""TODO: Returns an adjoining Room object based on a direction given. (i.e. if dir == "NORTH", returns a Room object in the north)."""
		...
