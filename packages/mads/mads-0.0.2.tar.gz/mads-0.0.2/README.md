# Mesh Adaptive Direct Search (MADS)
This package provides an implementation of the Mesh Adaptive Direct Search (MADS) algorithm for gradient-free optimization [1]. More specifically, it uses a modified variant of MADS with orthogonal search directions (OrthoMADS) [2]. However, it abandons using the deterministic Halton sequence for search directions in favor of random search directions, and only performs poll steps.

### Using MADS
The user must provide the following arguments
 - A numpy array of initial design variables
 - A numpy array of upper bounds for the design variables
 - A numpy array of lower bounds for the design variables
 - An objective function to be minimized
 - A stopping tolerance based on the poll size e.g. 1E-6
 - A stopping tolerance based on the objective function e.g. 1E-6
 - A stopping tolerance based on the maximum number of iterations
 - A True/False flag for printing optimization statistics

MADS will perform up to the specified maximum number of design iterations. At each iteration it will perform up to 2N evaluations of the objective function, where N is the number of design variables, skipping points that have already been evaluated. It automatically shrinks/expands the poll size to search the design space, and exits when any one of the three aforementioned stopping criteria is met.

Upon completion, MADS returns
 - The mimimized value of the objective function
 - A numpy array of the design variables that yielded this minima

### Example Applications
Here we provide a simple example problem to minimize f(x,y) = (x-0.3)<sup>2</sup> + (y-0.7)<sup>2</sup>. This is a strictly postive function, which trivially takes a minimum value at [x,y] = [0.3,0.7]. We will an initial guess of [x,y] = [0.5,0.5] and take upper and lower bounds within the unit square.

```python
# Import libraries
import numpy as np
from mads import orthomads

# Define objective function
def objective_function(d):
    f = (d[0] - 0.3)**2 + (d[1] - 0.7)**2
    
    return f

# Define initial guess, bounds, poll tolerance, and max iterations
design_variables = np.array([0, 0])
bounds_lower = np.array([0, 0])
bounds_upper = np.array([1, 1])
dp_tol = 1E-6
nitermax = 1000

# Run the optimizer
mads.orthomads(design_variables, bounds_upper, bounds_lower, objective_function, dp_tol, nitermax, True)
```

This should exit with the following results

```
Optimization Results...
Objective: 0.0000000000 Parameters: [ 0.2999997149  0.6999995360]
```

### References
[1] C. Audet and J. E. Dennis, Mesh Adaptive Direct Search Algorithms for Constrained Optimization, SIAM Journal on Optimization, 2006, 17 (1), 188-217.

[2] M. A. Abramson, C. Audet, J. E. Dennis, and S. Le Digabel, OrthoMADS: A Deterministic MADS Instance with Orthogonal Directions, SIAM Journal on Optimization, 2009, 20 (2), 948-966.