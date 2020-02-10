#!/usr/bin/python

"""
Python Core object Types
"""

import math

def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Assign a string "EE551" to a variable x
    x = "EE551"

    # Assign a string "Stevens" to a variable y

    # Repeat variable y 5 times

    # What is the length of z?

    # Concatenate variable y with string " is good"

    # Replace "good" with "awesome" in variable m and assign it to a new variable n

    return x, y, z, length, m, n


def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome"

    # Split variable n on a delimiter space into a list of substrings as p

    # Get r as all the items past the first of the third substring

    # Create a 3 x 3 matrix as nested list such that 
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]

    # Collect the items in the last column of matrix A using list comprehension as c

    # Collect only the even items of the diagonal of matrix A using list comprehension as d

    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.
    # return o as the ASCII value of "Stevens"

    return p, r, c, d, o


def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"

    # Return a as the item in dictionary f that the key "fruit" maps to

    # Increase the quantity of f by 1 and return the value as f

    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85

    # Add "programmer" to the list of jobs Grace has

    # Return p as the third job Grace has that you recently added

    # Use the sort() function to get sorted keys of amazing_grace in alphabetically ascending order, return the result as k

    return a, f, p, k

numbers_and_strings()
lists()
dictionaries()





