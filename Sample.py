# Declaring user input variable
x = int(input("Enter your number: "))


# Declaring the function
def fib(num):
    # Returning 1 in the first sequence
    if num == 0 or num == 1:
        return num
    # If the number is greater than 1 return to the next sequence
    else:
        return fib(num - 2) + fib(num - 1)


# Printing the results
print(fib(x))
