#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test cases for the overflow module.
"""

import unittest
from src import overflow
from src.glass import Glass

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"
__version__ = "0.0.0"


class TestData:
    def __init__(self, i: int, j: int, k: float, y: float):
        self.i = i
        self.j = j
        self.k = k
        self.y = y  # Expected output.


class OverFlowTest(unittest.TestCase):

    MAX_CAPACITY_LITRES: float = 0.25  # Capacity per glass in litres.

    def setUp(self):
        self.root_glass: Glass = Glass(self.MAX_CAPACITY_LITRES)

    def test_fill_under_capacity(self):
        """ Check when we fill the root glass with less than its capacity. """
        self.root_glass.fill(0.2)
        self.assertEqual(0.2, self.root_glass.water)

    def test_fill_over_capacity(self):
        """ If we go over, then we should expect the contents to be at capacity. """
        self.root_glass.fill(0.5)
        self.assertEqual(self.MAX_CAPACITY_LITRES, self.root_glass.water)

    def test_visualize(self):
        """ Visualize the glass graph. """
        self.root_glass.fill(3)
        n_glasses, total_water = overflow.illustrate(self.root_glass)
        self.assertEqual(3, total_water)

    def test_overflow(self):
        dataset = [
            TestData(i=0, j=0, k=0.0, y=0.0),
            TestData(i=2, j=1, k=1.0, y=0.125),
            TestData(i=2, j=0, k=1.0, y=0.0625),
            TestData(i=8, j=6, k=10.0, y=0.1484375),
            TestData(i=100, j=5, k=1.0, y=0),
        ]

        for data in dataset:
            # Check we get the right results for the input.
            result = overflow.calculate(i=data.i, j=data.j, k=data.k)
            self.assertEqual(data.y, result)

            # Also check that the water total is correct.
            glass = Glass()
            glass.fill(data.k)
            _, total_water = overflow.illustrate(glass)
            self.assertAlmostEqual(data.k, total_water)
