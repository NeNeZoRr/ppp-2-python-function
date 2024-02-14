# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(A1, A2, A3):
    return max(A1, A2, A3)
# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(numbers):
    result = 1 
    for num in numbers:
        result *= num
    return result
# Write a Python function called rev_string() to reverse a string.
def rev_string(string):
    return string[::-1]
# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.



# Test:
print(max_num(5, 10, 3))
print(mult_list([1, 2, 3, 4]))
print(rev_string("Hi"))