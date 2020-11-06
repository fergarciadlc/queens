# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 13:35:25 2020

@author: Fernando
"""
from itertools import permutations, combinations 


def is_diagonal(point1, point2):
    """
    This function determines whether two queens are in the same diagonal 
    or not.

    Args:
        point1 (tuple of size 2): Position of the first queen.
        point2 (tuple of size 2): Position of the second queen.

    Returns:
        bool: True if the queens are in the same diagonal, False otherwise.
    """
    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    slope = (y2-y1)/(x2-x1)
    
    # Return -> if queens are in same diagonal with the slope equation
    return slope == -1 or slope == 1


def NQueens(n):
    """
    This functions calculates the Eight Queens puzzle for any
    n greater than zero.

    Args:
        n (integer): Number of Queens and size of the board

    Raises:
        TypeError: n must be an integer number.
        ValueError: n must be greater than zero.

    Returns:
        final_solution (list): List of all possible configurations of the 
        puzzle by the given n.

    """
    if type(n) is not int:
        raise TypeError("n must be an integer number.")
    if n < 1:
        raise ValueError("n must be greater than zero.")
    x = range(1, n+1)
    
    # global list_of_permutations # n! -> number of permutations
    list_of_permutations = []
    final_solution = []

    for permutation in permutations(range(1, n+1)):
        y = permutation
        all_permutations = list(zip(x,y)) # coordenates
        list_of_permutations.append(all_permutations)

    for possible_solution in list_of_permutations:
        solutions = []
        # Determine if queens are in the same diagonal
        for piece1, piece2 in combinations(possible_solution, 2):
            solutions.append(is_diagonal(piece1, piece2))
        
        # store the position if NONE of the Queens are in the same diagonal
        if True not in solutions:
            final_solution.append(possible_solution)
            print(possible_solution)

    return final_solution


if __name__ == "__main__":
    final_solution = NQueens(8)
    print(f"Found {len(final_solution)} solutions")
