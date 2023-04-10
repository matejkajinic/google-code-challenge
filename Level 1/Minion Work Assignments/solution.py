def solution(data, n):
    # Create a dictionary to store the count of occurrences of each number in the data list
    count_dict = {}
    for num in data:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    # Filter the data list by removing numbers that occur more than n times
    result = [num for num in data if count_dict[num] <= n]

    return result

# Example usage:
data = [5, 10, 15, 10, 7]
n = 1
print(solution(data, n))  # Output: [5, 15, 7]


# To submit - remove the "Example usage" part