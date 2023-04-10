def solution(xs):
    pos_values = []
    neg_values = []
    zero_count = 0

    for value in xs:
        if value > 0:
            pos_values.append(value)
        elif value < 0:
            neg_values.append(value)
        else:
            zero_count += 1

    pos_product = 1
    for value in pos_values:
        pos_product *= value

    neg_values.sort()
    if len(neg_values) % 2 != 0:
        # If there are zeros or any positive values, remove the smallest negative value
        if zero_count > 0 or len(pos_values) > 0:
            neg_values.pop()
        # If there's only one negative value and no positive values or zeros, return the negative value
        elif len(neg_values) == 1:
            return str(neg_values[0])

    neg_product = 1
    for value in neg_values:
        neg_product *= value

    max_product = pos_product * neg_product

    # If there are no positive or negative values left, return "0"
    if len(pos_values) == 0 and len(neg_values) == 0:
        return "0"

    return str(max_product)

# Test cases
print(solution([2, 0, 2, 2, 0]))  # Output: "8"
print(solution([-2, -3, 4, -5]))  # Output: "60"
print(solution([-2, 0, 0, 0, 0]))  # Output: "0"