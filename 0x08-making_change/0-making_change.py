#!/usr/bin/python3
"""
This module contains a function to determine the fewest number of coins
needed to meet a given amount.
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given total.

    Args:
        coins (list): List of coin values.
        total (int): The target total amount.

    Returns:
        int: Minimum number of coins to make the total,
             or -1 if it's not possible.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
