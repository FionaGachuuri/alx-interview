#!/usr/bin/python3
"""
Prime Game - Optimized solution using dynamic programming and game theory
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game across multiple rounds.
    Optimized version using precomputed results.

    Args:
        x (int): Number of rounds
        nums (list): Array of n values for each round

    Returns:
        str or None: Winner format or None if tie
    """

    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0
    # Create an array of possible prime numbers
    j = [1 for x in range(sorted(nums)[-1] + 1)]

    # Set 0 and 1 as non-prime
    j[0], j[1] = 0, 0

    # Use the Sieve of Eratosthenes to find all prime numbers
    for i in range(2, len(j)):
        remove_multiples(j, i)

    # Iterate through the nums array
    for i in nums:
        # Count the number of primes up to the current number
        # and determine the winner based on the parity of the sum
        if sum(j[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    # Determine the overall winner
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def remove_multiples(ls, x):
    """
    Removes multiples of a prime number from an array of possible prime
    numbers.

    Args:
        ls (list): List of possible prime numbers
        x (int): Prime number to remove multiples of
    Returns:
        None: The list is modified in place
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
