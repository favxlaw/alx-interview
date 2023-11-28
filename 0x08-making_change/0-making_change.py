#!/usr/bin/python3
"""
0. Change comes from within
"""


def makeChange(coins, total):
    """
    Given a pile of coins of different values, determine the fewest number
    of coins needed to meet a given amount total
    """
    if total <= 0:
        return 0

    # Arrange coins in descending order
    # total *= 100
    coins = sorted(coins, reverse=True)
    # print('coins:', coins)

    remainder = total
    count = 0

    while remainder > 0:
        foundCoin = False
        for coin in coins:
            if remainder >= coin:
                remainder -= coin
                count += 1
                foundCoin = True
                break
        if not foundCoin:
            return -1

    return count
  