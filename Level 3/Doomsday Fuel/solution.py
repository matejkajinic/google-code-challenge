
from fractions import Fraction
from fractions import gcd


def fraction(numerator, denominator=1):
    return 0 if numerator == 0 else Fraction(numerator, denominator)


def subtract(a, b):
    # subtract matrix b from a
    n = xrange(len(a))
    return [[a[i][j] - b[i][j] for j in n] for i in n]


def identity(m):
    # identity matrix for matrix m
    n = xrange(len(m))
    return [[1 if i == j else 0 for j in n] for i in n]


def multiply(a, b):
    # multiply matrices a x b
    return [[sum(i * j for i, j in zip(r, c)) for c in zip(*b)] for r in a]


def invert(a):
    b = identity(a)
    for d in xrange(len(a)):
        to1 = fraction(1, a[d][d])
        for j in xrange(len(a)):
            a[d][j] *= to1
            b[d][j] *= to1
        for i in range(len(a))[0:d] + range(len(a))[d + 1 :]:
            to0 = a[i][d]
            for j in xrange(len(a)):
                a[i][j] = a[i][j] - to0 * a[d][j]
                b[i][j] = b[i][j] - to0 * b[d][j]
    return b


def lcm(a):
    # least common multiple for array
    for i, x in enumerate(a):
        lcm = x if i == 0 else lcm * x // gcd(lcm, x)
    return lcm


def solution(m):
    """
    This problem describes an absorbing Markov Chain.

    The provided data is almost in canonical form, P.  With this matrix,
    we can then use its properties to determine B, the probabilities of
    ending up in a particular absorbing (terminal) state.
              _       _
             |         |
             |  Q   R  |
        P =  |         |
             |  0   I  |
             |_       _|

                        -1
        B =  ( I  -  Q )   * R
    """

    terminal = [not any(row) for row in m]

    if terminal.count(True) == 1:
        return [1, 1]

    p = [
        [
            1
            if terminal[state] and state == next_state
            else fraction(prob, sum(m[state]))
            for next_state, prob in enumerate(probs)
        ]
        for state, probs in enumerate(m)
    ]

    q = [
        [p[i][j] for j, is_terminal in enumerate(terminal) if not is_terminal]
        for i, is_terminal in enumerate(terminal)
        if not is_terminal
    ]

    r = [
        [p[i][j] for j, is_terminal in enumerate(terminal) if is_terminal]
        for i, is_terminal in enumerate(terminal)
        if not is_terminal
    ]

    # probabilities for starting in state 0
    b0 = multiply(invert(subtract(identity(q), q)), r)[0]

    common = lcm([x.denominator for x in b0])

    return [x.numerator * common / x.denominator for x in b0] + [common]
