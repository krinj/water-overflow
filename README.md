# Water Overflow
This is the source code for the **Water Overflow** problem.  The goal of this repo is not only to provide an implementation for the solution, but also to demonstrate the approach and infrastructure (TDD, OOP, Documentation, etc). The solution will be implemented in **Python 3.6**, with no external libraries or dependencies (apart from the standard library).

## Problem Statement

> There is a stack of water glasses in a form of triangle as illustrated. Each glass has a 250ml capacity. When a liquid is poured into the top most glass any overflow is evenly distributed between the glasses in the next row. That is, half of the overflow pours into the left glass while the remainder of the overflow pours into the right glass. 

![water_overflow](images/water_overflow.png)

> Write a program that is able to calculate and illustrate how much liquid is in the j-th glass of the i-th row when K litres are poured into the top most glass. The solution can be a command line tool or have a graphical interface.

Note: In the diagram there appears to be an error (or the definition of `j` is unclear). On the last row, there are two glasses with index `(i=3, j=1)`. This should not be possible, instead I expect the `j` here should be `2`, and then `3` on the last glass.

## Quick Start

#### Python

You will need Python 3.6 or higher to run the command directly. If your system does not have it, I recommend [installing it via Miniconda](https://docs.conda.io/en/latest/miniconda.html). **No other dependencies should be required**.

1. Clone this repo.

   ```bash
   git clone https://github.com/krinj/water-overflow.git
   ```

2. Enter the directory.

   ```bash
   cd water-overflow
   ```

3. Run the Python script.

   ```bash
   python3 cmd_calculate_overflow.py -i 3 -j 1 -k 3
   ```

You should see the expected output. Try with different values of `i` `j` and `k` to see the results.

```
Found Water (i=3, j=1): 0.25
```

> **Note**: It appears my implementation is not efficient enough to deal with larger levels of k. (e.g. 50).

Also, adding the `-v` flag will cause the program to print out more information about each level.

```bash
python3 cmd_calculate_overflow.py -i 3 -j 1 -k 3 -v
```

Output:

```
Row 000:  0.25
Row 001:  0.25 0.25
Row 002:  0.25 0.25 0.25
Row 003:  0.16 0.25 0.25 0.16
Row 004:  0.17 0.25 0.17
Row 005:  0.05 0.05
N. Glasses: 15
Total Water: 3.0
Found Water (i=3, j=1): 0.25
```

#### Docker

You can also run this program as a Docker container. 

1. Ensure that Docker is installed: <https://docs.docker.com/install/>

2. Build the image.

   ```bash
   # Clone the repo (if you haven't already).
   git clone https://github.com/krinj/water-overflow.git
   
   # Enter the directory (if you haven't already).
   cd water-overflow
   
   # Build Docker image. Here, it is tagged as 'overflow'.
   docker build -t overflow .
   ```

3. Run the container. Once the image is built, you can run it normally using the same arguments as the Python CLI above.

   ```bash
   docker run overflow -i 0 -j 0 -k 3 -v
   ```

#### Arguments

You can also pass in the `--help` flag for more details about the parameters.

```
optional arguments:
  -h, --help            show this help message and exit
  -i ROW, --row ROW     The row of the glass.
  -j COL, --col COL     The col of the glass.
  -k WATER, --water WATER
                        The amount of water we would like to pour into the top
                        glass
  -v, --visualize       Flag for if we want to visualize the tree.

```

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

#### Filling

To fill a glass, we first work out how much capacity we have left, then max it out. If there is overflow, we split it in half and distribute them to the children.

If the children does not exist, they must be created. The most difficult part about creating this step is we must also set up the references to its parents and siblings, since in this tree, each glass could have **two parents** (and two glasses also share the same child).

The private functions that handle this are in `glass.py`: `_ensure_child`, `_create_child` and `_link_child`.

#### Traversal

To traverse to node `(i, j)` we must simply traverse towards the right j times, and then the rest is to the left, up to i.

## Testing

In order to visualize the water levels, there is a function `overflow.illustrate(k: int)` which should produce a rough output for the glasses. It will also traverse the tree and return the number of glasses used and the total water. See `tests/overflow_test.py` for an example.

```python
glass = Glass()
glass.fill(k=3.0)
n_glasses, total_water = overflow.illustrate(glass)
```

>  Expected output:

```
Row 000:  0.25
Row 001:  0.25 0.25
Row 002:  0.25 0.25 0.25
Row 003:  0.16 0.25 0.25 0.16
Row 004:  0.17 0.25 0.17
Row 005:  0.05 0.05
N. Glasses: 15
Total Water: 3.0
```

#### Run All Tests

The tests on this program are quite bare-bones, but should prove out the basic functionality and provide around 96%+ code coverage on the core module.

```bash
# From root directory.
python3 -m unittest tests.test_overflow  
```

