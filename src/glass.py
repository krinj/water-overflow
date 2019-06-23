# -*- coding: utf-8 -*-

"""
A representation of a single 'glass'. It is essentially an extended binary tree node.
"""

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"


class Glass:

    def __init__(self, capacity: float=0.25):

        self.left_child: Glass = None
        self.right_child: Glass = None

        self.left_parent: Glass = None
        self.right_parent: Glass = None

        self.capacity: float = capacity
        self.water: float = 0

    def fill(self, k: float):
        """ Fill this glass with k litres of water. """

        # Work out how much can go into this glass, and how much shall overflow.
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
        """ Fill the child glass with k litres of water. """

        if k <= 0:
            return

        # We need to create the child if it doesn't exist.
        self._ensure_child(left)
        child = self.left_child if left else self.right_child
        child.fill(k)

    def _ensure_child(self, left: bool=True):
        """ Ensure that a child exists. If it does not, create it."""

        # If the child already exists, then we are done.
        if left and self.left_child is not None:
            return
        elif not left and self.right_child is not None:
            return

        # Create the child and refer to it.
        child = Glass(self.capacity)
        if left:
            self.left_child = child
        else:
            self.right_child = child

        # It must also be bound to its siblings.
        self._link_child(left)

    def _link_child(self, left: bool) -> None:
        """ After a child has been created, it should also be the child of the sibling node. """

        parent = self.left_parent if left else self.right_parent
        if parent is None:
            return

        sibling = parent.left_child if left else parent.right_child
        if sibling is None:
            return

        if left:
            sibling.right_child = self.left_child
        else:
            sibling.left_child = self.right_child
