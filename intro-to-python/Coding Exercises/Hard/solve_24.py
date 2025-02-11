#INCOMPLETE

numbers = input("Enter 4 integers: ")

numbers = list(map(int, numbers.split()))
#numbers = [1, 1, 1, 1]

print(numbers)


def is24reachable(numbers):
    max = 1
    reachable = False

    for number in numbers:
        max *= number
    if max <= 24:
        reachable = False
    if reachable:
        print("Yes! 24 is reachable from", numbers)
        return
    print("Noooo :( 24 is unreachable from", numbers)
    return

is24reachable(numbers)


def isNreachable(numbers, target):
    if numbers[0] == target:
        return True
    for number in numbers:
        if target % number == 0:
            numbers.remove(number)
            return isNreachable(numbers, int(target / number))
