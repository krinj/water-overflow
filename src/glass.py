# -*- coding: utf-8 -*-

"""
A representation of a single 'glass'. It is essentially an extended binary tree node.
"""

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"


class Glass:

    def __init__(self, capacity: float=0.25):

        self.left: Glass = None
        self.right: Glass = None
        self.parent: Glass = None

        self.capacity: float = capacity
        self.water: float = 0

    def fill(self, k: float):

        remaining_capacity = self.capacity - self.water
        overflow = max(0.0, k - remaining_capacity)
        fill_amount = k - overflow

        # Fill this glass.
        self.water += fill_amount

        # Fill the left and right child with half the overflow each.
        half_overflow = overflow/2
        self._fill_child(left=True, k=half_overflow)
        self._fill_child(left=False, k=half_overflow)

    def _fill_child(self, left: bool=True, k: float=0):
        pass

    def _create_child(self):
        pass

    def _link_child(self):
        pass
