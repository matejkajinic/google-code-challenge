def solution(s):
    salutes = 0
    right_walkers = 0

    for char in s:
        if char == '>':
            right_walkers += 1
        elif char == '<':
            salutes += right_walkers * 2

    return salutes

# Example usage:
print(solution(">----<"))  # Output: 2
print(solution("<<>><"))  # Output: 4