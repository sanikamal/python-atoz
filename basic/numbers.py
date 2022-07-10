# using random
import random

print(random.random())  # random number between 0 and 1
print(random.randint(5, 50))  # random int between 5 and 50
print(random.choice([1, 5, 10, 15, 20, 25]))  # choose a random from this list

x = 50
y = 5.5
z = x + y + 5j

# printing the type of variables
print(x, type(x))
print(y, type(y))
print(z, type(z))

# using hex() and oct() functions
x = 10
print(hex(x))
print(oct(x))
