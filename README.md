# Assignment-3-Python

Task 1: Calculate Factorial Using a Function 


Problem Statement: Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

#Logic to solve

First Method :
import the math module.

math.factorial(n) directly gives the factorial.

If the user enters a negative number, it shows an error message.

Otherwise, it returns the factorial.

Second Method:
This function is created by yourself without using math.factorial.

If n <= 1, factorial is 1 (because 0! = 1 and 1! = 1).

Otherwise, it recursively calls itself: n × (n-1)!

Good example of recursion!

#######################################################################################################################
Task 2: Using the Math Module for Calculations
 
Problem Statement: Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
     Square root of the number
     Natural logarithm (log base e) of the number
     ine of the number (in radians)
3.   Displays the calculated results.

#Logic to solve

Explanation:

math.sqrt(n) → calculates square root.

math.log(n) → calculates natural log (base e).

math.sin(n) → calculates sine (trigonometric) of the number (in radians).


