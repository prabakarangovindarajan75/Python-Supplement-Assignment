# Problem 82: Remove adjacent duplicates
# Find and fix the error

def remove_adjacent_duplicates(text):
    result = ""
    for char in text:
        if not result or result[-1] != char:
            result += char
    return result

