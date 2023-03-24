# write a function that accepts a number and then solves the factorial of that number.  Then have your script prompt the user to input a number, call that function, and display the result to the user. 

# define the factorial function
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
    
 # prompt the user for input   
number = int(input('write a number: '))

# call the factorial function with the input number
result = factorial(number)

# display the result to the user
print(f'The factorial of {number} is {result}')


