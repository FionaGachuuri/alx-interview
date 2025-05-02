#!/usr/bin/python3
"""
This module provides a function to calculate the minimum number of
operations required to generate exactly `n` 'H' characters in a file,
starting with one 'H'. The only permitted operations are:

1. Copy All
2. Paste

Each "Copy All" followed by a sequence of "Paste" operations
doubles or adds to the current character count.
"""


def next_operation(target: int, operations: int,
                   current_characters: int, add_by: int) -> int:
    """
    Recursive helper function to determine the next operation step.

    Args:
        target (int): The desired number of 'H' characters.
        operations (int): The current count of operations performed.
        current_characters (int): The current count of 'H' characters.
        add_by (int): The number of characters added with each paste.

    Returns:
        int: The minimum number of operations needed to reach `target`.
    """
    if target == current_characters:
        return operations

    if target % current_characters == 0:
        # Perform "Copy All" followed by "Paste"
        return next_operation(
            target,
            operations + 2,
            current_characters * 2,
            current_characters
        )

    # Just "Paste"
    return next_operation(
        target,
        operations + 1,
        current_characters + add_by,
        add_by
    )


def minOperations(n: int) -> int:
    """
    Calculates the fewest number of operations required to produce
    exactly `n` 'H' characters in the file.

    Args:
        n (int): The desired number of characters.

    Returns:
        int: The minimum number of operations, or 0 if n is less than 2.
    """
    if n <= 1:
        return 0

    return next_operation(n, 2, 2, 1)
