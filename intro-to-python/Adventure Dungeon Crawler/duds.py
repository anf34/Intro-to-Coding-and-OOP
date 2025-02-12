horizontal = ""
vertical = ""
for i in range(0, room_width):
    if i == 0 or i == room_width - 1:
        horizontal += "+"
        vertical += "|"
    else:
        horizontal += "-"
        vertical += " "

horizontal_north = list(horizontal)
vertical_west = list(vertical)
horizontal_south = horizontal_north.copy()
vertical_east = vertical_west.copy()

if room_width > 2 and room_height > 2:
    if self.get_north():
        d = "N"
        if room_width % 2 == 0:
            horizontal_north[int(room_width / 2)] = d
            horizontal_noth[int(room_width / 2 + 1)] = d
        else:
            horizontal_north[int((room_width - 1) / 2)] = d

    if self.get_east():
        d = "E"
        if room_width % 2 == 0:
            vertical_east[int(room_width / 2)] = d
            vertical_east[int(room_width / 2 + 1)] = d
        else:
            vertical_east[int((room_width - 1) / 2)] = d

    if self.get_south():
        d = "S"
        if room_width % 2 == 0:
            horizontal_south[int(room_width / 2)] = d
            horizontal_south[int(room_width / 2 + 1)] = d
        else:
            horizontal_south[int((room_width - 1) / 2)] = d

    if self.get_west():
        d = "W"
        if room_height % 2 == 0:
            vertical_west[int(room_height / 2)] = d
            vertical_west[int(room_height / 2 + 1)] = d
        else:
            vertical_west[int(room_width + 1 / 2)] = d
horizontal_north = ''.join(horizontal_north)
horizontal_south = ''.join(horizontal_south)
vertical_west_list = vertical_west.copy()
vertical_west = ''.join(vertical_west_list)
#print(vertical_east)
#vertical_east = ''.join(vertical_east)

print(horizontal_north)
for i in range(0, room_height - 2):
    if i % 2 == 0 and i == int(room_height / 2) or i == math.floor((room_height / 2) + 1):
        if self.get_west():
            d = "W"
            if room_height % 2 == 0:
                vertical_west[int(room_height / 2)] = d
                vertical_west[int(room_height / 2 + 1)] = d
            else:
                vertical_west[int(room_width + 1 / 2)] = d
    print(vertical_west)

print(horizontal_south)
