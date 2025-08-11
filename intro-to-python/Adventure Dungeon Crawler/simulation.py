#cd ~/Documents/GIT/Python-projects/intro-to-python/Adventure\ Dungeon\ Crawler

#cd ~/Documents/GIT/Music\ Map

from room import Room
from item import Item
from adventurer import Adventurer
from quest import Quest
import sys
from helper import *

#Make sure create rooms works

#Key:
#if it says #TO DO then I'm pretty sure it's done. Otherwise it's not done

def read_paths(source):
	#DONE
	"""Returns a list of lists according to the specifications in a config file, (source).

	source contains path specifications of the form:
	origin > direction > destination.

	read_paths() interprets each line as a list with three elements, containing exactly those attributes. Each list is then added to a larger list, `paths`, which is returned."""

	#In other words, take a file and split it into a list of lists with each line as the next element of the list and each index of each element is seperated by >

	#input: text from paths.txt origin > direction > destination ...
	#output [[origin, direction, destination], ... ]
	paths = file_to_lst_lst(source, ">")
	return paths


def create_rooms(paths):
	print("hello this is create rooms.")
	# """Receives a list of paths and returns a list of rooms based on those paths. Each room will be generated in the order that they are found."""

	room_list = []



	for path in paths:
		room_in_list = False  #check if room is already in list
		for room in room_list:
			if room.get_name() == path[0]:
				room_in_list = True
				break
		if not room_in_list:
			print("adding new room " + path[0])
			new_room = Room(path[0])
			room_list.append(new_room)
	print("This is me printing paths: ", paths)
	for path in paths:
		for room in room_list:
			if path[0] == room.get_name():
				room.set_path(path[1], path[2])
				print("Moving on", room.get_name(), room.get_north())

	#TO DO 24/7/25, set each rooms neighbouring doors to approrpaite rooms
	#TO DO 1/8/25 check what happens when different starting room check it worsk, also draw the map




# #This needs fixing basically you need to read each path and make each room have a path
# 	for path in paths:
# 		for room_ in room_list:
# 			if room_.get_name() == path[0]:
# 				dest_room = None
# 				for room_ in room_list:
# 					if path[2] == room_.get_name():
# 						dest_room = room_
# 				room_.set_path(pa[1], dest_room)
#
#
# 	# TODO



	return room_list


def generate_items(source):
	#DONE FOR NOW
	"""Returns a list of items according to the specifications in a config file, (source).

	source contains item specifications of the form:
	item name | shortname | skill bonus | will bonus
	"""
	items_list = []
	items_lst_lst = file_to_lst_lst(source, "|")

	for item_ in items_lst_lst:
		items_list.append(Item(item_[0], item_[1], int(item_[2]), int(item_[3])))

	return items_list


def generate_quests(source, items, rooms):
	"""Returns a list of quests according to the specifications in a config file, (source).

	source contains quest specifications of the form:
	reward | action | quest description | before_text | after_text | quest requirements | failure message | success message | quest location
	"""

	#DONE FOR NOW
	quest_list = []
	quests = file_to_lst_lst(source, "|")
	#print(quests)

	for quest_ in quests:
		#print("Test", quest_)
		# def __init__(self, reward, action, desc, before, after, req, fail_msg, pass_msg, room):
		quest_list.append(Quest(quest_[0], quest_[1], quest_[2], quest_[3], quest_[4], quest_[5], quest_[6], quest_[7], quest_[8]))


	return quest_list


def get_quests_info(quests):
	for quest_ in quests:
		print(quest_.get_info())


def get_items_info(items):
	for item_ in items:
		print(item_.get_info())

def check(): #TO DO, add options for each fo the checks
	to_check = input("Check what? ").strip().upper()
	if to_check == "SELF":
		percy.check_self()
	else:
		valid_item = False
		for item_ in percy.get_inv():
			if item_.get_name().strip().upper == to_check:
				print(item_.get_info())
				valid_item = True
				break
		if not valid_item:
			print("You do not have that item yet or you entered an invalid item.")


# def assign_dir_to_rooms(rooms_, paths):
# 	rooms_lst_lst = create_rooms(paths)
#
# 	#Below is a list of rooms
# 	rooms_ = []
# 	for room_ in rooms_lst_lst:
#


# TODO: Retrieve info from CONFIG files. Use this information to make Adventurer, Item, Quest, and Room objects.
#Preprocess start
playing = True
print("Paths:")
paths = read_paths("paths.txt")
print(paths)

print("\nRooms:")
rooms = create_rooms(paths)
for room_ in rooms:
	print(room_.get_name())

# print("\nItems:")
# items = generate_items("items.txt")
# get_items_info(items)
#
# print("\nQuests:")
# quests = generate_quests("quests.txt", items, rooms)
# get_quests_info(quests)


def show_help():
	help_info = """
HELP - Shows some available commands.
LOOK or L - Lets you see the map/room again.
QUESTS - Lists all your active and completed quests.
INV - Lists all the items in your inventory.
CHECK - Lets you see an item (or yourself) in more detail.
NORTH or N - Moves you to the north.
SOUTH or S - Moves you to the south.
EAST or E - Moves you to the east.
WEST or W - Moves you to the west.
QUIT - Ends the adventure.
		"""
	print(help_info)

def quit_game():
	global playing
	print("Bye!")
	playing = False


# TODO: Receive commands from standard input and act appropriately.
percy = Adventurer()

user_input = ""



commands = {
    "HELP": show_help,
	"LOOK": lambda: rooms[0].draw(), #TO DO make it draw current room
	"L": lambda: rooms[0].draw(),
	"QUESTS": lambda: get_quests_info(quests), #TO DO***** #Change this function to the ass. requirements
	"INV": lambda: print(percy.get_inv()), #TO DO FIX FORMAT
	"CHECK": lambda: check(), #TO DO
	"NORTH": lambda: percy.change_location("N", rooms), #TO DO
	"SOUTH": lambda: percy.change_location("S", rooms),
	"EAST": lambda: percy.change_location("E", rooms),
	"WEST": lambda: percy.change_location("W", rooms),
	"QUIT": quit_game,
	"Q": quit_game,

}

#Preprocess end

while playing:
    user_input = input(">>> ").strip().upper()  # Get input, remove spaces, and normalise case

    if user_input in commands:
        commands[user_input]()  # Call the corresponding function
    else:
        print("Invalid command. Type 'HELP' to see available commands.")


# Draw debug:
# r = Room("Library")
# r.draw()
#
# sshield = Item("Shimmering Shield", "Shield", 5, 2)
#
# print(sshield.get_info())
#
#
#Items debug
# number_of_items = 4
# i = 0
# items_ = []
# while i < number_of_items:
# 	items_ = generate_items("items.txt")
# 	#print(items_[i].get_info())
# 	i += 1
# #print(items_)
# #
# # #
# paths_lst_lst = read_paths("paths.txt")
# # print(paths_lst_lst)
#
# # for room_ in rooms_:
# # 	print(room_.get_name())
# # 	print(room_.get_all_compass())
#
# #print(paths_lst_lst)
# rooms_ = create_rooms(paths_lst_lst)
#
# quests_ = generate_quests("quests.txt", items_, rooms_)
#
# for quest_ in quests_:
# 	print(quest_.get_room_desc())
#
#

# Adventure debug
# percy = Adventurer()
#
# percy.take(items_[0])
# print(percy.get_skill())
