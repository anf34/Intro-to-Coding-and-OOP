#Test cases for these

#Given a list or list of tuples this returns true if it finds e in the list.
def str_to_snake_case(text):
    """
    Converts a string to snake_case.
    Handles any case, spaces, and special characters without using `re`.

    Args:
        text (str): The input string.

    Returns:
        str: The string in snake_case.
    """
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Input must be a non-empty string.")

    # Initialize variables
    result = []
    prev_char = None  # Keep track of the previous character for spacing logic

    for char in text:
        if char.isalnum():  # Only allow alphanumeric characters
            if char.isupper() and prev_char and prev_char.islower():
                result.append('_')  # Add underscore before uppercase following a lowercase
            result.append(char.lower())
            prev_char = char
        else:
            # If the current character is a space or special character, replace with '_'
            if prev_char and prev_char != '_':
                result.append('_')  # Prevent consecutive underscores
            prev_char = '_'

    # Join the list and remove trailing underscores
    snake_case = ''.join(result).strip('_')
    return snake_case

def is_string_in_list(lst, target):
    if not isinstance(target, str):
        raise TypeError("Target must be a string.")

    for item in lst:
        if isinstance(item, str):  # If the item is a string
            if item == target:
                return True
        elif isinstance(item, tuple):  # If the item is a tuple
            if target in item:  # Check if the target exists in the tuple
                return True
    return False


#Given a list or list of tuples this returns true if it finds an empty string.
def check_empty_string(lst):
    return is_string_in_list(lst, "")


def check_only_strings(lst):
    return all(isinstance(item, str) for item in lst)

def check_only_tuples(lst):
    return all(isinstance(item, tuple) for item in lst)


def valid_string_tuples(lst):
    return not check_empty_string(lst) and check_only_tuples(lst)

#For a list of strings
def valid_string_list(lst):
    #Checks that all elements are strings
    #if any of the characters list are "" return false
    return check_only_strings(lst) and not check_empty_string(lst)

def camel_to_snake(camel_case_str):
    snake_case_str = ''
    for i, char in enumerate(camel_case_str):
        if char.isupper() and i > 0:
            snake_case_str += '_' + char.lower()
        else:
            snake_case_str += char.lower()
    return snake_case_str
