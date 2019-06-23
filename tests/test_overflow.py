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

    def test_overflow(self):
        result = overflow.calculate(i=0, j=0, k=0)
        self.assertEqual(0, result)
