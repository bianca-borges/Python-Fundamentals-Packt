# create tuples
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
letters = ('a', 'b', 'c', 'd', 'e', 'f')
m = ('a', 23, 2.65)

# create nested or 2d tuples
two_dim = ((2, 4), (5, 6), (9, 7))

# accessing items from tuples 2d
print(m[2])
print(two_dim[0][1])

# pack and unpack

packing_tuples = 2, 5, 'Space'
print(packing_tuples)
a, b, c = packing_tuples
print(a)
print(b)
print(c)
print(packing_tuples)

# slicing
print(numbers[2:5])
even_numbers = numbers[1::2]
odd_numbers = numbers[0::2]
print(even_numbers)
print(odd_numbers)

# iterations
for n in numbers:
    print(n**2)

# functions
def area_and_circumference_circle(radius):
    import math
    return (math.pi * radius ** 2, 2 * math.pi * radius)

print(area_and_circumference_circle(9))
