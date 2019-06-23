# Water Overflow
This is the source code for the **Water Overflow** problem.  The goal of this repo is not only to provide an implementation for the solution, but also to demonstrate the approach and infrastructure (TDD, OOP, Documentation, etc). The solution will be implemented in **Python 3.6**, with no external libraries or dependencies (apart from the standard library).

## Problem Statement

> There is a stack of water glasses in a form of triangle as illustrated. Each glass has a 250ml capacity. When a liquid is poured into the top most glass any overflow is evenly distributed between the glasses in the next row. That is, half of the overflow pours into the left glass while the remainder of the overflow pours into the right glass. 

![water_overflow](images/water_overflow.png)

> Write a program that is able to calculate and illustrate how much liquid is in the j-th glass of the i-th row when K litres are poured into the top most glass. The solution can be a command line tool or have a graphical interface.

## Analysis

> This is an ad-hoc journal that I will use to document my analysis and thinking as I form a solution to the problem.

* First, it is worth mentioning that a closed-form solution might exist for this problem. It looks deterministic enough that perhaps a mathematical function of (i, j, K) could be derived. But we won't go down that path for now.
* Immediately, the structure of the glasses looks to me like it would work well with a binary tree.
* An obvious solution would be to create a structure similar to above, and simply simulate the water flow. Once the water flow has been simulated, we can traverse the tree to look for the glass at `i, j`.

## Solution

> The solution I will implement is based on the idea above. Simply creating a data structure to represent the problem, and then simulating it.

#### Steps

1. Create a **Glass** class to present each glass. This will pretty much be a binary tree node, with some additional functionality to accept 'water.' If the glass overflows, the children will be constructed ad-hoc. So the pyramid will grow from the top down.
2. Create a wrapper function that takes `(i, j, K)` as input (also this is the interface described by the problem specification). The wrapper function will create a root node (glass) and fill with K-litres of water.
3. Once the simulation is complete, we will traverse from the root down to node `(i, j)` and return its contents. But as soon as we hit an empty glass, we also know that all glasses below it will be empty, so we can just return that.

#### Pros and Cons

| Pros                                                         | Cons                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Concept is simple and readable. The math and abstraction maps well to the problem description. | We are doing a lot of unnecessary work by calculating the amount of water that has to go into every glass. |
| Solution is extensible. For example, we could easily simulate what happens if water is poured  into **any** glass, not just the root node. | Not very space efficient. We are storing some data for each glass. |
| Once we simulate it for K-litres of liquid, we can look up the solution to any glass in that particular tree. | Probably not going to hold up well for extremely large inputs. |

