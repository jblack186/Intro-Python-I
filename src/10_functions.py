# Write a function is_even that will return true if the passed-in number is even.
def is_even(num):
    if num % 2 == 0:
        return True
# YOUR CODE HERE
print(is_even(8))
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
def isItEven(num):
    if num % 2 == 0:
        print('EVEN')
    elif num % 2 != 0:
        print("ODD")
# YOUR CODE HERE

print(isItEven(num))