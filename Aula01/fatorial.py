# Exercise:
# Problem: Write a recursive function to calculate factorial and determine its time complexity.
# Steps to Solve:
# Define the recursive factorial function.
# Analyse how many times the function is called relative to the input.

def fatorial(n):

    if n == 0 or n == 1:
        return 1

    else:
        return n * fatorial(n-1)


print(fatorial(5))