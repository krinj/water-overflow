#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test cases for the overflow module.
"""

import unittest
from src import overflow

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"
__version__ = "0.0.0"


class OverFlowTest(unittest.TestCase):

    def test_overflow(self):
        result = overflow.calculate(i=0, j=0, K=0)
        self.assertEqual(0, result)
