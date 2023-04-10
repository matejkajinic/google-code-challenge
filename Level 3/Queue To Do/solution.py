def xor_sequence(a, b):
    def xor_to_n(n):
        # XOR of all numbers from 0 to n inclusive
        remainder = n % 4
        if remainder == 0:
            return n
        elif remainder == 1:
            return 1
        elif remainder == 2:
            return n + 1
        else:
            return 0

    # XOR of all numbers from a to b inclusive
    return xor_to_n(a - 1) ^ xor_to_n(b)


def solution(start, length):
    checksum = 0

    for i in range(length):
        a = start + i * length
        b = a + length - i - 1
        checksum ^= xor_sequence(a, b)

    return checksum