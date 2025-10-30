import random
number = [random.randint(-100, 100) for x in range(10)]
count = 0
for y in number:
    count += y
print(f'Random numbers: {number}')
print(f'Sum of random numbers is {count}')
