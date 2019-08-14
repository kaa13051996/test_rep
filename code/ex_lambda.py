numbers = [2, 1, 3, 4, 7, 11, 18]
squared_numbers = map(lambda n: n**2, numbers)
odd_numbers = filter(lambda n: n % 2 == 1, numbers)
revers_numbs = reversed(numbers)
o = lambda: 11*12
print(o())
for i in odd_numbers:
    print(i)
