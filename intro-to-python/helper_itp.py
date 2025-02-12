#Check if a character is a hex digit, doesn't care about upper or lower case.
def char_is_hex(ch):
    hex_digits = [hex(i)[2:] for i in range(16)]
    for digit in hex_digits:
        if ch.lower() == digit.lower():
            return True
    return False
