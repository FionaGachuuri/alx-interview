#!/usr/bin/python3
"""
Prime Game - Maria and Ben take turns removing prime numbers and their multiples
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
    
    maria_wins = 0
    ben_wins = 0
    
    # Process each round
    for i in range(x):
        if i >= len(nums):
            break
            
        n = nums[i]
        
        if n < 2:
            # No primes available, Maria can't move first, Ben wins
            ben_wins += 1
            continue
        
        # Simulate the game for this round
        winner = simulate_game(n)
        
        if winner == "Maria":
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


def simulate_game(n):
    """
    Simulate a single game round and return the winner.
    
    Args:
        n (int): Upper limit of the set [1, 2, ..., n]
        
    Returns:
        str: "Maria" or "Ben"
    """
    # Create set of available numbers
    available = [True] * (n + 1)  # available[i] = True if i is still in the set
    available[0] = False  # 0 is not in the original set
    
    maria_turn = True
    
    while True:
        # Find the smallest available prime
        prime_found = False
        
        for i in range(2, n + 1):
            if available[i] and is_prime(i):
                # Remove this prime and all its multiples
                for j in range(i, n + 1, i):
                    available[j] = False
                prime_found = True
                break
        
        if not prime_found:
            # Current player can't move, they lose
            if maria_turn:
                return "Ben"  # Maria can't move, Ben wins
            else:
                return "Maria"  # Ben can't move, Maria wins
        
        # Switch turns
        maria_turn = not maria_turn


def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
        n (int): Number to check
        
    Returns:
        bool: True if n is prime, False otherwise
    """
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check odd divisors up to sqrt(n)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
