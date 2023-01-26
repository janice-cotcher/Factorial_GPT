# This code calculates the factorial of a given number using a recursive function
def factorial(n):
    # If the input number is less than or equal to 1, return 1
    if n <= 1:
        return 1
    else:
        # Otherwise, call the function recursively with the input number decremented by 1
        # and multiply the result by the original input number
        return n * factorial(n-1)

# Test the function with an input of 5
print(factorial(5))
