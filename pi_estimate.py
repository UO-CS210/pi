"""Estimate the value of Pi with Monte Carlo simulation.
Author:  your name here
Credits:  TBD
"""
import math
import random
import doctest

def in_unit_circle(x: float, y: float) -> bool:
    """Does (x,y) fall within the unit circle, i.e.,
    within a circle with origin (0,0) and radius 1.0?
    Examples:
    >>> in_unit_circle(1.0, 1.0)
    False
    >>> in_unit_circle(-1.0,-1.0)
    False
    >>> in_unit_circle(1.0,0.0)
    True
    >>> in_unit_circle(-0.5,-0.5)
    True
    """
    dist_sqr = x * x + y * y
    return dist_sqr <= 1.0


def probe() -> bool:
    """Determine whether one random probe within a square
    circumscribing the unit circle is within the unit circle.
    """
    x = random.uniform(-1.0, 1.0)
    y = random.uniform(-1.0, 1.0)
    return in_unit_circle(x, y)

def estimate(epsilon=0.0001) -> float:
    """Estimate the value of Pi to an accuracy of epsilon.
    >>> round(estimate(0.01), 1)
    3.1
    >>> round(estimate(0.001), 2)
    3.14
    >>> round(estimate(0.00001), 4)
    3.1416
    """
    prior_estimate = -100.0
    estimate = 100.0
    probe_count = 0
    within_count = 0
    while abs(estimate - prior_estimate) > epsilon / 100.0:
        # Perform 100 more probes in each batch
        for _ in range(10000):
            # Throw one more dart
            probe_count += 1
            if probe():
                within_count += 1
        prior_estimate = estimate
        estimate = 4.0 * within_count / probe_count
    return estimate

def main():
    pi_est = estimate(0.0000001)
    print(pi_est)

if __name__ == "__main__":
    main()




