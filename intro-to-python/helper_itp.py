#Check if a character is a hex digit
def char_is_hex(ch):
    hex_digits = [hex(i)[2:] for i in range(16)]
    for digit in hex_digits:
        if ch == digit:
            return True
    return False
