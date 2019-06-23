#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
CLI interface to calculate the overflow.
"""

import argparse
import src.overflow as overflow
from src.glass import Glass

__author__ = "Jakrin Juangbhanich"
__email__ = "juangbhanich.k@gmail.com"
__version__ = "0.0.0"


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--row", default=0, type=int,
                        help="The row of the glass.")
    parser.add_argument("-j", "--col", default=0, type=int,
                        help="The col of the glass.")
    parser.add_argument("-k", "--water", default=0, type=float,
                        help="The amount of water we would like to pour into the top glass")
    parser.add_argument('-v', '--visualize', action="store_true",
                        help="Flag for if we want to visualize the tree.")
    return parser.parse_args()


args = get_args()
i = args.row
j = args.col
k = args.water
should_visualize = args.visualize

if __name__ == "__main__":

    if should_visualize:
        g = Glass()
        g.fill(k)
        overflow.illustrate(g)

    y = overflow.calculate(i, j, k)
