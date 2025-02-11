#INCOMPLETE



"""
IPv6 Verification
Write a program to verify IPv6 addresses. IPv6 is the most recent Internet Protocol.
An IPv6 address uses 128 bits. We can arrange these bits in eight groups of four hexadecimal digits. Each group is separated from the next group using a colon ":".
A hexadecimal digit is a character in the ranges 0-9, A-F or a-f.
Examples of valid IPv6 addresses
2001:0001:FFFF:739A:0942:1236:1231:1000 is a valid IPv6 address.
2001:1:FFFF:739A:942:1236:1231:1000 is also valid.
Leading zeroes in each group can be omitted.
2001:0001:0000:739A:0942:1236:1231:1000 is valid.
Note that the third group has four 0s.
2001:1:0:739A:942:1236:1231:1000 is also valid, and is the same address as the one above.
Note that in the third group, one 0 had to be preserved for clarification.
Example 1:
$ python ipv6_verify.py
Please enter an IP address: 2001:1:0:739A:942:1236:1231:1000
It is a valid IPv6 address.
Example 2:
$ python ipv6_verify.py
Please enter an IP address: 0003:hfre:5790:7593:ut94:0000:7372:1095
It is not a valid IPv6 address.
"""

#As far as I can tell right now, this problem is trivial.

#Some of the leading 0's are removed so first add them in such that each string is 8 groups of four hex digits
#Remove colons from every input string.
#Check every character is of hex (ie is 0-9 or a-f)

#An example of a valid ip:
valid_ip = "2001:0001:FFFF:739A:0942:1236:1231:1000"


def is_hex_string(s):
    return all(c in "0123456789abcdefABCDEF" for c in s)

def verify_ip(string):
    #Must have 7 colons
    colon_counter = 0
    for ch in string:
        if ch == ":":
            colon_counter += 1
        if ch
    if colon_counter != 7:
        return False

    #Must contain only hex digits
