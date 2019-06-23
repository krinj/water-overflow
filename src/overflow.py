# -*- coding: utf-8 -*-

"""
Wrapper function to calculate the overflow at glass i, j given X litres.
"""

from collections import deque
from src.glass import Glass


__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"


def calculate(i: int=0, j: int=0, k: float=0) -> float:
    """ Calculate how much water is in glass(i, j) after k litres of water is poured
     into the top glass.
        i: the row of the glass
        j: the 'column' of the glass
        k: the amount of water (litres) poured into the top glass.
     """
    return 0


def illustrate(glass: Glass) -> (int, float):
    """ Traverse the glass from this one down and print out the water level at each row. """
    q = deque()
    levels = []

    q.append((glass, 0, True))

    n_glasses = 0
    total_water = 0

    while len(q) > 0:

        node, depth, row_end = q.popleft()

        # We are done.
        if node is None:
            break

        # Ensure we have the array.
        while len(levels) < depth + 1:
            levels.append([])

        # Add the water level.
        level = levels[depth]
        level.append(node.water)
        total_water += node.water
        n_glasses += 1

        # Only add the left child unless we are at the row end.
        entry = (node.left_child, depth + 1, False)
        q.append(entry)

        # Add the right child if we are at the row end.
        if row_end:
            entry = (node.right_child, depth + 1, True)
            q.append(entry)

    # Print out the water levels.
    for i, row in enumerate(levels):
        row_num = str(i).zfill(3)
        str_arr = [f"Row {row_num}: "]

        for x in row:
            str_arr.append(f"{x:.2f}")

        print(" ".join(str_arr))

    print(f"N. Glasses: {n_glasses}")
    print(f"Total Water: {total_water}")
    return n_glasses, total_water
