import time

squares = [num ** 2 for num in range(1, 1000000)]
tup_squares = tuple([num ** 2 for num in range(1, 1000000)])

tic = time.clock()
total = 0
for num in squares:
    total += num
toc = time.clock()
print(num)
print(tic - toc)

tic = time.clock()
total = 0
for num in tup_squares:
    total += num
toc = time.clock()
print(num)
print(tic - toc)
