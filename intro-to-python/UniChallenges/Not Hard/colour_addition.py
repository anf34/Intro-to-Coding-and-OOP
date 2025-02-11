"""
Change Colour
Since you have done the tutorial, you should be able to extract RGB values from integer representation of a pixel. This challenge requires reading in a pixel value and the RGB changes to be made to the colour.

If the RGB changes make any of the colour channels overflow or underflow, you will need to ensure your code handles this case by allowing an overflow or underflow and maintain the integer is restricted to 24bits and no colour channels interfere with others.

The value change can be represented in separate colour channels or as a pixel value itself.

Example 1:
Please provide a pixel value: 0x505050
Please provide channel values or pixel value: 0x005000
Your new pixel value is: 0x50a050

Example 2:
Please provide a pixel value: 0x505050
Please provide channel values or pixel value: 50 00 00
Your new pixel value is: 0x825050

"""

from helper_itp import char_is_hex


pixel_0 = input("Please provide a pixel value: ")

pixel_1 = input("Please provide channel values or pixel value: ")

#Below is an example of a pixel value:
#pixel_0 = "0x505050"

#And now an example of a channel value:
#pixel_1 = "50 00 00"

#Towards the end I started using similar terms for channel and pixel values, which isn't ideal. This program is too straightforward for me to go through the effort of rectifying all the values though.

#Check if a string is of pixel form
def valid_pixel_value(pixel):
    #Must be of length 8
    if len(pixel) != 8:
        print("Length not 8")
        return False

    #Must have an x in the 1st position and a 0 in the 0th position
    if pixel[0] != "0" or pixel[1] != "x":
        #print(pixel[0])
        #print(pixel[1])
        #print("x not in 1st or 0 not in 0th")
        return False

    #Must consist of only hex integers in every other position (0-9, a-f)
    for i in range(2, len(pixel)):
        if not char_is_hex(pixel[i]):
            #print(pixel[i], "is not hex")
            return False
    return True

#Check if a string is of channel form
def valid_channel_value(channel):
    #Must be of length 8
    if len(channel) != 8:
        print("Length not 8")
        return False

    #Spots 2 and 5 must be " "
    if channel[2] != " " or channel[5] != " ":
        print("Spots 2 and 5 must be " "")
        return False

    #Must consist of only hex integers in every position (0-9, a-f) except 2 and 5
    for i in range(0, len(channel)):
        if i == 2 or i == 5:
            continue
        if not char_is_hex(channel[i]):
            print(channel[i], "is not hex")
            return False
    return True

#Check if a character is a hex digit
#Imported from helper_itp

#Convert pixel string to rgb array
def pixel_to_rgb(pixel):
    if not valid_pixel_value(pixel):
        return -1
    p = []
    p.append(pixel[2] + pixel[3])
    p.append(pixel[4] + pixel[5])
    p.append(pixel[6] + pixel[7])
    return p

#Convert channel string to rgb array
def channel_to_rgb(channel):
    if not valid_channel_value(channel):
        return -1
    p = []
    p.append(channel[0] + channel[1])
    p.append(channel[3] + channel[4])
    p.append(channel[6] + channel[7])
    return p


#Check that the input from the user are valid pixels and the second input is a valid pixel or channel
sum = 0
if valid_pixel_value(pixel_0) and (valid_pixel_value(pixel_1) or valid_channel_value(pixel_1)):
    #print("We're gucci rn")
    p0 = pixel_to_rgb(pixel_0)
    #print(p0)
    p1 = []
    if valid_pixel_value(pixel_1):
        p1 = pixel_to_rgb(pixel_1)
    else:
        p1 = channel_to_rgb(pixel_1)
    #print(p1)
    sum = [f"{(int(x, 16) + int(y, 16)) % 0x100:02X}" for x, y in zip(p0, p1)]
else:
    print("Ensure first input is a pixel and second is either a channel or pixel.")


print("0x" + str(sum[0]) + str(sum[1]) + str(sum[2]))
