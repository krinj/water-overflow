# -*- coding: utf-8 -*-

"""
A representation of a single 'glass'. It is essentially an extended binary tree node.
"""

from collections import deque

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

        # BFS Fill.
        q = deque()
        q.append((self, k))

        while len(q) > 0:
            node, amount = q.popleft()
            overflow = node._fill(amount)

            # If there is overflow, ensure and fill the child nodes too.
            if overflow > 0:

                # Ensure that left and right children exist for the next operation.
                left_child = node._ensure_child(left=True)
                right_child = node._ensure_child(left=False)

                # Append them to the queue so we can continue the process.
                q.append((left_child, overflow/2))
                q.append((right_child, overflow/2))

    # ===================================================================================================
    # Private/Support functions.
    # ===================================================================================================

    def _fill(self, k: float) -> float:
        """ Fill this glass with k litres and return the overflow amount."""
        # Work out how much can go into this glass, and how much shall overflow.
        remaining_capacity = self.capacity - self.water
        overflow = max(0.0, k - remaining_capacity)
        fill_amount = k - overflow

        # Fill this glass.
        self.water += fill_amount
        return overflow

    def _ensure_child(self, left: bool=True) -> 'Glass':
        """ Ensure that a child exists. If it does not, create it."""

        # If the child already exists, then we are done.
        if left and self.left_child is not None:
            return self.left_child
        elif not left and self.right_child is not None:
            return self.right_child

        # Create the child and refer to it.
        return self._create_child(left)

    def _create_child(self, left: bool) -> 'Glass':
        """ Create the child glass and ensure that all references are set up properly. """
        child = Glass(self.capacity)

        # Bind the child.
        if left:
            child.right_parent = self
            self.left_child = child
        else:
            child.left_parent = self
            self.right_child = child

        # It must also be bound to its siblings.
        self._link_child(left)
        return child

    def _link_child(self, left: bool) -> None:
        """ After a child has been created, it should also be the child of the sibling node. """

        parent = self.left_parent if left else self.right_parent
        if parent is None:
            return

        sibling = parent.left_child if left else parent.right_child
        if sibling is None:
            sibling = parent._create_child(left)

        if left:
            sibling.right_child = self.left_child
            self.left_child.left_parent = sibling
        else:
            sibling.left_child = self.right_child
            self.right_child.right_parent = sibling
