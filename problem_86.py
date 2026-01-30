# Problem 86: Find sum of matrix diagonals
# Find and fix the error

def diagonal_sum(matrix):
    n = len(matrix)
    total = 0
    for i in range(n):
        total += matrix[i][i]
        total += matrix[i][n-1-i]
    
    # Remove the middle element once for odd-sized matrices
    if n % 2 == 1:
        total -= matrix[n//2][n//2]
    
    return total

