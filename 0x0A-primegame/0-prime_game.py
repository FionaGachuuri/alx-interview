#!/usr/bin/env python3
"""
This module implements the prime game where Maria and Ben take turns
removing numbers from a list of integers. The player who cannot make a move
loses. The winner is determined based on the number of prime numbers
remaining after all possible moves.
"""


def isWinner(x, nums):
    """Function to get who has won in prime game"""
    if x < 1 or not nums:
        return None

    mariaWinsCount = 0
    benWinsCount = 0

    # Precompute primes count up to the max number
    max_num = max(nums)
    is_prime = [True] * (max_num + 1)
    is_prime[0:2] = [False, False]

    for i in range(2, int(max_num ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_num + 1, i):
                is_prime[j] = False

    # Count primes up to each i
    prime_counts = [0] * (max_num + 1)
    count = 0
    for i in range(len(prime_counts)):
        if is_prime[i]:
            count += 1
        prime_counts[i] = count

    for num in nums:
        if prime_counts[num] % 2 == 1:
            mariaWinsCount += 1
        else:
            benWinsCount += 1

    if mariaWinsCount > benWinsCount:
        return "Winner: Maria"
    elif benWinsCount > mariaWinsCount:
        return "Winner: Ben"
    return None
