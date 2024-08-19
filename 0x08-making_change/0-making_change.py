#!/usr/bin/python3
"""
Module for making change using the fewest number of coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list of int): List of coin denominations available
    total (int): The target amount

    Returns:
    int: Fewest number of coins needed to meet total, or -1 if not possible
    """
    if total <= 0:
        return 0

    # Sort coins in descending order for a greedy approach
    coins.sort(reverse=True)

    coin_count = 0
    remaining = total

    for coin in coins:
        if coin <= remaining:
            # Use as many of this coin as possible
            num_coins = remaining // coin
            coin_count += num_coins
            remaining -= num_coins * coin

        if remaining == 0:
            return coin_count

    # going thro all coins, still have a remaining amount, it's not possible
    return -1
