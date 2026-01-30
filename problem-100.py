# Problem 100: Calculate average of nested lists
# Find and fix the error

def average_nested(nested_list):
    total = 0
    count = 0
    
    for sublist in nested_list:
        for num in sublist:
            total += num
            count += 1
    
    if count == 0:
        return 0  # or return None based on your preference
    
    return total / count

data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"Average: {average_nested(data)}")

