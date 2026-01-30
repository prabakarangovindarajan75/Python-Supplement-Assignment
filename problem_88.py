# Problem 88: Find all substrings of a string
# Find and fix the error

def all_substrings(text):
    substrings = []
    for i in range(len(text)):
        for j in range(i, len(text)):
            substrings.append(text[i:j+1])
    return substrings

word = "abc"
print(f"All substrings: {all_substrings(word)}")
