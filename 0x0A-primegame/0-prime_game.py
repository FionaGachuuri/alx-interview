#!/usr/bin/env python3
"""
This module implements the prime game where Maria and Ben take turns
removing numbers from a list of integers. The player who cannot make a move
loses. The winner is determined based on the number of prime numbers
remaining after all possible moves.
"""


def isWinner(x, nums):
    if x < 1 or not nums:
        return None

    n = max(nums)
    # Sieve of Eratosthenes to find primes up to n
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # Precompute the number of primes up to each number i
    prime_count = [0] * (n + 1)
    count = 0
    for i in range(n + 1):
        if is_prime[i]:
            count += 1
        prime_count[i] = count

    # Determine winner for each round
    maria_wins = 0
    ben_wins = 0

    for num in nums:
        if prime_count[num] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
