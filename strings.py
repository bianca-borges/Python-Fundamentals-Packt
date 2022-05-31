color = input('Please, enter hex color value: ')

r = color[0:2]
g = color[2:4]
b = color[4:6]
print(r, g, b)

r = int(r, 16)
g = int(g, 16)
b = int(b, 16)
print(r, g, b)
