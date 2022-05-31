num = int(input('Enter a number: '))

candidate = 1

while candidate <= num:
    if num % candidate == 0:
        print(f'{candidate} is a factor of {num}')
    candidate += 1
