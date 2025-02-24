import math

class Room:
	def __init__(self, name):
		"""TODO: Initialises a room. Do not change the function signature (line 2)."""
		self.name = name
		self.quest = None
		self.north = None
		self.south = None
		self.east = None
		self.west = None

	def get_name(self):
		return self.name

	def get_short_desc(self):
		# """TODO: Returns a string containing a short description of the room. This description changes based on whether or not a relevant quest has been completed in this room.

		# If there are no quests that are relevant to this room, this should return: 'There is nothing in this room.' """
		if not self.quest:
			return "There is nothing in this room."
		else:
			if self.quest.is_complete():
				return self.quest.get_after()
			if not self.quest.is_complete():
				return self.quest.get_before()
			else:
				return "You shouldn't be seeing this. Fix room.py"

	def get_quest_action(self):
		#Done for now
		# """TODO: If a quest can be completed in this room, returns a command that the user can input to attempt the quest."""
		if not self.quest:
			return "There is nothing in this room."
		else:
			return self.quest.get_action()


	def set_quest(self, q):
		self.quest = q

	def get_quest(self):
		return self.quest

	def set_path(self, dir, dest):
		"""TODO: Creates an path leading from this room to another."""
		if dir == "NORTH":
			self.north = dest
		elif dir == "SOUTH":
			self.south = dest
		elif dir == "EAST":
			self.east = dest
		elif dir == "WEST":
			self.west = dest
		else:
			print("Error. That is not a compass direction.")

	def draw(self):
		#"""TODO: Creates a drawing depicting the exits in each room."""
		room_width = 22 #Please keep this even
		room_height = 11 #And this odd

		#Make a list of lists for the display of the room
		room_grid = [[0 for _ in range(room_width)] for _ in range(room_height)]

		#Starting in the first row, iterate through each spot and place an icon
		for i in range(0, room_height):

			#Iterate through width of the room
			for j in range(0, room_width):
				#Place + at corners
				if (i == 0 or i == room_height - 1) and (j == 0 or j == room_width - 1):
					room_grid[i][j] = "+"

				#West and East walls: if in first or last element of a row, place |, or if in middle of room place a door if there is an adjacent room.
				elif (j == 0 or j == (room_width - 1)):
					if i != int((room_height - 1) / 2):
						room_grid[i][j] = "|"

					elif self.get_west() and j == 0:
						room_grid[i][j] = "W"

					elif self.get_east() and j == room_width - 1:
						room_grid[i][j] = "E"

					else:
						room_grid[i][j] = "|"

				#North and south walls, similarly to east and west above
				elif (i == 0 or i == room_height - 1):
					#Place a - if is not in the middle
					if j != int((room_width) / 2):
						room_grid[i][j] = "-"

					#Place a N if there's a north
					elif self.get_north() and i == 0:
						d = "N"
						room_grid[i][j] = d
						room_grid[i][j - 1] = d

					#And an S if there's a south
					elif self.get_south() and i == room_height - 1:
						d = "S"
						room_grid[i][j] = d
						room_grid[i][j - 1] = d
					else:
						room_grid[i][j] = "-"
				#Otherwise put an empty space
				else:
					room_grid[i][j] = " "

		for inner_list in room_grid:
			print("".join(map(str, inner_list)))

	def move(self, dir):
		"""TODO: Returns an adjoining Room object based on a direction given. (i.e. if dir == "NORTH", returns a Room object in the north)."""
		if dir == "NORTH":
			return self.north

		elif dir == "SOUTH":
			return self.south

		elif dir == "EAST":
			return self.east

		elif dir == "WEST":
			return self.west

		else:
			print("Invalid direction.")
			return -1;

	def get_all_compass(self):

		n = s = e = w = "Blocked"
		if self.north:
			n = self.north.get_name()

		if self.south:
			s = self.south.get_name()

		if self.east:
			e = self.east.get_name()

		if self.west:
			w = self.west.get_name()

		return [n, s, e, w]

	def get_north(self):
		return self.north

	def get_south(self):
		return self.south

	def get_east(self):
		return self.east

	def get_west(self):
		return self.west
