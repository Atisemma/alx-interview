#!/usr/bin/python3
"""
Prime Game Module
"""


def is_prime(n):
    """
    Determine if a number is prime
    Args:
        n: number to check
    Returns:
        True if n is prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes_up_to(n):
    """
    Get all prime numbers up to n using Sieve of Eratosthenes
    Args:
        n: upper limit
    Returns:
        List of prime numbers up to n
    """
    if n < 2:
        return []
    # Initialize sieve array
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    # Mark non-prime numbers in sieve
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    # Collect prime numbers
    primes = [i for i in range(2, n + 1) if sieve[i]]
    return primes


def isWinner(x, nums):
    """
    Determine winner of Prime Game
    Args:
        x: number of rounds
        nums: array of n for each round
    Returns:
        Name of winner (Maria/Ben) or None if cannot be determined
    """
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    # Play each round
    for n in nums:
        if n < 2:
            ben_wins += 1
            continue

        # Get prime numbers up to n
        primes = get_primes_up_to(n)

        # If number of prime numbers is even, Ben wins
        # If odd, Maria wins
        if len(primes) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
