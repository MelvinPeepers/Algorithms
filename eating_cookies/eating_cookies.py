#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

# Cookies.       Ways to eat

# 0
# —————
# 1

# 1
# —————
# 1

# 2
# —————
# 1,1
# 2

# 3
# —————
# 1, 1, 1
# 1, 2
# 2, 1
# 3

# # Look at the ways to eat (n-1) cookies, then eat one more
# # Now look at the ways to eat (n-2) cookies, then eat 2 at once
# # Now look at the ways to eat (n-3) cookies, then eat 3 at once
# # Now look at the ways to eat (n-4) cookies, then eat 4 at once

# 4
# —————
# 1, 1, 1, 1
# 1, 1, 2
# 1, 2, 1
# 2, 1, 1
# 2, 2
# 1, 3
# 3, 1


# # Look at the ways to eat (n-1) cookies, then eat one more
# # Now look at the ways to eat (n-2) cookies, then eat 2 at once
# # Now look at the ways to eat (n-3) cookies, then eat 3 at once
# # Now look at the ways to eat (n-4) cookies, then eat 4 at once
# # Now look at the ways to eat (n-5) cookies, then eat 5 at once

# 5
# —————
# 1, 1, 1, 1, 1
# 1, 1, 2, 1
# 1, 2, 1, 1
# 2, 1, 1, 1
# 2, 2, 1
# 1, 3, 1
# 3, 1, 1
# 1, 1, 1, 2
# 1, 2, 2
# 2, 1, 2
# 3, 2
# 1,1, 3
# 2, 3

# Plan
# How to turn this into code?
# # Find all combinations of 1, 2, 3 that add up to n
# # Find all possible orderings of those combinations
# 1, 1, 1, 1, 1
# 1, 1, 1, 2
# 1, 1, 3
# 1, 2, 2
# 2, 3


def eating_cookies(n, cache=None):
    if n < 0:
        return 0

    elif n < 2:
        return 1

    else:
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


print(eating_cookies(0))
print(eating_cookies(1))
print(eating_cookies(2))
print(eating_cookies(5))
print(eating_cookies(10))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
