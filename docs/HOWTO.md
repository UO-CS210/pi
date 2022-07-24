# Approximate Pi by sampling points

Pi (π) is defined as the ratio of a circle's circumference to its 
diameter, which is twice its radius. It appears in many other 
formulas in mathematics and physics, often in contexts that have 
nothing to do with geometry.  

Because π is an irrational 
number, it is not possible to represent it exactly with a Python 
floating point number, or with any rational number.  The best we can 
do is an approximation.

## Approximation methods

[Wikipedia](https://en.wikipedia.org/wiki/Approximations_of_%CF%80)
describes several methods that have been used for approximating π, 
from about 1000 BCE to current times.  Many of these involve rather 
daunting mathematical formulae involving continued fractions or 
series.  They are efficient, but difficult to understand. 

The method we will use in 
this project is not among the standard approaches, but illustrates a 
general approach for numerical estimation called _Monte Carlo 
simulation_.  Monte Carlo simulation is by no means the best or 
fastest way to estimate π, but it is useful in a wide variety of 
other estimation tasks.  Estimating π is a simple example that will 
help you understand how you might use the Monte Carlo method for 
other problems. 

### Monte Carlo methods

Monte Carlo is a city-state in Europe known for casinos and 
gambling.  Gambling typically involves a random process, such as 
rolling dice or drawing cards.  Monte Carlo simulation is a method 
of estimating something that is difficult to calculate directly by 
randomly generating many examples and counting how many of them 
satisfy a property of the thing we want to estimate.  For example, 
the 
[current best computer Go programs](https://en.wikipedia.org/wiki/AlphaGo) 
estimate the "goodness" of a 
position by playing out a number of random games from the position 
and counting the wins. 

## Estimating π from the area of a circle

We will base our Monte Carlo estimation of π by using a familiar 
formula for the area of a circle, $a = π r^2$. With a little algebra 
we can rewrite this as $\pi = \frac{a}{r^2}$.  So given any value $r$,
if we can obtain a good estimate for the area of a circle with that 
radius, we can divide by the square of $r$ to get an estimate of π.  
In particular, we could choose $r = 1$, because conveniently $1^2 = 
1$ and $\frac{a}{1} = a$.  
