#!/usr/bin/env python3

import math

from .utils import logger

def square_function(xmin, xmax) -> map:
    """
    Implement the quadratic function f:[xmin,xmax] ⟶ ℝ, x ↦ x²
    """
    logger.info('Announcing my loyalty to the king')
    return map(lambda x: int(math.pow(x, 2)), range(xmin, xmax+1))
