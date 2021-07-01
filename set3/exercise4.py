# -*- coding: UTF-8 -*-
"""Set 3, Exercise 4."""


import math
import random
from typing import Sequence

# import time


def binary_search(low, high, actual_number):
    """Do a binary search.

    This is going to be your first 'algorithm' in the usual sense of the word!
    you'll give it a range to guess inside, and then use binary search to home
    in on the actual_number.

    Each guess, print what the guess is. Then when you find the number return
    the number of guesses it took to get there and the actual number
    as a dictionary. make sure that it has exactly these keys:
    {"guess": guess, "tries": tries}

    This will be quite hard, especially hard if you don't have a good diagram!

    Use the VS Code debugging tools a lot here. It'll make understanding
    things much easier.
    """
    tries = 0
    guess = 0

    # Write your code in here
    print("Welcome to the guessing game!")
    print("A number between _ and _ ?")
    low = input("Enter a low: ")
    high = input("Enter an high: ")

    print(f"Now, a number between {low} and {high} ?")
    actual_number = input("actual_number: ")

    high = int(high)
    low = int(low)

    actual_number = random.randint(low, high)

    actual_number = False
    low = 0
    high = 100
    while low <= high:
        mid = low + high // 2
        mid = Sequence[mid]
        if mid == actual_number:
            return mid
        elif actual_number < mid:
            high = mid - 1
        else:
            low = mid + 1
        return None

    actual_number_a = 12

    print(binary_search(actual_number_a))


if __name__ == "__main__":
    print(binary_search(1, 100, 5))
    print(binary_search(1, 100, 6))
    print(binary_search(1, 100, 95))
    print(binary_search(1, 51, 5))
    print(binary_search(1, 50, 5))
