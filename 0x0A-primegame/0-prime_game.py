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
    if not nums or x < 1:
        return None
    
    # Find maximum n to optimize our preprocessing
    max_n = max(nums)
    
    # Precompute winners for all possible n values
    winners = precompute_winners(max_n)
    
    maria_wins = 0
    ben_wins = 0
    
    # Process each round using precomputed results
    for i in range(x):
        if i >= len(nums):
            break
            
        n = nums[i]
        
        if winners[n] == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    
    # Determine overall winner
    if maria_wins > ben_wins:
        return "Winner: Maria"
    elif ben_wins > maria_wins:
        return "Winner: Ben"
    else:
        return None


def precompute_winners(max_n):
    """
    Precompute game winners for all n from 1 to max_n using dynamic programming.
    
    The key insight: The game outcome depends only on the count of prime moves available.
    Since Maria goes first, she wins if there's an odd number of prime moves.
    
    Args:
        max_n (int): Maximum value to precompute
        
    Returns:
        list: winners[i] = winner for game with n = i
    """
    if max_n < 1:
        return ["Ben"]
    
    # Generate all primes up to max_n using Sieve of Eratosthenes
    primes = sieve_of_eratosthenes(max_n)
    
    # Convert to set for O(1) lookup
    prime_set = set(primes)
    
    # winners[i] stores the winner for n = i
    winners = ["Ben"] * (max_n + 1)
    
    # For each possible n, determine the winner
    for n in range(1, max_n + 1):
        # Count how many primes are <= n
        prime_count = sum(1 for p in primes if p <= n)
        
        # Maria wins if odd number of primes (she goes first)
        # Ben wins if even number of primes
        if prime_count % 2 == 1:
            winners[n] = "Maria"
        else:
            winners[n] = "Ben"
    
    return winners


def sieve_of_eratosthenes(limit):
    """
    Generate all prime numbers up to limit using Sieve of Eratosthenes.
    
    Args:
        limit (int): Upper limit (inclusive)
        
    Returns:
        list: List of prime numbers up to limit
    """
    if limit < 2:
        return []
    
    # Initialize boolean array - True means potentially prime
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    
    # Sieve algorithm
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            # Mark all multiples of i as composite
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    
    # Collect all prime numbers
    return [i for i in range(2, limit + 1) if is_prime[i]]
