#!/usr/bin/env python3
"""
This module implements the prime game where Maria and Ben take turns
removing numbers from a list of integers. The player who cannot make a move
loses. The winner is determined based on the number of prime numbers
remaining after all possible moves.
"""


def isWinner(x, nums):
    """
    Determine the winner of the prime game across multiple rounds.

    Args:
        x (int): Number of rounds
        nums (list): Array of n values for each round

    Returns:
        str or None: Name of player who won most rounds, or None if tie
    """
    if not nums or x < 1:
        return None

    # Find the maximum n to optimize our sieve
    max_n = max(nums)

    # Use Sieve of Eratosthenes to find all primes up to max_n
    def sieve_of_eratosthenes(limit):
        """Generate list of primes up to limit using Sieve of Eratosthenes"""
        if limit < 2:
            return []

        # Initialize boolean array
        is_prime = [True] * (limit + 1)
        is_prime[0] = is_prime[1] = False

        # Sieve algorithm
        for i in range(2, int(limit**0.5) + 1):
            if is_prime[i]:
                # Mark multiples of i as not prime
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        # Return list of prime numbers
        return [i for i in range(2, limit + 1) if is_prime[i]]

    # Get all primes up to max_n
    primes = sieve_of_eratosthenes(max_n)

    # Precompute prime counts for each possible n
    prime_counts = [0] * (max_n + 1)
    prime_idx = 0

    for n in range(1, max_n + 1):
        prime_counts[n] = prime_counts[n - 1]
        if prime_idx < len(primes) and primes[prime_idx] == n:
            prime_counts[n] += 1
            prime_idx += 1

    maria_wins = 0
    ben_wins = 0

    # Play each round
    for i in range(x):
        n = nums[i]

        # Count primes up to n
        prime_count = prime_counts[n]

        # Maria wins if odd number of primes (she goes first)
        # Ben wins if even number of primes
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def main():
    """Test the function with the provided example"""
    # Test case from the problem
    print("Winner: {}".format(isWinner(3, [4, 5, 1])))
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))


if __name__ == "__main__":
    main()
