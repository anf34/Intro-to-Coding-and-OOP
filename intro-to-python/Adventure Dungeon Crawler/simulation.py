from room import Room
from item import Item
from adventurer import Adventurer
from quest import Quest
import sys
from helper import *

#Key:
#if it says #TO DO then I'm pretty sure it's done. Otherwise it's not done

def read_paths(source):
	"""Returns a list of lists according to the specifications in a config file, (source).

	source contains path specifications of the form:
	origin > direction > destination.

	read_paths() interprets each line as a list with three elements, containing exactly those attributes. Each list is then added to a larger list, `paths`, which is returned."""

	#In other words, take a file and split it into a list of lists with each line as the next element of the list and each index of each element is seperated by >
	# TODO
	paths = file_to_lst_lst(source, ">")
	return paths


def create_rooms(paths):
	# """Receives a list of paths and returns a list of rooms based on those paths. Each room will be generated in the order that they are found."""

	room_list = []

	i = 0
	while i < 3:
		for path in paths:
			room_in_list = False
			for room in room_list:
				if room.get_name() == path[i]:
					room_in_list = True
			if not room_in_list:
				new_room = Room(path[i])
				room_list.append(new_room)


		i += 2
#This needs fixing
	for path in paths:
		for room_ in room_list:
			if room_.get_name() == path[0]:
				dest_room = None
				for room_ in room_list:
					if path[2] == room_.get_name():
						dest_room = room_
				room_.set_path(path[1], dest_room)


	# TODO

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

# def assign_dir_to_rooms(rooms_, paths):
# 	rooms_lst_lst = create_rooms(paths)
#
# 	#Below is a list of rooms
# 	rooms_ = []
# 	for room_ in rooms_lst_lst:
#


# TODO: Retrieve info from CONFIG files. Use this information to make Adventurer, Item, Quest, and Room objects.


# TODO: Receive commands from standard input and act appropriately.


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
number_of_items = 4
i = 0
items_ = []
while i < number_of_items:
	items_ = generate_items("items.txt")
	#print(items_[i].get_info())
	i += 1
#print(items_)
#
# #
paths_lst_lst = read_paths("paths.txt")
# # print(paths_lst_lst)
#
# # for room_ in rooms_:
# # 	print(room_.get_name())
# # 	print(room_.get_all_compass())
#
# #print(paths_lst_lst)
rooms_ = create_rooms(paths_lst_lst)

quests_ = generate_quests("quests.txt", items_, rooms_)

for quest_ in quests_:
	print(quest_.get_room_desc())



# Adventure debug
# percy = Adventurer()
#
# percy.take(items_[0])
# print(percy.get_skill())
