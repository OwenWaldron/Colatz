# Collatz

This repository is to house my exploration with the Collatz conjecture. As stated in [Wikipedia](https://en.wikipedia.org/wiki/Collatz_conjecture), the Collatz conjecture is:

> The conjecture asks whether repeating two simple arithmetic operations will eventually transform every positive integer into 1. It concerns sequences of integers in which each term is obtained from the previous term as follows: if a term is even, the next term is one half of it. If a term is odd, the next term is 3 times the previous term plus 1.

It's a very famous unsolved math problem that I've had fun playing around with.

# Preamble

I wanted to explain the way I've been seeing the problem, and add some notation and conventions to speak more readily.

## Reduced Collatz function

When looking at how the Collatz operation affects the binary representation of numbers, I found it useful to think of a reduced Collatz opertion.
First of all, it is worth noting that even numbers are rather uninteresting. The Collatz operation divides even numbers by two until it is odd. This is uninteresting to me as it brings the number "closer" to 1. In binary, this looks like dropping the trailing 0 until there are none left. Thus, it makes sense to me to only care about the odd numbers, and drop any trailing 0's between intermediate steps.  
  
We can therefore define a reduced Collatz funtion (on odd numbers): multiply the numeber by 3, add 1, and drop all trailling 0's.
It is worth noting that for any odd number $x$, then $3x+1$ is even and therefore must have a trailling 0.
  
The $3n+1$ operation is quite interesting in binary. First, examining $3n$, you can notice that $3n = n + 2n$, so we have the original number added to itself, right shifted by one binary digit. This results in interesting behaviour with alternating sequences of 0 and 1, as well as how blocks of consequtive 0's and 1's are affected. The resulting $+1$ turns the rightmost chain of 1's into a chain of 0's and a carry into the next chain of 0's.
Thus, after adding 1, and dropping all of the trailing 0's the reduced collatz function eliminates the 

## Collapsed binary

