</hr>

# Approximating the Brachistochrone Curve with a Genetic Algorithm

Vivek Gopalakrishnan | June 9, 2018


**Problem setup:**

Find the least-time path between two points in 2-dimensional space. Assume friction is negligible and that all particles experience a uniform gravitational field.

**Theory:**

This project aims to numerically approximate the Brachistochrone, the path of least-time connecting two points. The path of least-time is defined as the path that, if followed by a particle, would take the least time to travel from one point to another. From classical proofs derived in the 1600s, we know know that this path is a cycloid, the curve obtained by tracing the path of a singular point on a wheel as the wheel rolls through space. Instead of using proof, I indend to find the least-time path using a genetic algorithm.

**Algorithm:**

1. Two points are randomly initialized and fixed in two-dimensional space. 
2. A population of random paths are generated. 
3. The times required to travel these paths are calculated (*time* is the genetic algorithm's fitness score). 
4. Paths with high fitness scores are more likely to be selected in the mating pool. The pool randomly combines different parent paths to create a new generation of paths.
5. Iterate through steps 3 and 4 until the fitnesses converge to a steady value.
6. Visualize these curves and compare to the theoretical values.

**References:**
- [Brachistochrone Curve](https://en.wikipedia.org/wiki/Brachistochrone_curve)
- [Genetic Algorithms](http://natureofcode.com/book/chapter-9-the-evolution-of-code/)

<hr>