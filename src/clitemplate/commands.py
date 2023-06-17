#!/usr/bin/env python3

import math

def square_function(xmin, xmax) -> map:
    """
    Compute the quadratic function
    """
    return map(lambda x: int(math.pow(x, 2)), range(xmin, xmax+1))
