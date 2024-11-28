'''
Note: Python 
does not have built-in support for Arrays, 
but Python Lists can be used instead.
#=============
'''
cars = ["Ford", "Volvo", "BMW"]

x = cars[1]

print(x)
# #==============
cars = ["Ford", "Volvo", "BMW"]

cars[0] = "Toyota"

print(cars)

x = len(cars)

print(x)
# #===========
cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars)
# #===============
cars.pop(1)

print(cars)
#===========
cars = ["Ford", "Volvo", "BMW","Volvo"]

cars.remove("Volvo")

print(cars)

#==========Note: The list's remove() 
'''method only removes the 
first occurrence of the specified value.
'''
fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits)
#==============
fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)

#===========
cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)

fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)

fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits)

fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)
#tuple

fruits.extend(points)

print(fruits)



